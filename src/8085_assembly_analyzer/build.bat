@echo off
if not exist target\classes mkdir target\classes
java -cp "lib\antlr-4.13.1-complete.jar" org.antlr.v4.Tool -visitor -package main.java -o src\main\java src\main\antlr4\Assembly8085.g4
javac -cp ".;lib\antlr-4.13.1-complete.jar" -d target\classes src\main\java\*.java