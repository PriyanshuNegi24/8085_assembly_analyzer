import sys
import subprocess
from antlr4 import *
from generated.Assembly8085Lexer import Assembly8085Lexer
from generated.Assembly8085Parser import Assembly8085Parser
from generated.Assembly8085Visitor import Assembly8085Visitor
from antlr4.tree.Tree import TerminalNodeImpl

VALID_OPCODES = {
    # Data Transfer
    "MOV", "MVI", "LXI", "LDA", "STA", "LHLD", "SHLD", "LDAX", "STAX", "XCHG",

    # Arithmetic
    "ADD", "ADI", "ADC", "ACI", "SUB", "SUI", "SBB", "SBI", "INR", "DCR", "INX", "DCX", "DAD", "DAA",

    # Logical
    "ANA", "ANI", "XRA", "XRI", "ORA", "ORI", "CMP", "CPI", "CMA", "CMC", "STC",

    # Branching
    "JMP", "JC", "JNC", "JZ", "JNZ", "JP", "JM", "JPE", "JPO",
    "CALL", "CC", "CNC", "CZ", "CNZ", "CP", "CM", "CPE", "CPO",
    "RET", "RC", "RNC", "RZ", "RNZ", "RP", "RM", "RPE", "RPO",

    # Stack, I/O, Machine Control
    "PUSH", "POP", "XTHL", "SPHL", "PCHL",
    "IN", "OUT", "EI", "DI", "HLT", "NOP", "RIM", "SIM"
}

opcode_signature = {
    # Data Transfer Instructions
    'MOV': (2, ['register', 'register_or_memory']),
    'MVI': (2, ['register_or_memory', 'immediate']),
    'LXI': (2, ['register_pair', 'immediate']),
    'LDA': (1, ['memory']),
    'STA': (1, ['memory']),
    'LHLD': (1, ['memory']),
    'SHLD': (1, ['memory']),
    'LDAX': (1, ['register_pair']),
    'STAX': (1, ['register_pair']),
    'XCHG': (0, []),

    # Arithmetic Instructions
    'ADD': (1, ['register_or_memory']),
    'ADI': (1, ['immediate']),
    'ADC': (1, ['register_or_memory']),
    'ACI': (1, ['immediate']),
    'SUB': (1, ['register_or_memory']),
    'SUI': (1, ['immediate']),
    'SBB': (1, ['register_or_memory']),
    'SBI': (1, ['immediate']),
    'INR': (1, ['register_or_memory']),
    'DCR': (1, ['register_or_memory']),
    'INX': (1, ['register_pair']),
    'DCX': (1, ['register_pair']),
    'DAD': (1, ['register_pair']),
    'DAA': (0, []),

    # Logical Instructions
    'ANA': (1, ['register_or_memory']),
    'ANI': (1, ['immediate']),
    'XRA': (1, ['register_or_memory']),
    'XRI': (1, ['immediate']),
    'ORA': (1, ['register_or_memory']),
    'ORI': (1, ['immediate']),
    'CMP': (1, ['register_or_memory']),
    'CPI': (1, ['immediate']),
    'CMA': (0, []),
    'CMC': (0, []),
    'STC': (0, []),

    # Branch Instructions
    'JMP': (1, ['label']),
    'JC': (1, ['label']),
    'JNC': (1, ['label']),
    'JZ': (1, ['label']),
    'JNZ': (1, ['label']),
    'JP': (1, ['label']),
    'JM': (1, ['label']),
    'JPE': (1, ['label']),
    'JPO': (1, ['label']),
    'CALL': (1, ['label']),
    'CC': (1, ['label']),
    'CNC': (1, ['label']),
    'CZ': (1, ['label']),
    'CNZ': (1, ['label']),
    'CP': (1, ['label']),
    'CM': (1, ['label']),
    'CPE': (1, ['label']),
    'CPO': (1, ['label']),
    'RET': (0, []),
    'RC': (0, []),
    'RNC': (0, []),
    'RZ': (0, []),
    'RNZ': (0, []),
    'RP': (0, []),
    'RM': (0, []),
    'RPE': (0, []),
    'RPO': (0, []),

    # Stack, I/O, Machine Control Instructions
    'PUSH': (1, ['register_pair_psw']),
    'POP': (1, ['register_pair_psw']),
    'XTHL': (0, []),
    'SPHL': (0, []),
    'PCHL': (0, []),
    'IN': (1, ['immediate']),
    'OUT': (1, ['immediate']),
    'EI': (0, []),
    'DI': (0, []),
    'HLT': (0, []),
    'NOP': (0, []),
    'RIM': (0, []),
    'SIM': (0, [])
}

class Instruction:
    def __init__(self, opcode, operands):
        self.opcode = opcode
        self.operands = operands

    def __repr__(self):
        return f"{self.opcode} {' '.join(self.operands)}"

class InstructionVisitor(Assembly8085Visitor):
    def __init__(self):
        self.instructions = []
        self.errors = []

    def visitProgram(self, ctx):
        for line_ctx in ctx.line():
            instruction = self.visit(line_ctx)
            if instruction:
                self.instructions.append(instruction)
        return self.instructions

    def visitLine(self, ctx):
        if ctx.instruction():
            return self.visit(ctx.instruction())
        return None

    def visitInstruction(self, ctx):
        opcode = ctx.opcode().getText().upper()
        operands = [op.getText() for op in ctx.operand()] if ctx.operand() else []

        if opcode not in VALID_OPCODES:
            self.errors.append(f"Line {ctx.start.line}: Unknown opcode '{opcode}'")

        self.instructions.append({
            "line": ctx.start.line,
            "opcode": opcode,
            "operands": operands
        })

        return {"opcode": opcode, "operands": operands}

class SemanticAnalyzer(Assembly8085Visitor):
    def __init__(self):
        self.errors = []
        self.labels_defined = set()
        self.labels_used = set()

    def visitLabel(self, ctx):
        label_name = ctx.IDENTIFIER().getText()
        if label_name in self.labels_defined:
            self.errors.append(f"Line {ctx.start.line}: Duplicate label '{label_name}'")
        else:
            self.labels_defined.add(label_name)
        return self.visitChildren(ctx)

    def visitInstruction(self, ctx):
        opcode = ctx.opcode().getText().upper()
        operands = [op.getText() for op in ctx.operand()] if ctx.operand() else []
        expected = opcode_signature.get(opcode)

        if expected:
            expected_count, _ = expected
            if len(operands) != expected_count:
                self.errors.append(f"Line {ctx.start.line}: Opcode '{opcode}' expects {expected_count} operands but got {len(operands)}")
        else:
            self.errors.append(f"Line {ctx.start.line}: Unknown opcode '{opcode}'")

        for op_ctx in ctx.operand() if ctx.operand() else []:
            label_ref_ctx = op_ctx.label_reference()
            if label_ref_ctx:
                self.labels_used.add(label_ref_ctx.getText())

        return self.visitChildren(ctx)

    def finalize(self):
        undefined = self.labels_used - self.labels_defined
        for label in undefined:
            self.errors.append(f"Undefined label used: {label}")

# ---- DOT GRAPH GENERATION ----
def write_dot(tree, parser, filename):
    node_id = 0
    edges = []
    nodes = []

    def recurse(node):
        nonlocal node_id
        current_id = node_id
        node_id += 1

        if isinstance(node, TerminalNodeImpl):
            label = node.getText().replace('"', '\\"')
        else:
            label = parser.ruleNames[node.getRuleIndex()]

        nodes.append(f'  node{current_id} [label="{label}"];')

        for i in range(node.getChildCount()):
            child = node.getChild(i)
            child_id = recurse(child)
            edges.append(f'  node{current_id} -> node{child_id};')

        return current_id

    recurse(tree)

    with open(filename, "w") as f:
        f.write("digraph G {\n")
        for n in nodes:
            f.write(n + "\n")
        for e in edges:
            f.write(e + "\n")
        f.write("}\n")

# ---- MAIN FUNCTION ----
def main():
    input_file = "input.asm"
    input_stream = FileStream(input_file)
    lexer = Assembly8085Lexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = Assembly8085Parser(token_stream)
    tree = parser.program()

    # --- Visitors ---
    visitor = InstructionVisitor()
    visitor.visit(tree)

    # --- Output Instructions ---
    print("Instructions parsed:")
    for ins in visitor.instructions:
        print(f"{ins['opcode']} {' '.join(ins['operands'])}")

    # --- Report Semantic Errors ---
    if visitor.errors:
        print("\nSemantic Errors found:")
        for err in visitor.errors:
            print(err)
    else:
        print("\nNo semantic errors detected!")

    # --- Generate DOT and PNG ---
    dot_file = "parse_tree.dot"
    png_file = "parse_tree.png"
    write_dot(tree, parser, dot_file)

    try:
        subprocess.run(["dot", "-Tpng", dot_file, "-o", png_file], check=True)
        print(f"\n✅ Parse tree image generated: {png_file}")
    except FileNotFoundError:
        print("\n⚠️ Graphviz 'dot' not found. Please install Graphviz and ensure 'dot' is in your PATH.")
    except subprocess.CalledProcessError:
        print("\n❌ Failed to generate PNG from dot file.")

if __name__ == "__main__":
    main()
