# 8085 Microprocessor Assembly Syntax Analyzer

This project provides a syntax analyzer for 8085 microprocessor assembly language using ANTLR4.

## Project Structure

- `Assembly8085.g4`: ANTLR4 grammar file for 8085 assembly language
- `Assembler8085.java`: Main class that reads input files and initializes the parser
- `Analyzer8085.java`: Custom visitor class that performs syntax analysis
- `sample.asm`: Sample 8085 assembly program for testing

## Setup Instructions

### Prerequisites

- Java JDK 8 or higher
- ANTLR4 (4.9 or higher)
- Maven (optional, for easier build management)

### Setup

1. Install ANTLR4:
   ```
   pip install antlr4-python3-runtime  # For Python runtime
   # OR
   wget https://www.antlr.org/download/antlr-4.9.2-complete.jar  # For Java
   ```

2. Generate lexer and parser from the grammar:
   ```
   java -jar antlr-4.9.2-complete.jar -visitor Assembly8085.g4
   ```

3. Compile the Java files:
   ```
   javac -cp .:antlr-4.9.2-complete.jar *.java
   ```

### Running the Analyzer

Run the analyzer on a sample input file:

```
java -cp .:antlr-4.9.2-complete.jar Assembler8085 sample.asm
```

## Grammar Features

The 8085 assembly grammar supports:

- Labels with colons (e.g., `START:`)
- Common 8085 instructions (MOV, MVI, LXI, etc.)
- Directives (ORG, EQU, DB, DS)
- Comments beginning with semicolons
- Hexadecimal (with H suffix or 0x prefix), decimal, and binary numbers
- Character literals
- String literals
- Basic expression evaluation

## Analyzer Features

The analyzer performs:

- Syntax validation according to the grammar
- Simple error reporting
- Symbol table management for labels
- Address tracking
- Instruction size calculation
- Basic instruction validation

## Extending the Project

You can extend this project by:

1. Adding more comprehensive validation for specific instructions
2. Implementing a complete assembler that generates machine code
3. Adding support for macros and include files
4. Implementing a more sophisticated expression evaluator
5. Adding optimizations for common patterns

## Limitations

This is a basic syntax analyzer with the following limitations:

- Limited instruction validation (mainly checks operand count)
- Simple expression evaluation (doesn't handle complex expressions)
- No macro support
- Limited error recovery
- No code generation or optimization

## Example Input

```assembly
; Sample 8085 Assembly Program

        ORG     0800H   ; Program starts at address 0800H

START:  MVI     A, 00H  ; Initialize A register with 0
        MVI     B, 05H  ; Set B register to 5 for loop counter

LOOP:   INR     A       ; Increment A
        DCR     B       ; Decrement loop counter
        JNZ     LOOP    ; If not zero, continue loop

        MOV     C, A    ; Store result in C
        STA     RESULT  ; Store A in memory
        HLT             ; Halt execution

RESULT: DS      1       ; Reserve 1 byte for result
```