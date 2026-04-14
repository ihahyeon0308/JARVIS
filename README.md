# 👏 Clap Launcher - JARVIS

**박수로 제어하는 앱 실행 프로그램!** 마이크로 박수를 감지하고 박수 패턴으로 앱을 자동으로 실행합니다.

✅ **Windows 최적화** - `run.bat` 한 번의 클릭으로 시작

## 🎬 작동 원리

1. **프로그램 실행** → `run.bat` 더블클릭
2. **박수 2번** 👏👏 → Notion TAB + GitHub 프로필이 **나란히 분할** 배치됨
3. **박수 3번** 👏👏👏 → VS Code + 영상 재생 후 **자동 종료**

## ✨ 기능

- 🎙️ **박수 감지**: 마이크를 통한 정확한 박수 인식
- 🪟 **Smart Window Arrangement**: Chrome 창을 자동으로 왼쪽/오른쪽으로 배치
- 🔗 **커스텀 링크**: Notion, GitHub 등 자신의 링크로 설정 가능
- 🎬 **영상 자동 재생**: Video 폴더의 MP4 파일 자동 인식 및 재생
- ⚡ **빠른 실행**: 한 번의 클릭으로 모든 기능 시작
- 🔌 **간단한 설정**: Python만 설치하면 바로 사용 가능

## 📋 요구사항

- **Python 3.13** (Windows)
- **마이크** (정확한 박수 감지 필수)
- **Google Chrome** (필수)
- **Windows OS**
- PyAudio, NumPy, pvporcupine

## 🚀 빠른 시작

### 1️⃣ 설치

```bash
# 1. 저장소 클론 또는 다운로드
git clone https://github.com/ihahyeon0308/JARVIS.git
cd JARVIS

# 2. Python 3.13 설치 확인
python --version

# 3. 패키지 설치
pip install -r requirements.txt
```

### 2️⃣ 실행

**방법 1: 가장 간단 (추천)**
```bash
run.bat 더블클릭
```

**방법 2: 커맨드라인**
```bash
"C:\Program Files\Python313\python.exe" clap_launcher.py
```

**방법 3: 바탕화면 바로가기**
```bash
# create_shortcut.vbs 더블클릭
# 그 후 바탕화면의 "Clap Launcher" 아이콘 더블클릭
```

## ⚙️ 커스터마이징

### 링크 변경

[clap_launcher.py](clap_launcher.py) 파일에서 `launch_all_apps()` 함수 수정:

```python
def launch_all_apps(self):
    print("\n🚀 박수 두 번 감지! 링크 열기 중...\n")
    if self.os_type == "Windows":
        subprocess.Popen(["start", "chrome.exe", "--new-window", "https://your-github-link.com"], shell=True)
        print("✅ GitHub 프로필 열기")
        time.sleep(1.5)
        
        subprocess.Popen(["start", "chrome.exe", "--new-window", "https://your-notion-page.com"], shell=True)
        print("✅ Notion TAB 열기")
```

### 영상 변경

1. `Video/` 폴더에 새로운 MP4 파일 추가
2. 기존 파일 삭제
3. 자동으로 인식하여 재생됩니다 (파일명 상관 없음)

```bash
# 현재 영상 파일
Video/KakaoTalk_20260414_143119943.mp4
```

### 박수 감도 조정

[clap_launcher.py](clap_launcher.py) 약 183번째 줄:

```python
launcher = ClapLauncher(clap_threshold=1800, debug=False)
# clap_threshold 값을 조정
# 낮을수록 민감 (더 쉽게 감지)
# 높을수록 무뎌짐 (강한 박수만 감지)
```

## 📁 파일 구조

```
JARVIS/
├── clap_launcher.py          # 메인 프로그램  ⭐
├── run.bat                   # Windows 실행 파일 (더블클릭!)
├── arrange_windows.ps1       # Chrome 창 배치 스크립트
├── create_shortcut.vbs       # 바탕화면 바로가기 생성 (선택)
├── requirements.txt          # Python 패키지 목록
├── Video/                    # 영상 폴더
│   └── *.mp4                 # 여기에 MP4 파일 추가
├── Dockerfile                # Docker 설정
└── README.md                 # 이 파일
```

## 🎯 박수 패턴

| 패턴 | 동작 | 상태 |
|------|------|------|
| **👏👏** | Notion + GitHub을 **나란히** 열기 | 대기 모드 전환 |
| **👏👏👏** | VS Code + 영상 재생 후 종료 | 프로그램 자동 종료 |

## 🔧 문제 해결

### 1️⃣ "ModuleNotFoundError: No module named 'pyaudio'"

```bash
# Python 3.13 사용자는 미리 컴파일된 버전 설치
pip install --upgrade pyaudio

# 또는
pip install pipwin
pipwin install pyaudio
```

### 2️⃣ Chrome이 열리지 않음

Chrome이 설치되어 있고 PATH에 등록되었는지 확인:

```bash
where chrome
```

설치되지 않았다면:
- [Google Chrome 다운로드](https://google.com/chrome)에서 설치

### 3️⃣ 박수가 감지되지 않음

**체크리스트:**
1. 마이크가 제대로 연결되었는지 확인
2. Windows 설정 → 개인 정보 보호 → 마이크에서 Python 접근 허용 확인
3. `clap_threshold` 값을 낮춰보기 (더 민감하게)

```bash
# Debug 모드에서 박수 강도 확인
python clap_launcher.py --debug

# 박수 칠 때 진폭(Amplitude) 값이 표시됨
# 값이 충분하지 않으면 clap_threshold 값 낮추기
```

### 4️⃣ "Python 3.13 not found"

Python 3.13이 설치되어 있는지 확인:

```bash
python --version
```

설치되지 않았다면:
- [Python 3.13 다운로드](https://python.org/downloads/) (반드시 3.13!)
- 설치 시 "Add Python to PATH" 체크 필수

### 5️⃣ PowerShell 오류

Windows 10/11에서 PowerShell 권한 문제가 발생하면:

```powershell
# PowerShell을 관리자로 실행 후
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

## 💡 팁

- **박수 감도 미세 조정**: 프로그램을 여러 번 테스트하며 `clap_threshold` 값 추가 조정
- **조용한 환경에서 테스트**: 배경음이 적을수록 정확도 높음
- **Chrome 창 배치**: 자동으로 Notion (오른쪽) + GitHub (왼쪽)로 배치됨
- **영상 변경**: Video 폴더에 새 MP4만 추가하면 자동 인식
- **바탕화면 바로가기**: `create_shortcut.vbs` 더블클릭하면 자동 생성

## 📊 시스템 요구사항

| 항목 | 사양 |
|------|------|
| OS | Windows 10 / 11 |
| Python | 3.13 |
| RAM | 최소 2GB |
| Microphone | 내장/외장 마이크 |
| Chrome | 최신 버전 |

## 🎵 코드 구조

### Main Functions

```python
class ClapLauncher:
    def detect_clap(self):        # 박수 감지
    def launch_all_apps(self):    # 박수 2번 - 앱 실행
    def play_video(self):          # 박수 3번 - 영상 재생
    def arrange_windows(self):     # 창 자동 배치
```

## ✅ 체크리스트

시작하기 전에 확인하세요:

- [ ] Python 3.13 설치됨
- [ ] Google Chrome 설치됨  
- [ ] 마이크 연결됨
- [ ] `pip install -r requirements.txt` 실행 완료
- [ ] `run.bat` 파일 확인

## 📝 라이선스

MIT License - 자유롭게 수정하고 배포할 수 있습니다.

## 👤 개발자

**Hahyun Lee** (@ihahyeon0308)
- AI Developer | Backend & Frontend
- Hankuk University of Foreign Studies (HUFS)
- Computer Science and Engineering

## 🤝 기여하기

개선 사항이나 버그 리포트는 언제든 환영합니다!

---

**박수로 더 빠르게 일해보세요!** 👏🚀
cd wake-up
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

**Linux:**
```bash
# Install portaudio first (required for PyAudio)
sudo apt-get install portaudio19-dev  # Ubuntu/Debian
# OR
sudo dnf install portaudio-devel      # Fedora

git clone https://github.com/tpateeq/wake-up.git
cd wake-up
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 3. Add Your API Key

Open `clap_launcher.py` and add your key at line 32:

```python
PORCUPINE_ACCESS_KEY = "your-key-here"
```

### 4. Configure Your Apps

The script **automatically detects your OS** and uses the appropriate commands! Just customize the app names in the `launch_all_apps()` method (starting at line 267):

**Example configuration:**
```python
def launch_all_apps(self):
    print("\n🚀 DOUBLE CLAP DETECTED! Launching apps...\n")
    
    if self.os_type == "Darwin":  # macOS
        self._launch_app_macos("Visual Studio Code")
        self._launch_app_macos("Google Chrome", args=["--new-window", "https://claude.ai"])
        self._launch_app_macos("Discord")
        
    elif self.os_type == "Windows":
        self._launch_app_windows("code")  # VS Code
        self._launch_app_windows("chrome", args=["https://claude.ai"])
        self._launch_app_windows("discord")
        
    elif self.os_type == "Linux":
        self._launch_app_linux("code")  # VS Code
        self._launch_app_linux("google-chrome", args=["https://claude.ai"])
        self._launch_app_linux("discord")
```

**Customize for your favorite apps:**

*macOS examples:*
```python
self._launch_app_macos("Spotify")
self._launch_app_macos("Slack")
self._launch_app_macos("Safari", args=["https://example.com"])
self._launch_app_macos("Terminal")
```

*Windows examples:*
```python
self._launch_app_windows("spotify")
self._launch_app_windows("slack")
self._launch_app_windows("notepad")
# Full path for apps not in PATH:
subprocess.Popen([r"C:\Program Files\App\app.exe"])
```

*Linux examples:*
```python
self._launch_app_linux("spotify")
self._launch_app_linux("slack")
self._launch_app_linux("firefox", args=["https://example.com"])
self._launch_app_linux("gnome-terminal")
```

### 5. Run

```bash
python3 clap_launcher.py  # macOS/Linux
python clap_launcher.py   # Windows
```

Say **"jarvis"** and start clapping! 🎉

The script will automatically detect your OS:
```
🖥️  Detected OS: Windows  # or Darwin (macOS), or Linux
```

## 🎮 Available Wake Words

- `jarvis` (default)
- `computer`
- `alexa`
- `hey google`
- `hey siri`
- `ok google`
- `terminator`
- `bumblebee`
- `porcupine`
- `blueberry`
- `grapefruit`
- `grasshopper`

**Use a different wake word:**
```bash
python3 clap_launcher.py --wake computer
```

## 🛠️ Customization

### Change the video URL (triple clap action)

Edit the `play_youtube_video()` method around line 333:

```python
def play_youtube_video(self):
    youtube_url = "https://www.instagram.com/p/DMZ58Whvfir/"  # Change to any URL!
    
    # The script automatically handles opening URLs on all platforms
```

You can use any URL - YouTube, Instagram, websites, local files, etc!

### Adjust clap sensitivity

If claps aren't being detected or too many false positives:

```python
# In main() function, around line 416:
launcher = UnifiedLauncher(
    wake_word=wake_word, 
    clap_threshold=1800,  # Lower = more sensitive, Higher = less sensitive
    debug=debug_mode
)
```

**Run with debug mode** to see amplitude levels and find the right threshold:
```bash
python3 clap_launcher.py --debug
```

## 🐛 Troubleshooting

### Wake word not detected

**Check microphone permissions:**
- **macOS**: System Preferences → Security & Privacy → Microphone → Enable Terminal
- **Windows**: Settings → Privacy → Microphone → Enable Python
- **Linux**: Check microphone permissions for your terminal

**Test your microphone:**
- Speak clearly at normal volume
- Make sure you're using the correct microphone (if you have multiple)
- Try a different wake word: `python3 clap_launcher.py --wake computer`

**Check which microphone is being used:**
Run this Python snippet to list available audio devices:
```python
import pyaudio
pa = pyaudio.PyAudio()
for i in range(pa.get_device_count()):
    info = pa.get_device_info_by_index(i)
    if info['maxInputChannels'] > 0:
        print(f"{i}: {info['name']}")
```

### Claps not detected

- **Run debug mode**: `python3 clap_launcher.py --debug`
- Clap sharply and crisply near the microphone
- Watch the amplitude output - it should spike above the threshold
- Adjust `clap_threshold` in code (line 416)
  - Lower value = more sensitive (might pick up background noise)
  - Higher value = less sensitive (might miss soft claps)
- Default threshold is 1800 - adjust based on your debug output

**Example debug output:**
```
Amplitude: 2500 (threshold: 1800)  # ✅ Clap detected!
Amplitude: 1200 (threshold: 1800)  # ❌ Too quiet
```

### "No module named 'pvporcupine'"

```bash
pip install pvporcupine
```

### macOS: "PortAudio not found" or "portaudio.h not found"

This means portaudio wasn't installed before PyAudio:

```bash
# Install portaudio
brew install portaudio

# Then reinstall requirements
pip install -r requirements.txt
```

### Windows: Python 3.13 installation fails

**Recommended solution:** Use Python 3.11 or 3.12 instead.

Some dependencies (numpy, PyAudio) don't have pre-built wheels for Python 3.13 on Windows yet.

1. Download Python 3.12 from [python.org](https://www.python.org/downloads/)
2. Reinstall and create new venv:
   ```bash
   py -3.12 -m venv venv
   venv\Scripts\activate
   pip install -r requirements.txt
   ```

### Windows: Apps not launching

**Check if apps are installed and in PATH:**
```bash
where appname  # Check if app is in PATH
```

**For apps not in PATH:**
Use full path in the script:
```python
subprocess.Popen([r"C:\Program Files\YourApp\app.exe"])
```

**Common app commands:**
- VS Code: `code`
- Chrome: `chrome`
- Discord: `discord`
- Spotify: `spotify`
- Slack: `slack`

### API Key errors

**"Invalid access key" or initialization failed:**
- Make sure you copied the key correctly (no extra spaces)
- Verify the key at [console.picovoice.ai](https://console.picovoice.ai/)
- Check if you're using a v3 key with v4 library (or vice versa)
- Free tier keys have device limits - you may need a new key if using on multiple devices

### Linux: PyAudio installation fails

```bash
# Ubuntu/Debian
sudo apt-get install portaudio19-dev python3-dev

# Fedora
sudo dnf install portaudio-devel python3-devel

# Then reinstall
pip install -r requirements.txt
```

## 📝 How It Works Internally

1. **OS Detection**: Script detects your platform using `platform.system()`
2. **Wake Word**: Porcupine continuously listens for your wake word (offline)
3. **Activation Window**: 5 seconds to perform double clap
4. **App Launch**: OS-appropriate commands launch your apps
5. **Triple Clap Window**: 30 seconds to perform triple clap for secondary action

## 🔒 Privacy

- Wake word detection runs **100% offline** on your machine
- No audio data is sent to any server
- Porcupine API key only validates the library, doesn't transmit audio
- Completely private and secure

## 🤝 Contributing

Contributions welcome! Feel free to:
- Add support for more platforms
- Improve clap detection algorithm
- Add more customization options
- Fix bugs or improve documentation

## 📄 License

MIT License - feel free to use and modify!

---

**⭐ Star this repo if you find it useful!**

**Made with 💙 for productivity enthusiasts**