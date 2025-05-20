import sys
import os
from antlr4 import *

# Add the 'generated' folder to Python's import path
current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(current_dir, "generated"))

from Assembly8085Lexer import Assembly8085Lexer
from Assembly8085Parser import Assembly8085Parser
from analyze import AnalyzerVisitor  # Assuming analyze.py defines AnalyzerVisitor

def main():
    input_stream = FileStream("input.asm")
    lexer = Assembly8085Lexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = Assembly8085Parser(stream)
    tree = parser.program()

    visitor = AnalyzerVisitor()
    visitor.visit(tree)

if __name__ == '__main__':
    main()
