grammar Assembly8085;

// Parser Rules

program
    : line* EOF
    ;

line
    : (label)? (instruction)? comment? NEWLINE
    | NEWLINE
    ;

label
    : IDENTIFIER ':'
    ;

instruction
    : opcode                         // No operand
    | opcode operand                 // One operand
    | opcode operand ',' operand     // Two operands
    ;

opcode
    : OPCODE_NOARG
    | OPCODE_ONEARG
    | OPCODE_TWOARG
    ;

operand
    : register
    | memoryReference
    | immediate
    | label_reference
    ;

register
    : REG_A | REG_B | REG_C | REG_D | REG_E | REG_H | REG_L | REG_PSW | REG_SP | MEMORY_REFERENCE
    ;

memoryReference
    : MEMORY_REFERENCE
    ;

immediate
    : NUMBER
    ;

label_reference
    : IDENTIFIER
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
REG_A : [Aa];
REG_B : [Bb];
REG_C : [Cc];
REG_D : [Dd];
REG_E : [Ee];
REG_H : [Hh];
REG_L : [Ll];
REG_PSW : [Pp][Ss][Ww];
REG_SP : [Ss][Pp];
MEMORY_REFERENCE : [Mm];

// Numbers
NUMBER
    : HEX_NUM
    | BIN_NUM
    | DEC_NUM
    ;

fragment HEX_NUM : [0-9A-Fa-f]+ [Hh];
fragment BIN_NUM : [01]+ 'B';
fragment DEC_NUM : [0-9]+;

// Identifiers
IDENTIFIER : [A-Za-z_] [A-Za-z0-9_]*;

// Whitespace
WS : [ \t]+ -> skip;