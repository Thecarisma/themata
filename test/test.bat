@echo off
SET THEME=%1
SET CURRENT_DIR=%cd%

del "test_rst\conf.py"
copy "confs\%THEME%.conf.py" "test_rst\conf.py"
cd test_rst\
@RD /S /Q "build"
sphinx-build -b html -d build/doctrees  ./ build/html
cd ../
del "test_rst\conf.py"