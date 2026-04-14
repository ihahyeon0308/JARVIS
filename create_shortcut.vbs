Dim objShell, strDesktopPath, objLink, strLinkPath, strBatPath
Set objShell = CreateObject("WScript.Shell")
strDesktopPath = objShell.SpecialFolders("Desktop")
strBatPath = "C:\Users\UserK\Desktop\Jarvis\wake-up\run.bat"
strLinkPath = strDesktopPath & "\Clap Launcher.lnk"

Set objLink = objShell.CreateShortcut(strLinkPath)
objLink.TargetPath = strBatPath
objLink.WorkingDirectory = "C:\Users\UserK\Desktop\Jarvis\wake-up"
objLink.Description = "박수로 앱 실행"
objLink.Save

MsgBox "바탕화면에 '클랩 런처' 바로가기가 생겼습니다!", vbInformation
