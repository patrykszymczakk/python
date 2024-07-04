Set WshShell = CreateObject("WScript.Shell")
WshShell.Run chr(34) & "C:\RestartBrowser.bat" & chr(34), 0
Set WshShell = Nothing
