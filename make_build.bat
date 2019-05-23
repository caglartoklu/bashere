CD %~dp0
REM more options: https://pyinstaller.readthedocs.io/en/latest/usage.html
REM pyinstaller --console --onedir bashere.py
python -OO -m PyInstaller --console --onedir bashere.py
