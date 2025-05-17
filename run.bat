@echo off
if "%1"=="" (
    echo Usage: run.bat ^<assembly-file^>
    exit /b 1
)
java -cp "target\classes;lib\antlr-4.13.1-complete.jar" main.java.Assembler8085 %1