set WshShell = WScript.CreateObject("WScript.Shell")
strStartup = WshShell.SpecialFolders("Startup")
set oShellLink = WshShell.CreateShortcut(strStartup & "\AIRA.lnk")
oShellLink.TargetPath = "c:\Users\Naman\Documents\New folder\AIRA_AI MAIN\AIRA_AI\dist\AIRA\AIRA.exe"
oShellLink.WindowStyle = 1
oShellLink.Description = "Start AIRA AI"
oShellLink.WorkingDirectory = "c:\Users\Naman\Documents\New folder\AIRA_AI MAIN\AIRA_AI"
oShellLink.Save
WScript.Echo "AIRA has been added to Startup!"
