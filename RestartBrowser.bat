@echo off
:loop
tasklist /FI "IMAGENAME eq chrome.exe" 2>NUL | find /I /N "chrome.exe">NUL
if "%ERRORLEVEL%"=="1" (
    start "" "C:\Program Files\Google\Chrome\Application\chrome.exe" --guest --app=http://10.20.221.23/can.html"
)
timeout /t 5 /nobreak > NUL
goto loop
