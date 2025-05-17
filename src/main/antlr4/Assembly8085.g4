grammar Assembly8085;

program
    : line* EOF
    ;

line
    : (label)? (instruction | directive)? comment? NEWLINE
    | NEWLINE
    ;

label
    : IDENTIFIER ':'
    ;

instruction
    : opcode (operand (',' operand)*)?
    ;   

directive
    : DIRECTIVE_ORG expressionValue
    | DIRECTIVE_EQU expressionValue
    | DIRECTIVE_DB expressionValue (',' expressionValue)*
    | DIRECTIVE_DS expressionValue
    ;

opcode
    : OPCODE_NOARG       // Instructions with no arguments (like RET, HLT)
    | OPCODE_ONEARG      // Instructions with one argument (like CMA, RAL)
    | OPCODE_TWOARG      // Instructions with two arguments (like MOV, MVI)
    ;

operand
    : register
    | memoryReference
    | immediate
    | label_reference
    ;

register
    : REG_A
    | REG_B
    | REG_C
    | REG_D
    | REG_E
    | REG_H
    | REG_L
    | REG_M
    | REG_PSW
    | REG_SP
    ;

memoryReference
    : MEMORY_REFERENCE
    ;

immediate
    : '#'? expressionValue
    ;

label_reference
    : IDENTIFIER
    ;

expressionValue
    : NUMBER
    | CHARACTER
    | STRING
    | IDENTIFIER
    | expressionValue operator expressionValue
    | '(' expressionValue ')'
    ;

operator
    : '+' | '-' | '*' | '/' | '&' | '|' | '^' | '<<' | '>>'
    ;

comment
    : COMMENT
    ;

// Lexer Rules
NEWLINE 
    : [\r\n]+ 
    ;

COMMENT 
    : ';' ~[\r\n]*
    ;

// Directives
DIRECTIVE_ORG 
    : 'ORG' | '.ORG' | 'org'
    ;

DIRECTIVE_EQU 
    : 'EQU' | '.EQU' | 'equ'
    ;

DIRECTIVE_DB 
    : 'DB' | '.DB' | 'db'
    ;

DIRECTIVE_DS 
    : 'DS' | '.DS' | 'ds'
    ;

// Opcodes
OPCODE_NOARG 
    : 'NOP' | 'HLT' | 'RET' | 'RNZ' | 'RZ' | 'RNC' | 'RC' | 'RPO' | 'RPE' | 'RP' | 'RM'
    | 'XTHL' | 'PCHL' | 'SPHL' | 'XCHG' | 'EI' | 'DI' | 'RIM' | 'SIM' | 'DAA'
    | 'CMA' | 'STC' | 'CMC' | 'RAL' | 'RAR' | 'RLC' | 'RRC'
    ;

OPCODE_ONEARG 
    : 'PUSH' | 'POP' | 'INR' | 'DCR' | 'DAD' | 'INX' | 'DCX'
    | 'CALL' | 'JMP' | 'JNZ' | 'JZ' | 'JNC' | 'JC' | 'JPO' | 'JPE' | 'JP' | 'JM'
    | 'CNZ' | 'CZ' | 'CNC' | 'CC' | 'CPO' | 'CPE' | 'CP' | 'CM'
    | 'ANA' | 'ORA' | 'XRA' | 'ADD' | 'ADC' | 'SUB' | 'SBB' | 'CMP'
    ;

OPCODE_TWOARG 
    : 'MOV' | 'MVI' | 'LXI' | 'LDA' | 'STA' | 'LHLD' | 'SHLD' | 'LDAX' | 'STAX'
    | 'ADI' | 'ACI' | 'SUI' | 'SBI' | 'ANI' | 'ORI' | 'XRI' | 'CPI'
    | 'IN' | 'OUT'
    ;

// Registers
REG_A : 'A' | 'a';
REG_B : 'B' | 'b';
REG_C : 'C' | 'c';
REG_D : 'D' | 'd';
REG_E : 'E' | 'e';
REG_H : 'H' | 'h';
REG_L : 'L' | 'l';
REG_M : 'M' | 'm';
REG_PSW : 'PSW' | 'psw';
REG_SP : 'SP' | 'sp';

MEMORY_REFERENCE
    : 'M' | 'm'
    ;

NUMBER
    : [0-9]+ ('H' | 'h')?           // Decimal or hex with H suffix
    | '0'[Xx][0-9A-Fa-f]+          // Hex with 0x prefix
    | [0-1]+'B'                    // Binary
    ;

CHARACTER
    : '\'' . '\''
    ;

STRING
    : '"' ~["\r\n]* '"'
    ;

IDENTIFIER
    : [A-Za-z][A-Za-z0-9_]*
    ;

WS
    : [ \t]+ -> skip
    ;