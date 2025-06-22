import sys
sys.path.insert(0, "./generated")

from antlr4 import *
from generated.Assembly8085Lexer import Assembly8085Lexer
from generated.Assembly8085Parser import Assembly8085Parser

from antlr4.tree.Tree import TerminalNodeImpl

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

    # 👉 THIS LINE IS MISSING
    recurse(tree)

    with open(filename, "w") as f:
        f.write("digraph G {\n")
        for n in nodes:
            f.write(n + "\n")
        for e in edges:
            f.write(e + "\n")
        f.write("}\n")

def main():
    input_stream = FileStream("input.asm")  # Make sure input.asm exists here
    lexer = Assembly8085Lexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = Assembly8085Parser(stream)
    tree = parser.program()
    # Optional: print tokens
    stream.fill()
    for token in stream.tokens:
        print(token)

    print(tree.toStringTree(recog=parser))

    write_dot(tree, parser, "parse_tree.dot")
    print("DOT file 'parse_tree.dot' generated.")

if __name__ == "__main__":
    main()
