import pyaudio
import numpy as np
import subprocess
import time
import sys
import os
import platform
from collections import deque
import struct
import signal
import webbrowser
import ctypes
from ctypes import wintypes


# ── Windows API ──────────────────────────────────────────────
user32   = ctypes.windll.user32
SW_RESTORE = 9

WNDENUMPROC = ctypes.WINFUNCTYPE(wintypes.BOOL, wintypes.HWND, wintypes.LPARAM)


def get_chrome_hwnds():
    """현재 존재하는 Chrome 창 핸들 집합 반환 (제목 무관)"""
    handles = set()

    def _cb(hwnd, _):
        if not user32.IsWindowVisible(hwnd):
            return True
        length = user32.GetWindowTextLengthW(hwnd)
        if length == 0:
            return True
        buf = ctypes.create_unicode_buffer(length + 1)
        user32.GetWindowTextW(hwnd, buf, length + 1)
        title = buf.value
        # Chrome 창이면 수집 (제목에 '– Chrome' 또는 '- Chrome' 포함)
        if '– Chrome' in title or '- Chrome' in title or title.endswith('Chrome'):
            handles.add(hwnd)
        return True

    cb = WNDENUMPROC(_cb)
    user32.EnumWindows(cb, 0)
    return handles


def wait_for_new_hwnd(before: set, timeout=10) -> int | None:
    """before 에 없던 새 Chrome 창 핸들이 나타날 때까지 대기"""
    deadline = time.time() + timeout
    while time.time() < deadline:
        after = get_chrome_hwnds()
        new = after - before
        if new:
            return next(iter(new))   # 새 창 핸들 반환
        time.sleep(0.3)
    return None


def place_windows(left_hwnd: int, right_hwnd: int) -> bool:
    """두 핸들을 화면 반반으로 배치"""
    screen_w = user32.GetSystemMetrics(0)
    screen_h = user32.GetSystemMetrics(1)
    half_w   = screen_w // 2

    print(f"  화면: {screen_w}×{screen_h}  →  각 창: {half_w}×{screen_h}")

    # 최대화 해제
    user32.ShowWindow(left_hwnd,  SW_RESTORE)
    user32.ShowWindow(right_hwnd, SW_RESTORE)
    time.sleep(0.4)

    ok1 = user32.MoveWindow(left_hwnd,  0,      0, half_w, screen_h, True)
    time.sleep(0.15)
    ok2 = user32.MoveWindow(right_hwnd, half_w, 0, half_w, screen_h, True)
    time.sleep(0.15)

    # 앞으로 가져오기
    user32.SetForegroundWindow(left_hwnd)
    time.sleep(0.1)
    user32.SetForegroundWindow(right_hwnd)

    print(f"  MoveWindow 결과 → 왼쪽:{ok1}  오른쪽:{ok2}")
    return bool(ok1 and ok2)


# ── ClapLauncher ─────────────────────────────────────────────
class ClapLauncher:
    def __init__(self, clap_threshold=1800, debug=False):
        self.clap_threshold   = clap_threshold
        self.debug            = debug
        self.os_type          = platform.system()
        self.running          = True
        self.clap_times       = []
        self.last_clap_time   = 0
        self.clap_interval    = 0.7
        self.previous_amplitude = 0
        self.amplitude_history  = deque(maxlen=10)
        self.waiting_for_triple = False
        self.triple_wait_time   = 0
        self.triple_wait_duration = 30

        print(f"🖥️  Detected OS: {self.os_type}")
        self.pa = pyaudio.PyAudio()
        self.audio_stream = None
        signal.signal(signal.SIGINT, self.signal_handler)

    def signal_handler(self, sig, frame):
        print("\n\n👋 Shutting down...")
        self.running = False

    def start_audio_stream(self):
        self.sample_rate  = 16000
        self.frame_length = 512
        try:
            self.audio_stream = self.pa.open(
                rate=self.sample_rate,
                channels=1,
                format=pyaudio.paInt16,
                input=True,
                frames_per_buffer=self.frame_length
            )
            print("🎧 박수를 기다리는 중...")
        except Exception as e:
            print(f"❌ 오디오 스트림 오류: {e}")
            sys.exit(1)

    def detect_clap(self, pcm):
        try:
            audio_data = np.array(pcm, dtype=np.int16)
            amplitude  = np.abs(audio_data).max()
            self.amplitude_history.append(amplitude)
            current_time = time.time()

            if self.debug and amplitude > 500:
                print(f"Amplitude: {amplitude}")

            amplitude_jump = amplitude - self.previous_amplitude
            sharp_attack   = amplitude_jump > (self.clap_threshold * 0.4)
            loud_enough    = amplitude > self.clap_threshold

            if len(self.amplitude_history) >= 3:
                avg_recent    = sum(self.amplitude_history) / len(self.amplitude_history)
                not_sustained = avg_recent < (self.clap_threshold * 0.5)
            else:
                not_sustained = True

            is_clap = loud_enough and (sharp_attack or not_sustained)

            if is_clap and current_time - self.last_clap_time > 0.1:
                self.clap_times.append(current_time)
                self.last_clap_time = current_time
                print(f"👏 박수 #{len(self.clap_times)} 감지!")

                self.clap_times = [t for t in self.clap_times
                                   if current_time - t < self.clap_interval * 2.5]

                if len(self.clap_times) >= 3:
                    span = self.clap_times[-1] - self.clap_times[-3]
                    if span < self.clap_interval * 2.5:
                        self.clap_times.clear()
                        return 3

                if not self.waiting_for_triple and len(self.clap_times) >= 2:
                    span = self.clap_times[-1] - self.clap_times[-2]
                    if span < self.clap_interval:
                        self.clap_times.clear()
                        return 2

            self.previous_amplitude = amplitude

            if self.clap_times and current_time - self.clap_times[-1] > self.clap_interval * 2:
                self.clap_times.clear()

            return 0
        except Exception as e:
            if self.debug:
                print(f"오류: {e}")
            return 0

    def launch_all_apps(self):
        print("\n🚀 박수 두 번 감지! 링크 열기 중...\n")

        if self.os_type != "Windows":
            webbrowser.open_new("https://github.com/ihahyeon0308")
            webbrowser.open_new(
                "https://www.notion.so/TAB-Back-end-2a2d875fb34d80788ec1f7c0b16f2e09"
            )
            return

        # ── 핵심: 열기 전 스냅샷 → 새 핸들만 골라내기 ──────────────

        # 1) 현재 Chrome 창 목록 스냅샷
        snap0 = get_chrome_hwnds()
        print(f"  기존 Chrome 창 수: {len(snap0)}")

        # 2) GitHub 열기
        subprocess.Popen(
            ["start", "chrome.exe", "--new-window", "https://github.com/ihahyeon0308"],
            shell=True
        )
        print("  GitHub 창 대기 중...")
        github_hwnd = wait_for_new_hwnd(snap0, timeout=12)

        if github_hwnd is None:
            print("❌ GitHub 창을 찾지 못했습니다.")
            return
        print(f"  ✅ GitHub 핸들: {github_hwnd}")

        # 3) Notion 열기
        snap1 = get_chrome_hwnds()   # GitHub 포함된 새 스냅샷
        subprocess.Popen(
            ["start", "chrome.exe", "--new-window",
             "https://www.notion.so/TAB-Back-end-2a2d875fb34d80788ec1f7c0b16f2e09"],
            shell=True
        )
        print("  Notion 창 대기 중...")
        notion_hwnd = wait_for_new_hwnd(snap1, timeout=12)

        if notion_hwnd is None:
            print("❌ Notion 창을 찾지 못했습니다.")
            return
        print(f"  ✅ Notion 핸들: {notion_hwnd}")

        # 4) 배치: 왼쪽 = GitHub, 오른쪽 = Notion
        print("  창 배치 중...")
        if place_windows(github_hwnd, notion_hwnd):
            print("✅ 창 배치 완료!")
        else:
            print("⚠️ 배치 중 오류 발생")

        print("\n✨ 완료!\n")

    def play_video(self):
        print("\n🎵 박수 세 번 감지! VS Code 와 영상 열기...\n")
        if self.os_type == "Windows":
            subprocess.Popen("code", shell=True)
            print("✅ VS Code 실행")
            time.sleep(0.5)
            video_dir = os.path.join(os.path.dirname(__file__), "Video")
            if os.path.exists(video_dir):
                for file in os.listdir(video_dir):
                    if file.endswith(".mp4"):
                        os.startfile(os.path.join(video_dir, file))
                        print(f"✅ 영상 재생: {file}")
                        break
            else:
                print("❌ Video 폴더를 찾을 수 없습니다")
        elif self.os_type == "Darwin":
            subprocess.Popen(["open", "-a", "Visual Studio Code"])
            video_dir = os.path.join(os.path.dirname(__file__), "Video")
            for file in os.listdir(video_dir):
                if file.endswith(".mp4"):
                    subprocess.Popen(["open", os.path.join(video_dir, file)])
                    print(f"✅ 영상 재생: {file}")
                    break
        elif self.os_type == "Linux":
            subprocess.Popen(["code"])
            video_dir = os.path.join(os.path.dirname(__file__), "Video")
            for file in os.listdir(video_dir):
                if file.endswith(".mp4"):
                    subprocess.Popen(["xdg-open", os.path.join(video_dir, file)])
                    print(f"✅ 영상 재생: {file}")
                    break
        print("\n✨ 완료!\n")

    def run(self):
        self.start_audio_stream()
        try:
            while self.running:
                pcm_bytes = self.audio_stream.read(self.frame_length, exception_on_overflow=False)
                pcm = struct.unpack_from("h" * self.frame_length, pcm_bytes)
                clap_type = self.detect_clap(pcm)

                if clap_type == 2 and not self.waiting_for_triple:
                    self.launch_all_apps()
                    self.waiting_for_triple = True
                    self.triple_wait_time   = time.time()
                    print("⏳ 30초 안에 박수 세 번 → 영상 열기!")

                elif clap_type == 3 and self.waiting_for_triple:
                    self.play_video()
                    self.waiting_for_triple = False
                    print("\n✨ 모든 기능 실행 완료!\n")
                    os._exit(0)

                if self.waiting_for_triple:
                    if time.time() - self.triple_wait_time > self.triple_wait_duration:
                        self.waiting_for_triple = False
                        print("⏰ 시간 초과! 다시 박수 두 번으로 시작하세요.\n")

        except KeyboardInterrupt:
            print("\n\n👋 종료 중...")
        finally:
            self.cleanup()

    def cleanup(self):
        try:
            if self.audio_stream:
                self.audio_stream.stop_stream()
                self.audio_stream.close()
            if self.pa:
                self.pa.terminate()
        except Exception:
            pass
        print("안녕히 가세요!")


def main():
    print("=" * 60)
    print("  👏 WAKE UP - 박수로 앱 실행!")
    print("=" * 60)
    print("👏👏   박수 두 번 → Notion + GitHub 열기")
    print("👏👏👏  박수 세 번 → VS Code + 영상 재생 (종료)")
    print("\nCtrl+C 로 종료\n")
    debug_mode = "--debug" in sys.argv
    launcher = ClapLauncher(clap_threshold=1800, debug=debug_mode)
    launcher.run()


if __name__ == "__main__":
    main()