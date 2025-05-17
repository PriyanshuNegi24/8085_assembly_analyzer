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