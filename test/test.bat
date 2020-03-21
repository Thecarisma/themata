@echo off
SET THEME=%1
SET CURRENT_DIR=%cd%

del "test_rst\conf.py"
copy "confs\%THEME%.conf.py" "test_rst\conf.py"
cd test_rst\
make html
cd %CURRENT_DIR%
del "test_rst\conf.py"