@echo off

cd ..\
SET OUTPUT_FOLDER=%CD%\dist\gendoc\
cd docs/
@REM SET THEMES=clear
SET THEMES=clear fandango fluid garri hackish milkish sugar water
if exist "%OUTPUT_FOLDER%" (
    @RD /S /Q "%OUTPUT_FOLDER%"
)
md %OUTPUT_FOLDER%

cmd.exe /c make.bat html
move "build\html\*" "%OUTPUT_FOLDER%\"
for /d %%a in ("build\html\*") do move "%%~fa" "%OUTPUT_FOLDER%\"
type NUL > "%OUTPUT_FOLDER%\.nojekyll"

(for %%a in (%THEMES%) do (
    echo.
    echo ==================================
    echo generating doc for %%a
    echo ==================================
    echo.
    if exist "%%a" (
        cd %%a
        cmd.exe /c make html 
        mkdir %OUTPUT_FOLDER%\%%a\
        move "build\html\*" "%OUTPUT_FOLDER%\%%a\"
        for /d %%b in ("build\html\*") do move "%%~fb" "%OUTPUT_FOLDER%\%%a\"
        cd ..\
    )
))
