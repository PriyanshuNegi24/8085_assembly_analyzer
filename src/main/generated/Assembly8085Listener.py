# Generated from Assembly8085.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .Assembly8085Parser import Assembly8085Parser
else:
    from Assembly8085Parser import Assembly8085Parser

# This class defines a complete listener for a parse tree produced by Assembly8085Parser.
class Assembly8085Listener(ParseTreeListener):

    # Enter a parse tree produced by Assembly8085Parser#program.
    def enterProgram(self, ctx:Assembly8085Parser.ProgramContext):
        pass

    # Exit a parse tree produced by Assembly8085Parser#program.
    def exitProgram(self, ctx:Assembly8085Parser.ProgramContext):
        pass


    # Enter a parse tree produced by Assembly8085Parser#line.
    def enterLine(self, ctx:Assembly8085Parser.LineContext):
        pass

    # Exit a parse tree produced by Assembly8085Parser#line.
    def exitLine(self, ctx:Assembly8085Parser.LineContext):
        pass


    # Enter a parse tree produced by Assembly8085Parser#label.
    def enterLabel(self, ctx:Assembly8085Parser.LabelContext):
        pass

    # Exit a parse tree produced by Assembly8085Parser#label.
    def exitLabel(self, ctx:Assembly8085Parser.LabelContext):
        pass


    # Enter a parse tree produced by Assembly8085Parser#instruction.
    def enterInstruction(self, ctx:Assembly8085Parser.InstructionContext):
        pass

    # Exit a parse tree produced by Assembly8085Parser#instruction.
    def exitInstruction(self, ctx:Assembly8085Parser.InstructionContext):
        pass


    # Enter a parse tree produced by Assembly8085Parser#directive.
    def enterDirective(self, ctx:Assembly8085Parser.DirectiveContext):
        pass

    # Exit a parse tree produced by Assembly8085Parser#directive.
    def exitDirective(self, ctx:Assembly8085Parser.DirectiveContext):
        pass


    # Enter a parse tree produced by Assembly8085Parser#opcode.
    def enterOpcode(self, ctx:Assembly8085Parser.OpcodeContext):
        pass

    # Exit a parse tree produced by Assembly8085Parser#opcode.
    def exitOpcode(self, ctx:Assembly8085Parser.OpcodeContext):
        pass


    # Enter a parse tree produced by Assembly8085Parser#operand.
    def enterOperand(self, ctx:Assembly8085Parser.OperandContext):
        pass

    # Exit a parse tree produced by Assembly8085Parser#operand.
    def exitOperand(self, ctx:Assembly8085Parser.OperandContext):
        pass


    # Enter a parse tree produced by Assembly8085Parser#register.
    def enterRegister(self, ctx:Assembly8085Parser.RegisterContext):
        pass

    # Exit a parse tree produced by Assembly8085Parser#register.
    def exitRegister(self, ctx:Assembly8085Parser.RegisterContext):
        pass


    # Enter a parse tree produced by Assembly8085Parser#memoryReference.
    def enterMemoryReference(self, ctx:Assembly8085Parser.MemoryReferenceContext):
        pass

    # Exit a parse tree produced by Assembly8085Parser#memoryReference.
    def exitMemoryReference(self, ctx:Assembly8085Parser.MemoryReferenceContext):
        pass


    # Enter a parse tree produced by Assembly8085Parser#immediate.
    def enterImmediate(self, ctx:Assembly8085Parser.ImmediateContext):
        pass

    # Exit a parse tree produced by Assembly8085Parser#immediate.
    def exitImmediate(self, ctx:Assembly8085Parser.ImmediateContext):
        pass


    # Enter a parse tree produced by Assembly8085Parser#label_reference.
    def enterLabel_reference(self, ctx:Assembly8085Parser.Label_referenceContext):
        pass

    # Exit a parse tree produced by Assembly8085Parser#label_reference.
    def exitLabel_reference(self, ctx:Assembly8085Parser.Label_referenceContext):
        pass


    # Enter a parse tree produced by Assembly8085Parser#expressionValue.
    def enterExpressionValue(self, ctx:Assembly8085Parser.ExpressionValueContext):
        pass

    # Exit a parse tree produced by Assembly8085Parser#expressionValue.
    def exitExpressionValue(self, ctx:Assembly8085Parser.ExpressionValueContext):
        pass


    # Enter a parse tree produced by Assembly8085Parser#operator.
    def enterOperator(self, ctx:Assembly8085Parser.OperatorContext):
        pass

    # Exit a parse tree produced by Assembly8085Parser#operator.
    def exitOperator(self, ctx:Assembly8085Parser.OperatorContext):
        pass


    # Enter a parse tree produced by Assembly8085Parser#comment.
    def enterComment(self, ctx:Assembly8085Parser.CommentContext):
        pass

    # Exit a parse tree produced by Assembly8085Parser#comment.
    def exitComment(self, ctx:Assembly8085Parser.CommentContext):
        pass



del Assembly8085Parser