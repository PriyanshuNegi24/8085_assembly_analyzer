# Generated from Assembly8085.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .Assembly8085Parser import Assembly8085Parser
else:
    from Assembly8085Parser import Assembly8085Parser

# This class defines a complete generic visitor for a parse tree produced by Assembly8085Parser.

class Assembly8085Visitor(ParseTreeVisitor):

    # Visit a parse tree produced by Assembly8085Parser#program.
    def visitProgram(self, ctx:Assembly8085Parser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Assembly8085Parser#line.
    def visitLine(self, ctx:Assembly8085Parser.LineContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Assembly8085Parser#label.
    def visitLabel(self, ctx:Assembly8085Parser.LabelContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Assembly8085Parser#instruction.
    def visitInstruction(self, ctx:Assembly8085Parser.InstructionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Assembly8085Parser#directive.
    def visitDirective(self, ctx:Assembly8085Parser.DirectiveContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Assembly8085Parser#opcode.
    def visitOpcode(self, ctx:Assembly8085Parser.OpcodeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Assembly8085Parser#operand.
    def visitOperand(self, ctx:Assembly8085Parser.OperandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Assembly8085Parser#register.
    def visitRegister(self, ctx:Assembly8085Parser.RegisterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Assembly8085Parser#memoryReference.
    def visitMemoryReference(self, ctx:Assembly8085Parser.MemoryReferenceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Assembly8085Parser#immediate.
    def visitImmediate(self, ctx:Assembly8085Parser.ImmediateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Assembly8085Parser#label_reference.
    def visitLabel_reference(self, ctx:Assembly8085Parser.Label_referenceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Assembly8085Parser#expressionValue.
    def visitExpressionValue(self, ctx:Assembly8085Parser.ExpressionValueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Assembly8085Parser#operator.
    def visitOperator(self, ctx:Assembly8085Parser.OperatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Assembly8085Parser#comment.
    def visitComment(self, ctx:Assembly8085Parser.CommentContext):
        return self.visitChildren(ctx)



del Assembly8085Parser