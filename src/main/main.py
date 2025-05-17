
import sys
from antlr4 import *
from generated.Assembly8085Lexer import Assembly8085Lexer
from generated.Assembly8085Parser import Assembly8085Parser
from generated.Assembly8085Listener import Assembly8085Listener

class MyListener(Assembly8085Listener):
    def enterInstruction(self, ctx):
        print("Instruction:", ctx.getText())  # customize based on your grammar

def main():
    if len(sys.argv) != 2:
        print("Usage: python main.py <input_file.asm>")
        return

    input_file = sys.argv[1]
    input_stream = FileStream(input_file)
    
    lexer = Assembly8085Lexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = Assembly8085Parser(token_stream)
    tree = parser.program()  # Replace 'program' with your grammar's start rule

    listener = MyListener()
    walker = ParseTreeWalker()
    walker.walk(listener, tree)

if __name__ == "__main__":
    main()
