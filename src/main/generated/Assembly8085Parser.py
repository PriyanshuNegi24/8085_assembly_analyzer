# Generated from Assembly8085.g4 by ANTLR 4.13.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,20,76,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,1,0,5,0,24,8,0,10,0,12,0,27,
        9,0,1,0,1,0,1,1,3,1,32,8,1,1,1,3,1,35,8,1,1,1,3,1,38,8,1,1,1,1,1,
        3,1,42,8,1,1,2,1,2,1,2,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,3,3,56,
        8,3,1,4,1,4,1,5,1,5,1,5,1,5,3,5,64,8,5,1,6,1,6,1,7,1,7,1,8,1,8,1,
        9,1,9,1,10,1,10,1,10,0,0,11,0,2,4,6,8,10,12,14,16,18,20,0,2,1,0,
        5,7,1,0,8,17,74,0,25,1,0,0,0,2,41,1,0,0,0,4,43,1,0,0,0,6,55,1,0,
        0,0,8,57,1,0,0,0,10,63,1,0,0,0,12,65,1,0,0,0,14,67,1,0,0,0,16,69,
        1,0,0,0,18,71,1,0,0,0,20,73,1,0,0,0,22,24,3,2,1,0,23,22,1,0,0,0,
        24,27,1,0,0,0,25,23,1,0,0,0,25,26,1,0,0,0,26,28,1,0,0,0,27,25,1,
        0,0,0,28,29,5,0,0,1,29,1,1,0,0,0,30,32,3,4,2,0,31,30,1,0,0,0,31,
        32,1,0,0,0,32,34,1,0,0,0,33,35,3,6,3,0,34,33,1,0,0,0,34,35,1,0,0,
        0,35,37,1,0,0,0,36,38,3,20,10,0,37,36,1,0,0,0,37,38,1,0,0,0,38,39,
        1,0,0,0,39,42,5,3,0,0,40,42,5,3,0,0,41,31,1,0,0,0,41,40,1,0,0,0,
        42,3,1,0,0,0,43,44,5,19,0,0,44,45,5,1,0,0,45,5,1,0,0,0,46,56,3,8,
        4,0,47,48,3,8,4,0,48,49,3,10,5,0,49,56,1,0,0,0,50,51,3,8,4,0,51,
        52,3,10,5,0,52,53,5,2,0,0,53,54,3,10,5,0,54,56,1,0,0,0,55,46,1,0,
        0,0,55,47,1,0,0,0,55,50,1,0,0,0,56,7,1,0,0,0,57,58,7,0,0,0,58,9,
        1,0,0,0,59,64,3,12,6,0,60,64,3,14,7,0,61,64,3,16,8,0,62,64,3,18,
        9,0,63,59,1,0,0,0,63,60,1,0,0,0,63,61,1,0,0,0,63,62,1,0,0,0,64,11,
        1,0,0,0,65,66,7,1,0,0,66,13,1,0,0,0,67,68,5,17,0,0,68,15,1,0,0,0,
        69,70,5,18,0,0,70,17,1,0,0,0,71,72,5,19,0,0,72,19,1,0,0,0,73,74,
        5,4,0,0,74,21,1,0,0,0,7,25,31,34,37,41,55,63
    ]

class Assembly8085Parser ( Parser ):

    grammarFileName = "Assembly8085.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "':'", "','" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "NEWLINE", 
                      "COMMENT", "OPCODE_NOARG", "OPCODE_ONEARG", "OPCODE_TWOARG", 
                      "REG_A", "REG_B", "REG_C", "REG_D", "REG_E", "REG_H", 
                      "REG_L", "REG_PSW", "REG_SP", "MEMORY_REFERENCE", 
                      "NUMBER", "IDENTIFIER", "WS" ]

    RULE_program = 0
    RULE_line = 1
    RULE_label = 2
    RULE_instruction = 3
    RULE_opcode = 4
    RULE_operand = 5
    RULE_register = 6
    RULE_memoryReference = 7
    RULE_immediate = 8
    RULE_label_reference = 9
    RULE_comment = 10

    ruleNames =  [ "program", "line", "label", "instruction", "opcode", 
                   "operand", "register", "memoryReference", "immediate", 
                   "label_reference", "comment" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    NEWLINE=3
    COMMENT=4
    OPCODE_NOARG=5
    OPCODE_ONEARG=6
    OPCODE_TWOARG=7
    REG_A=8
    REG_B=9
    REG_C=10
    REG_D=11
    REG_E=12
    REG_H=13
    REG_L=14
    REG_PSW=15
    REG_SP=16
    MEMORY_REFERENCE=17
    NUMBER=18
    IDENTIFIER=19
    WS=20

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(Assembly8085Parser.EOF, 0)

        def line(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Assembly8085Parser.LineContext)
            else:
                return self.getTypedRuleContext(Assembly8085Parser.LineContext,i)


        def getRuleIndex(self):
            return Assembly8085Parser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = Assembly8085Parser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 25
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 524536) != 0):
                self.state = 22
                self.line()
                self.state = 27
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 28
            self.match(Assembly8085Parser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LineContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NEWLINE(self):
            return self.getToken(Assembly8085Parser.NEWLINE, 0)

        def label(self):
            return self.getTypedRuleContext(Assembly8085Parser.LabelContext,0)


        def instruction(self):
            return self.getTypedRuleContext(Assembly8085Parser.InstructionContext,0)


        def comment(self):
            return self.getTypedRuleContext(Assembly8085Parser.CommentContext,0)


        def getRuleIndex(self):
            return Assembly8085Parser.RULE_line

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLine" ):
                listener.enterLine(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLine" ):
                listener.exitLine(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLine" ):
                return visitor.visitLine(self)
            else:
                return visitor.visitChildren(self)




    def line(self):

        localctx = Assembly8085Parser.LineContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_line)
        self._la = 0 # Token type
        try:
            self.state = 41
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 31
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==19:
                    self.state = 30
                    self.label()


                self.state = 34
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & 224) != 0):
                    self.state = 33
                    self.instruction()


                self.state = 37
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==4:
                    self.state = 36
                    self.comment()


                self.state = 39
                self.match(Assembly8085Parser.NEWLINE)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 40
                self.match(Assembly8085Parser.NEWLINE)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LabelContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(Assembly8085Parser.IDENTIFIER, 0)

        def getRuleIndex(self):
            return Assembly8085Parser.RULE_label

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLabel" ):
                listener.enterLabel(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLabel" ):
                listener.exitLabel(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLabel" ):
                return visitor.visitLabel(self)
            else:
                return visitor.visitChildren(self)




    def label(self):

        localctx = Assembly8085Parser.LabelContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_label)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 43
            self.match(Assembly8085Parser.IDENTIFIER)
            self.state = 44
            self.match(Assembly8085Parser.T__0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InstructionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def opcode(self):
            return self.getTypedRuleContext(Assembly8085Parser.OpcodeContext,0)


        def operand(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Assembly8085Parser.OperandContext)
            else:
                return self.getTypedRuleContext(Assembly8085Parser.OperandContext,i)


        def getRuleIndex(self):
            return Assembly8085Parser.RULE_instruction

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInstruction" ):
                listener.enterInstruction(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInstruction" ):
                listener.exitInstruction(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInstruction" ):
                return visitor.visitInstruction(self)
            else:
                return visitor.visitChildren(self)




    def instruction(self):

        localctx = Assembly8085Parser.InstructionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_instruction)
        try:
            self.state = 55
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 46
                self.opcode()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 47
                self.opcode()
                self.state = 48
                self.operand()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 50
                self.opcode()
                self.state = 51
                self.operand()
                self.state = 52
                self.match(Assembly8085Parser.T__1)
                self.state = 53
                self.operand()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OpcodeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OPCODE_NOARG(self):
            return self.getToken(Assembly8085Parser.OPCODE_NOARG, 0)

        def OPCODE_ONEARG(self):
            return self.getToken(Assembly8085Parser.OPCODE_ONEARG, 0)

        def OPCODE_TWOARG(self):
            return self.getToken(Assembly8085Parser.OPCODE_TWOARG, 0)

        def getRuleIndex(self):
            return Assembly8085Parser.RULE_opcode

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOpcode" ):
                listener.enterOpcode(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOpcode" ):
                listener.exitOpcode(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOpcode" ):
                return visitor.visitOpcode(self)
            else:
                return visitor.visitChildren(self)




    def opcode(self):

        localctx = Assembly8085Parser.OpcodeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_opcode)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 57
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 224) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OperandContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def register(self):
            return self.getTypedRuleContext(Assembly8085Parser.RegisterContext,0)


        def memoryReference(self):
            return self.getTypedRuleContext(Assembly8085Parser.MemoryReferenceContext,0)


        def immediate(self):
            return self.getTypedRuleContext(Assembly8085Parser.ImmediateContext,0)


        def label_reference(self):
            return self.getTypedRuleContext(Assembly8085Parser.Label_referenceContext,0)


        def getRuleIndex(self):
            return Assembly8085Parser.RULE_operand

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOperand" ):
                listener.enterOperand(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOperand" ):
                listener.exitOperand(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOperand" ):
                return visitor.visitOperand(self)
            else:
                return visitor.visitChildren(self)




    def operand(self):

        localctx = Assembly8085Parser.OperandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_operand)
        try:
            self.state = 63
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 59
                self.register()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 60
                self.memoryReference()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 61
                self.immediate()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 62
                self.label_reference()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RegisterContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def REG_A(self):
            return self.getToken(Assembly8085Parser.REG_A, 0)

        def REG_B(self):
            return self.getToken(Assembly8085Parser.REG_B, 0)

        def REG_C(self):
            return self.getToken(Assembly8085Parser.REG_C, 0)

        def REG_D(self):
            return self.getToken(Assembly8085Parser.REG_D, 0)

        def REG_E(self):
            return self.getToken(Assembly8085Parser.REG_E, 0)

        def REG_H(self):
            return self.getToken(Assembly8085Parser.REG_H, 0)

        def REG_L(self):
            return self.getToken(Assembly8085Parser.REG_L, 0)

        def REG_PSW(self):
            return self.getToken(Assembly8085Parser.REG_PSW, 0)

        def REG_SP(self):
            return self.getToken(Assembly8085Parser.REG_SP, 0)

        def MEMORY_REFERENCE(self):
            return self.getToken(Assembly8085Parser.MEMORY_REFERENCE, 0)

        def getRuleIndex(self):
            return Assembly8085Parser.RULE_register

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRegister" ):
                listener.enterRegister(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRegister" ):
                listener.exitRegister(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRegister" ):
                return visitor.visitRegister(self)
            else:
                return visitor.visitChildren(self)




    def register(self):

        localctx = Assembly8085Parser.RegisterContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_register)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 65
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 261888) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MemoryReferenceContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def MEMORY_REFERENCE(self):
            return self.getToken(Assembly8085Parser.MEMORY_REFERENCE, 0)

        def getRuleIndex(self):
            return Assembly8085Parser.RULE_memoryReference

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMemoryReference" ):
                listener.enterMemoryReference(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMemoryReference" ):
                listener.exitMemoryReference(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMemoryReference" ):
                return visitor.visitMemoryReference(self)
            else:
                return visitor.visitChildren(self)




    def memoryReference(self):

        localctx = Assembly8085Parser.MemoryReferenceContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_memoryReference)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 67
            self.match(Assembly8085Parser.MEMORY_REFERENCE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ImmediateContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMBER(self):
            return self.getToken(Assembly8085Parser.NUMBER, 0)

        def getRuleIndex(self):
            return Assembly8085Parser.RULE_immediate

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterImmediate" ):
                listener.enterImmediate(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitImmediate" ):
                listener.exitImmediate(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitImmediate" ):
                return visitor.visitImmediate(self)
            else:
                return visitor.visitChildren(self)




    def immediate(self):

        localctx = Assembly8085Parser.ImmediateContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_immediate)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 69
            self.match(Assembly8085Parser.NUMBER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Label_referenceContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(Assembly8085Parser.IDENTIFIER, 0)

        def getRuleIndex(self):
            return Assembly8085Parser.RULE_label_reference

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLabel_reference" ):
                listener.enterLabel_reference(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLabel_reference" ):
                listener.exitLabel_reference(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLabel_reference" ):
                return visitor.visitLabel_reference(self)
            else:
                return visitor.visitChildren(self)




    def label_reference(self):

        localctx = Assembly8085Parser.Label_referenceContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_label_reference)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 71
            self.match(Assembly8085Parser.IDENTIFIER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CommentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COMMENT(self):
            return self.getToken(Assembly8085Parser.COMMENT, 0)

        def getRuleIndex(self):
            return Assembly8085Parser.RULE_comment

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComment" ):
                listener.enterComment(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComment" ):
                listener.exitComment(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitComment" ):
                return visitor.visitComment(self)
            else:
                return visitor.visitChildren(self)




    def comment(self):

        localctx = Assembly8085Parser.CommentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_comment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 73
            self.match(Assembly8085Parser.COMMENT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





