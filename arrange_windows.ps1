# Windows API 정의
Add-Type @"
using System;
using System.Runtime.InteropServices;
public class WindowManager {
    [DllImport("user32.dll")]
    public static extern bool MoveWindow(IntPtr hwnd, int x, int y, int nWidth, int nHeight, bool bRepaint);
    
    [DllImport("user32.dll")]
    public static extern bool IsWindow(IntPtr hwnd);
}
"@

# 충분한 시간 대기 - 창이 완전히 로드될 때까지
Start-Sleep -Seconds 4

# Chrome 프로세스 가져오기
$allChromeProcesses = @(Get-Process chrome -ErrorAction SilentlyContinue | Sort-Object StartTime -Descending)

if ($allChromeProcesses.Count -lt 2) {
    exit 1
}

# 가장 최신 2개 프로세스의 메인 윈도우 가져오기
$github_hwnd = 0
$notion_hwnd = 0

# 가장 최신 프로세스들 확인
$latestProcesses = $allChromeProcesses | Select-Object -First 4

foreach ($proc in $latestProcesses) {
    $hwnd = $proc.MainWindowHandle
    
    # 유효한 윈도우인지 확인
    if ([WindowManager]::IsWindow($hwnd)) {
        # 다시 시도 - 윈도우가 제대로 로드되기까지 대기
        $retries = 0
        while ($retries -lt 5) {
            if ($hwnd -ne 0) {
                # 창의 타이틀 확인할 수 없으므로 순서대로 배치
                if ($github_hwnd -eq 0) {
                    $github_hwnd = $hwnd
                    break
                } elseif ($notion_hwnd -eq 0) {
                    $notion_hwnd = $hwnd
                    break
                }
            }
            $retries++
            Start-Sleep -Milliseconds 500
        }
    }
    
    if ($github_hwnd -ne 0 -and $notion_hwnd -ne 0) {
        break
    }
}

# 화면 해상도 기반으로 배치
# 기본값: 1920x1080
$screenWidth = 1920
$screenHeight = 1080
$windowWidth = [Math]::Floor($screenWidth / 2) - 5
$windowHeight = $screenHeight - 30

# 왼쪽 창 배치 (GitHub)
if ($github_hwnd -ne 0) {
    [WindowManager]::MoveWindow($github_hwnd, 0, 0, $windowWidth, $windowHeight, $true)
    Start-Sleep -Milliseconds 300
}

# 오른쪽 창 배치 (Notion)
if ($notion_hwnd -ne 0) {
    [WindowManager]::MoveWindow($notion_hwnd, $windowWidth + 10, 0, $windowWidth, $windowHeight, $true)
}

exit 0


