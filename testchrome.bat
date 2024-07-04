@echo off
set browser=chrome.exe
set incognito_cmd="C:\Program Files\Google\Chrome\Application\chrome.exe" --incognito "http://10.20.221.23/win.html"

:check_browser
tasklist /FI "IMAGENAME eq %browser%" 2>NUL | find /I /N "%browser%">NUL
if "%ERRORLEVEL%"=="1" (
    echo Browser is not running. Waiting for 5 seconds before reopening.
    timeout /t 5 /nobreak >nul
    echo Reopening browser in incognito mode with the default link.
    start "" %incognito_cmd%
) else (
    echo Browser is running. Checking again in 1 minute.
    timeout /t 10 /nobreak >nul
)
goto check_browser
