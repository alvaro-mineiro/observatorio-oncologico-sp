@echo off
cd /d "%~dp0"
python servidor_local.py || py servidor_local.py
pause
