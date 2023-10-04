@echo off
setlocal enabledelayedexpansion

set "psCommand="(new-object -COM 'Shell.Application').BrowseForFolder(0, 'Select the directory containing PDFs', 0x0001, 0).self.path""

for /f "delims=" %%I in ('powershell -command %psCommand%') do set "pdf_directory=%%I"

if "%pdf_directory%"=="" (
    echo No directory selected. Exiting...
    exit /b
)

set "acrobat_path=C:\Program Files\Adobe\Acrobat DC\Acrobat\Acrobat.exe"

for /r "%pdf_directory%" %%F in (*.pdf) do (
    echo Printing: %%~nF
    "%acrobat_path%" /n /t "%%F"
    timeout /t 5 /nobreak > nul  :: Add a 5-second delay between prints
)

endlocal
