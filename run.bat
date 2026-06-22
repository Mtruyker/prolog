@echo off
chcp 65001 > nul
echo.
echo ====================================================
echo    Экспертная система производственной практики
echo ====================================================
echo.
echo Запуск SWI-Prolog...
echo.
"C:\Program Files\swipl\bin\swipl.exe" -g "set_stream(user_output,encoding(utf8)), set_stream(user_error,encoding(utf8)), set_stream(user_input,encoding(utf8))" -l run_cli.pl -g start -t halt
echo.
pause
