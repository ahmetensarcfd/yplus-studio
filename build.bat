@echo off
setlocal enabledelayedexpansion
cd /d "%~dp0"
echo ==================================================
echo    Y+ STUDIO  -  .exe derleme (build)
echo ==================================================
echo.

REM --- Python launcher tespiti ---
where py >nul 2>&1
if %errorlevel%==0 ( set "PY=py -3" ) else ( set "PY=python" )

echo [1/4] Gerekli paketler kuruluyor (pywebview, pythonnet, pyinstaller)...
%PY% -m pip install --upgrade pip >nul 2>&1
%PY% -m pip install --upgrade pywebview pythonnet pyinstaller
if errorlevel 1 goto :err

echo.
echo [2/4] PyInstaller ile tek dosya .exe derleniyor...
%PY% -m PyInstaller --noconfirm --onefile --noconsole --name yplusstudio ^
   --add-data "index.html;." ^
   --collect-all webview ^
   --exclude-module tkinter ^
   app.py
if errorlevel 1 goto :err

echo.
echo [3/4] exe tasiniyor, gecici dosyalar temizleniyor...
if exist "dist\yplusstudio.exe" ( move /Y "dist\yplusstudio.exe" "yplusstudio.exe" >nul )
rmdir /S /Q build >nul 2>&1
rmdir /S /Q dist >nul 2>&1
rmdir /S /Q __pycache__ >nul 2>&1
del /Q yplusstudio.spec >nul 2>&1

echo.
if exist "yplusstudio.exe" (
  echo [4/4] BASARILI:  yplusstudio.exe hazir.  Uygulama baslatiliyor...
  start "" "%~dp0yplusstudio.exe"
) else (
  echo [4/4] UYARI: yplusstudio.exe bulunamadi, loglari kontrol edin.
  pause
)
exit /b 0

:err
echo.
echo HATA: derleme basarisiz oldu. Yukaridaki mesaja bakin