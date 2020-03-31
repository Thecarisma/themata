@echo off

SET THEMES=clear
cmd.exe /c make.bat html

(for %%a in (%THEMES%) do (
    echo.
    echo ==================================
    echo generating doc for %%a
    echo ==================================
    echo.
    cd %%a
    make html 
    cd ../
))
