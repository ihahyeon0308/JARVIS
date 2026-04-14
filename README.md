# 👏 Clap Launcher - JARVIS

**Launch apps by clapping!** Detects claps via microphone and automatically launches apps based on clap patterns.

✅ **Windows Optimized** — Start with a single click using `run.bat`

## 🎬 How It Works

1. **Start the program** → Double-click `run.bat`
2. **Clap twice** 👏👏 → Notion tab + GitHub profile open **side by side**
3. **Clap three times** 👏👏👏 → VS Code + video playback, then **auto-exit**

## ✨ Features

- 🎙️ **Clap Detection**: Accurate clap recognition through the microphone
- 🪟 **Smart Window Arrangement**: Automatically positions Chrome windows left and right
- 🔗 **Custom Links**: Configure with your own Notion, GitHub, or any other links
- 🎬 **Auto Video Playback**: Automatically detects and plays MP4 files in the Video folder
- ⚡ **Quick Launch**: Start all features with a single click
- 🔌 **Simple Setup**: Works right away with just Python installed

## 📋 Requirements

- **Python 3.13** (Windows)
- **Microphone** (required for accurate clap detection)
- **Google Chrome** (required)
- **Windows OS**
- PyAudio, NumPy, pvporcupine

## 🚀 Quick Start

### 1️⃣ Installation

```bash
# 1. Clone or download the repository
git clone https://github.com/ihahyeon0308/JARVIS.git
cd JARVIS

# 2. Verify Python 3.13 is installed
python --version

# 3. Install packages
pip install -r requirements.txt
```

### 2️⃣ Running

**Option 1: Easiest (Recommended)**
```bash
Double-click run.bat
```

**Option 2: Command Line**
```bash
"C:\Program Files\Python313\python.exe" clap_launcher.py
```

**Option 3: Desktop Shortcut**
```bash
# Double-click create_shortcut.vbs
# Then double-click the "Clap Launcher" icon on your desktop
```

## ⚙️ Customization

### Change Links

Edit the `launch_all_apps()` function in [clap_launcher.py](clap_launcher.py):

```python
def launch_all_apps(self):
    print("\n🚀 Double clap detected! Opening links...\n")
    if self.os_type == "Windows":
        subprocess.Popen(["start", "chrome.exe", "--new-window", "https://your-github-link.com"], shell=True)
        print("✅ Opening GitHub profile")
        time.sleep(1.5)
        
        subprocess.Popen(["start", "chrome.exe", "--new-window", "https://your-notion-page.com"], shell=True)
        print("✅ Opening Notion tab")
```

### Change Video

1. Add a new MP4 file to the `Video/` folder
2. Delete the existing file
3. It will be detected and played automatically (filename doesn't matter)

```bash
# Current video file
Video/KakaoTalk_20260414_143119943.mp4
```

### Adjust Clap Sensitivity

Around line 183 in [clap_launcher.py](clap_launcher.py):

```python
launcher = ClapLauncher(clap_threshold=1800, debug=False)
# Adjust the clap_threshold value
# Lower = more sensitive (detects softer claps)
# Higher = less sensitive (only detects loud claps)
```

## 📁 File Structure

```
JARVIS/
├── clap_launcher.py          # Main program  ⭐
├── run.bat                   # Windows launcher (double-click!)
├── arrange_windows.ps1       # Chrome window arrangement script
├── create_shortcut.vbs       # Desktop shortcut creator (optional)
├── requirements.txt          # Python package list
├── Video/                    # Video folder
│   └── *.mp4                 # Add MP4 files here
├── Dockerfile                # Docker configuration
└── README.md                 # This file
```

## 🎯 Clap Patterns

| Pattern | Action | State |
|---------|--------|-------|
| **👏👏** | Open Notion + GitHub **side by side** | Switches to standby mode |
| **👏👏👏** | Launch VS Code + play video, then exit | Program auto-exits |

## 🔧 Troubleshooting

### 1️⃣ "ModuleNotFoundError: No module named 'pyaudio'"

```bash
# For Python 3.13 users, install a pre-compiled version
pip install --upgrade pyaudio

# Or
pip install pipwin
pipwin install pyaudio
```

### 2️⃣ Chrome won't open

Verify Chrome is installed and registered in PATH:

```bash
where chrome
```

If not installed:
- Install from [Google Chrome](https://google.com/chrome)

### 3️⃣ Claps not detected

**Checklist:**
1. Confirm microphone is properly connected
2. Windows Settings → Privacy → Microphone → Allow Python access
3. Try lowering the `clap_threshold` value (for more sensitivity)

```bash
# Check clap amplitude in debug mode
python clap_launcher.py --debug

# Amplitude value is shown when clapping
# If values are too low, decrease the clap_threshold
```

### 4️⃣ "Python 3.13 not found"

Verify Python 3.13 is installed:

```bash
python --version
```

If not installed:
- Download from [Python 3.13](https://python.org/downloads/) (must be 3.13!)
- Check "Add Python to PATH" during installation

### 5️⃣ PowerShell errors

If you encounter PowerShell permission issues on Windows 10/11:

```powershell
# Run PowerShell as Administrator, then:
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

## 💡 Tips

- **Fine-tune sensitivity**: Run multiple tests and adjust `clap_threshold` accordingly
- **Test in a quiet environment**: Less background noise means better accuracy
- **Chrome window layout**: Automatically arranged as Notion (right) + GitHub (left)
- **Swap the video**: Just add a new MP4 to the Video folder — it's auto-detected
- **Desktop shortcut**: Double-click `create_shortcut.vbs` to create one automatically

## 📊 System Requirements

| Item | Specification |
|------|---------------|
| OS | Windows 10 / 11 |
| Python | 3.13 |
| RAM | Minimum 2GB |
| Microphone | Built-in or external |
| Chrome | Latest version |

## 🎵 Code Structure

### Main Functions

```python
class ClapLauncher:
    def detect_clap(self):        # Clap detection
    def launch_all_apps(self):    # Double clap - launch apps
    def play_video(self):         # Triple clap - play video
    def arrange_windows(self):    # Auto window arrangement
```

## ✅ Checklist

Make sure before you start:

- [ ] Python 3.13 installed
- [ ] Google Chrome installed
- [ ] Microphone connected
- [ ] `pip install -r requirements.txt` completed
- [ ] `run.bat` file confirmed

---

## Cross-Platform Setup (macOS / Linux)

**Windows:**
```bash
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

### Add Your API Key

Open `clap_launcher.py` and add your key at line 32:

```python
PORCUPINE_ACCESS_KEY = "your-key-here"
```

### Configure Your Apps

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

### Run

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

## 🛠️ Advanced Customization

### Change the video URL (triple clap action)

Edit the `play_youtube_video()` method around line 333:

```python
def play_youtube_video(self):
    youtube_url = "https://www.instagram.com/p/DMZ58Whvfir/"  # Change to any URL!
    
    # The script automatically handles opening URLs on all platforms
```

You can use any URL — YouTube, Instagram, websites, local files, etc!

### Adjust clap sensitivity

If claps aren't being detected or there are too many false positives:

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

## 🐛 Additional Troubleshooting

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
- Watch the amplitude output — it should spike above the threshold
- Adjust `clap_threshold` in code (line 416)

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

```bash
brew install portaudio
pip install -r requirements.txt
```

### Windows: Python 3.13 installation fails

Some dependencies (numpy, PyAudio) don't have pre-built wheels for Python 3.13 on Windows yet. Use Python 3.11 or 3.12 instead:

```bash
py -3.12 -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

### Windows: Apps not launching

```bash
where appname  # Check if app is in PATH
```

**For apps not in PATH:**
```python
subprocess.Popen([r"C:\Program Files\YourApp\app.exe"])
```

**Common app commands:** `code`, `chrome`, `discord`, `spotify`, `slack`

### API Key errors

- Make sure you copied the key correctly (no extra spaces)
- Verify the key at [console.picovoice.ai](https://console.picovoice.ai/)
- Check if you're using a v3 key with v4 library (or vice versa)
- Free tier keys have device limits — you may need a new key if using on multiple devices

### Linux: PyAudio installation fails

```bash
# Ubuntu/Debian
sudo apt-get install portaudio19-dev python3-dev

# Fedora
sudo dnf install portaudio-devel python3-devel

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

## 📝 License

MIT License — feel free to use and modify!

## 👤 Developer

**Hahyun Lee** (@ihahyeon0308)
- AI Developer | Backend & Frontend
- Hankuk University of Foreign Studies (HUFS)
- Computer Science and Engineering

---

**Work faster with a clap!** 👏🚀

⭐ Star this repo if you find it useful!

**Made with 💙 for productivity enthusiasts**