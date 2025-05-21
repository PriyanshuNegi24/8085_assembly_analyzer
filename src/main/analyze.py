import subprocess
from antlr4 import *
from generated.Assembly8085Lexer import Assembly8085Lexer
from generated.Assembly8085Parser import Assembly8085Parser
from generated.Assembly8085Visitor import Assembly8085Visitor
from antlr4.error.ErrorListener import ErrorListener
from antlr4.tree.Tree import TerminalNodeImpl

VALID_OPCODES = {
    "MOV", "MVI", "LXI", "LDA", "STA", "LHLD", "SHLD", "LDAX", "STAX", "XCHG",
    "ADD", "ADI", "ADC", "ACI", "SUB", "SUI", "SBB", "SBI", "INR", "DCR", "INX", "DCX", "DAD", "DAA",
    "ANA", "ANI", "XRA", "XRI", "ORA", "ORI", "CMP", "CPI", "CMA", "CMC", "STC",
    "JMP", "JC", "JNC", "JZ", "JNZ", "JP", "JM", "JPE", "JPO",
    "CALL", "CC", "CNC", "CZ", "CNZ", "CP", "CM", "CPE", "CPO",
    "RET", "RC", "RNC", "RZ", "RNZ", "RP", "RM", "RPE", "RPO",
    "PUSH", "POP", "XTHL", "SPHL", "PCHL",
    "IN", "OUT", "EI", "DI", "HLT", "NOP", "RIM", "SIM"
}

class CollectingErrorListener(ErrorListener):
    def __init__(self):
        self.errors = []

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        self.errors.append(f"line {line}:{column} {msg}")

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
        opcode = ctx.opcode().getText().upper() if ctx.opcode() else "<missing>"
        operands = [op.getText() for op in ctx.operand()] if ctx.operand() else []

        if opcode not in VALID_OPCODES:
            self.errors.append(f"Line {ctx.start.line}: Unknown or missing opcode '{opcode}'")

        return {"opcode": opcode, "operands": operands}

class SemanticAnalyzer(Assembly8085Visitor):
    def __init__(self):
        self.labels = set()
        self.used_labels = []
        self.errors = []

    def visitProgram(self, ctx):
        for line_ctx in ctx.line():
            self.visit(line_ctx)
        return

    def visitLine(self, ctx):
        # Collect label definitions
        if ctx.label():
            label = ctx.label().IDENTIFIER().getText()
            if label in self.labels:
                self.errors.append(f"Duplicate label: {label}")
            self.labels.add(label)
        # Check instructions for label usage
        if ctx.instruction():
            self.visit(ctx.instruction())
        return

    def visitInstruction(self, ctx):
        opcode = ctx.opcode().getText().upper() if ctx.opcode() else "<missing>"
        operands = [op.getText() for op in ctx.operand()] if ctx.operand() else []

        expected_operands = {
            "MOV": 2, "MVI": 2, "LXI": 2, "LDA": 1, "STA": 1, "LHLD": 1, "SHLD": 1,
            "LDAX": 1, "STAX": 1, "XCHG": 0, "ADD": 1, "ADI": 1, "ADC": 1, "ACI": 1,
            "SUB": 1, "SUI": 1, "SBB": 1, "SBI": 1, "INR": 1, "DCR": 1, "INX": 1,
            "DCX": 1, "DAD": 1, "DAA": 0, "ANA": 1, "ANI": 1, "XRA": 1, "XRI": 1,
            "ORA": 1, "ORI": 1, "CMP": 1, "CPI": 1, "CMA": 0, "CMC": 0, "STC": 0,
            "JMP": 1, "JC": 1, "JNC": 1, "JZ": 1, "JNZ": 1, "JP": 1, "JM": 1,
            "JPE": 1, "JPO": 1, "CALL": 1, "CC": 1, "CNC": 1, "CZ": 1, "CNZ": 1,
            "CP": 1, "CM": 1, "CPE": 1, "CPO": 1, "RET": 0, "RC": 0, "RNC": 0,
            "RZ": 0, "RNZ": 0, "RP": 0, "RM": 0, "RPE": 0, "RPO": 0,
            "PUSH": 1, "POP": 1, "XTHL": 0, "SPHL": 0, "PCHL": 0, "IN": 1, "OUT": 1,
            "EI": 0, "DI": 0, "HLT": 0, "NOP": 0, "RIM": 0, "SIM": 0
        }

        if opcode in expected_operands:
            if len(operands) != expected_operands[opcode]:
                self.errors.append(
                    f"Line {ctx.start.line}: '{opcode}' expects {expected_operands[opcode]} operand(s), got {len(operands)}"
                )
        else:
            self.errors.append(f"Line {ctx.start.line}: Unknown instruction '{opcode}'")

        # If operand is a label reference, collect it
        if opcode in {"JMP", "CALL", "JC", "JNC", "JZ", "JNZ", "JP", "JM", "JPE", "JPO", "CC", "CNC", "CZ", "CNZ", "CP", "CM", "CPE", "CPO"} and operands:
            self.used_labels.append(operands[0])

        return

    def finalize(self):
        for lbl in self.used_labels:
            if lbl not in self.labels:
                self.errors.append(f"Semantic Error: Undefined label: {lbl}")

def write_dot(tree, parser, filename):
    node_id = 0
    edges = []
    nodes = []

    def recurse(node):
        nonlocal node_id
        current_id = node_id
        node_id += 1

        label = node.getText().replace('"', '\\"') if isinstance(node, TerminalNodeImpl) else parser.ruleNames[node.getRuleIndex()]
        nodes.append(f'  node{current_id} [label="{label}"];')

        for i in range(node.getChildCount()):
            child = node.getChild(i)
            child_id = recurse(child)
            edges.append(f'  node{current_id} -> node{child_id};')

        return current_id

    recurse(tree)

    with open(filename, "w") as f:
        f.write("digraph G {\n")
        f.writelines(n + "\n" for n in nodes)
        f.writelines(e + "\n" for e in edges)
        f.write("}\n")

def main():
    input_file = "input.asm"

    # Read file & normalize line endings (remove \r)
    with open(input_file, "r", encoding="utf-8") as f:
        content = f.read().replace('\r', '')
    with open(input_file, "w", encoding="utf-8") as f:
        f.write(content)

    input_stream = InputStream(content)
    lexer = Assembly8085Lexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = Assembly8085Parser(token_stream)

    # Attach custom error listener
    error_listener = CollectingErrorListener()
    parser.removeErrorListeners()
    parser.addErrorListener(error_listener)

    tree = parser.program()

    if error_listener.errors:
        print("Parsing Errors:")
        for err in error_listener.errors:
            print(err)
        print("\nFix parsing errors before semantic analysis.\n")
        return

    # Instructions
    visitor = InstructionVisitor()
    visitor.visit(tree)

    print("Instructions parsed:")
    for ins in visitor.instructions:
        print(f"{ins['opcode']} {' '.join(ins['operands'])}")
    if visitor.errors:
        print("\nInstruction Warnings:")
        for err in visitor.errors:
            print(err)

    # Semantic analysis
    semantic_visitor = SemanticAnalyzer()
    semantic_visitor.visit(tree)
    semantic_visitor.finalize()

    if semantic_visitor.errors:
        print("\nSemantic Errors:")
        for err in semantic_visitor.errors:
            print(err)
    else:
        print("\nNo semantic errors detected!")

    # Parse tree visualization
    dot_file = "parse_tree.dot"
    png_file = "parse_tree.png"
    write_dot(tree, parser, dot_file)

    try:
        subprocess.run(["dot", "-Tpng", dot_file, "-o", png_file], check=True)
        print(f"\nParse tree image generated: {png_file}")
    except FileNotFoundError:
        print("\nError: Graphviz 'dot' not found.")
    except subprocess.CalledProcessError:
        print("\nError: Failed to generate PNG from dot file.")

if __name__ == "__main__":
    main()