# Generated from src/main/antlr4/Assembly8085.g4 by ANTLR 4.13.1
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
        4,1,38,132,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        1,0,5,0,30,8,0,10,0,12,0,33,9,0,1,0,1,0,1,1,1,1,3,1,39,8,1,1,1,3,
        1,42,8,1,1,1,1,1,1,1,1,1,3,1,48,8,1,1,1,1,1,1,1,1,1,3,1,54,8,1,1,
        1,1,1,1,1,3,1,59,8,1,1,2,1,2,1,2,1,3,1,3,1,3,1,3,3,3,68,8,3,3,3,
        70,8,3,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,5,4,80,8,4,10,4,12,4,83,9,
        4,1,4,1,4,3,4,87,8,4,1,5,1,5,1,6,1,6,1,6,1,6,3,6,95,8,6,1,7,1,7,
        1,8,1,8,1,9,3,9,102,8,9,1,9,1,9,1,10,1,10,1,11,1,11,1,11,1,11,1,
        11,1,11,1,11,1,11,1,11,3,11,117,8,11,1,11,1,11,1,11,1,11,5,11,123,
        8,11,10,11,12,11,126,9,11,1,12,1,12,1,13,1,13,1,13,0,1,22,14,0,2,
        4,6,8,10,12,14,16,18,20,22,24,26,0,3,2,0,21,23,37,37,1,0,24,33,1,
        0,6,14,140,0,31,1,0,0,0,2,58,1,0,0,0,4,60,1,0,0,0,6,63,1,0,0,0,8,
        86,1,0,0,0,10,88,1,0,0,0,12,94,1,0,0,0,14,96,1,0,0,0,16,98,1,0,0,
        0,18,101,1,0,0,0,20,105,1,0,0,0,22,116,1,0,0,0,24,127,1,0,0,0,26,
        129,1,0,0,0,28,30,3,2,1,0,29,28,1,0,0,0,30,33,1,0,0,0,31,29,1,0,
        0,0,31,32,1,0,0,0,32,34,1,0,0,0,33,31,1,0,0,0,34,35,5,0,0,1,35,1,
        1,0,0,0,36,38,3,4,2,0,37,39,3,6,3,0,38,37,1,0,0,0,38,39,1,0,0,0,
        39,41,1,0,0,0,40,42,3,26,13,0,41,40,1,0,0,0,41,42,1,0,0,0,42,43,
        1,0,0,0,43,44,5,15,0,0,44,59,1,0,0,0,45,47,3,6,3,0,46,48,3,26,13,
        0,47,46,1,0,0,0,47,48,1,0,0,0,48,49,1,0,0,0,49,50,5,15,0,0,50,59,
        1,0,0,0,51,53,3,8,4,0,52,54,3,26,13,0,53,52,1,0,0,0,53,54,1,0,0,
        0,54,55,1,0,0,0,55,56,5,15,0,0,56,59,1,0,0,0,57,59,5,15,0,0,58,36,
        1,0,0,0,58,45,1,0,0,0,58,51,1,0,0,0,58,57,1,0,0,0,59,3,1,0,0,0,60,
        61,5,37,0,0,61,62,5,1,0,0,62,5,1,0,0,0,63,69,3,10,5,0,64,67,3,12,
        6,0,65,66,5,2,0,0,66,68,3,12,6,0,67,65,1,0,0,0,67,68,1,0,0,0,68,
        70,1,0,0,0,69,64,1,0,0,0,69,70,1,0,0,0,70,7,1,0,0,0,71,72,5,17,0,
        0,72,87,3,22,11,0,73,74,5,18,0,0,74,87,3,22,11,0,75,76,5,19,0,0,
        76,81,3,22,11,0,77,78,5,2,0,0,78,80,3,22,11,0,79,77,1,0,0,0,80,83,
        1,0,0,0,81,79,1,0,0,0,81,82,1,0,0,0,82,87,1,0,0,0,83,81,1,0,0,0,
        84,85,5,20,0,0,85,87,3,22,11,0,86,71,1,0,0,0,86,73,1,0,0,0,86,75,
        1,0,0,0,86,84,1,0,0,0,87,9,1,0,0,0,88,89,7,0,0,0,89,11,1,0,0,0,90,
        95,3,14,7,0,91,95,3,16,8,0,92,95,3,18,9,0,93,95,3,20,10,0,94,90,
        1,0,0,0,94,91,1,0,0,0,94,92,1,0,0,0,94,93,1,0,0,0,95,13,1,0,0,0,
        96,97,7,1,0,0,97,15,1,0,0,0,98,99,5,33,0,0,99,17,1,0,0,0,100,102,
        5,3,0,0,101,100,1,0,0,0,101,102,1,0,0,0,102,103,1,0,0,0,103,104,
        3,22,11,0,104,19,1,0,0,0,105,106,5,37,0,0,106,21,1,0,0,0,107,108,
        6,11,-1,0,108,117,5,34,0,0,109,117,5,35,0,0,110,117,5,36,0,0,111,
        117,5,37,0,0,112,113,5,4,0,0,113,114,3,22,11,0,114,115,5,5,0,0,115,
        117,1,0,0,0,116,107,1,0,0,0,116,109,1,0,0,0,116,110,1,0,0,0,116,
        111,1,0,0,0,116,112,1,0,0,0,117,124,1,0,0,0,118,119,10,1,0,0,119,
        120,3,24,12,0,120,121,3,22,11,2,121,123,1,0,0,0,122,118,1,0,0,0,
        123,126,1,0,0,0,124,122,1,0,0,0,124,125,1,0,0,0,125,23,1,0,0,0,126,
        124,1,0,0,0,127,128,7,2,0,0,128,25,1,0,0,0,129,130,5,16,0,0,130,
        27,1,0,0,0,14,31,38,41,47,53,58,67,69,81,86,94,101,116,124
    ]

class Assembly8085Parser ( Parser ):

    grammarFileName = "Assembly8085.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "':'", "','", "'#'", "'('", "')'", "'+'", 
                     "'-'", "'*'", "'/'", "'&'", "'|'", "'^'", "'<<'", "'>>'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "NEWLINE", 
                      "COMMENT", "DIRECTIVE_ORG", "DIRECTIVE_EQU", "DIRECTIVE_DB", 
                      "DIRECTIVE_DS", "OPCODE_NOARG", "OPCODE_ONEARG", "OPCODE_TWOARG", 
                      "REG_A", "REG_B", "REG_C", "REG_D", "REG_E", "REG_H", 
                      "REG_L", "REG_PSW", "REG_SP", "MEMORY_REFERENCE", 
                      "NUMBER", "CHARACTER", "STRING", "IDENTIFIER", "WS" ]

    RULE_program = 0
    RULE_line = 1
    RULE_label = 2
    RULE_instruction = 3
    RULE_directive = 4
    RULE_opcode = 5
    RULE_operand = 6
    RULE_register = 7
    RULE_memoryReference = 8
    RULE_immediate = 9
    RULE_label_reference = 10
    RULE_expressionValue = 11
    RULE_operator = 12
    RULE_comment = 13

    ruleNames =  [ "program", "line", "label", "instruction", "directive", 
                   "opcode", "operand", "register", "memoryReference", "immediate", 
                   "label_reference", "expressionValue", "operator", "comment" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    T__12=13
    T__13=14
    NEWLINE=15
    COMMENT=16
    DIRECTIVE_ORG=17
    DIRECTIVE_EQU=18
    DIRECTIVE_DB=19
    DIRECTIVE_DS=20
    OPCODE_NOARG=21
    OPCODE_ONEARG=22
    OPCODE_TWOARG=23
    REG_A=24
    REG_B=25
    REG_C=26
    REG_D=27
    REG_E=28
    REG_H=29
    REG_L=30
    REG_PSW=31
    REG_SP=32
    MEMORY_REFERENCE=33
    NUMBER=34
    CHARACTER=35
    STRING=36
    IDENTIFIER=37
    WS=38

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
            self.state = 31
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 137455632384) != 0):
                self.state = 28
                self.line()
                self.state = 33
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 34
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

        def label(self):
            return self.getTypedRuleContext(Assembly8085Parser.LabelContext,0)


        def NEWLINE(self):
            return self.getToken(Assembly8085Parser.NEWLINE, 0)

        def instruction(self):
            return self.getTypedRuleContext(Assembly8085Parser.InstructionContext,0)


        def comment(self):
            return self.getTypedRuleContext(Assembly8085Parser.CommentContext,0)


        def directive(self):
            return self.getTypedRuleContext(Assembly8085Parser.DirectiveContext,0)


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
            self.state = 58
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 36
                self.label()
                self.state = 38
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & 137453633536) != 0):
                    self.state = 37
                    self.instruction()


                self.state = 41
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==16:
                    self.state = 40
                    self.comment()


                self.state = 43
                self.match(Assembly8085Parser.NEWLINE)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 45
                self.instruction()
                self.state = 47
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==16:
                    self.state = 46
                    self.comment()


                self.state = 49
                self.match(Assembly8085Parser.NEWLINE)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 51
                self.directive()
                self.state = 53
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==16:
                    self.state = 52
                    self.comment()


                self.state = 55
                self.match(Assembly8085Parser.NEWLINE)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 57
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
            self.state = 60
            self.match(Assembly8085Parser.IDENTIFIER)
            self.state = 61
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
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 63
            self.opcode()
            self.state = 69
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 274861129752) != 0):
                self.state = 64
                self.operand()
                self.state = 67
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==2:
                    self.state = 65
                    self.match(Assembly8085Parser.T__1)
                    self.state = 66
                    self.operand()




        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DirectiveContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DIRECTIVE_ORG(self):
            return self.getToken(Assembly8085Parser.DIRECTIVE_ORG, 0)

        def expressionValue(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Assembly8085Parser.ExpressionValueContext)
            else:
                return self.getTypedRuleContext(Assembly8085Parser.ExpressionValueContext,i)


        def DIRECTIVE_EQU(self):
            return self.getToken(Assembly8085Parser.DIRECTIVE_EQU, 0)

        def DIRECTIVE_DB(self):
            return self.getToken(Assembly8085Parser.DIRECTIVE_DB, 0)

        def DIRECTIVE_DS(self):
            return self.getToken(Assembly8085Parser.DIRECTIVE_DS, 0)

        def getRuleIndex(self):
            return Assembly8085Parser.RULE_directive

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDirective" ):
                listener.enterDirective(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDirective" ):
                listener.exitDirective(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDirective" ):
                return visitor.visitDirective(self)
            else:
                return visitor.visitChildren(self)




    def directive(self):

        localctx = Assembly8085Parser.DirectiveContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_directive)
        self._la = 0 # Token type
        try:
            self.state = 86
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [17]:
                self.enterOuterAlt(localctx, 1)
                self.state = 71
                self.match(Assembly8085Parser.DIRECTIVE_ORG)
                self.state = 72
                self.expressionValue(0)
                pass
            elif token in [18]:
                self.enterOuterAlt(localctx, 2)
                self.state = 73
                self.match(Assembly8085Parser.DIRECTIVE_EQU)
                self.state = 74
                self.expressionValue(0)
                pass
            elif token in [19]:
                self.enterOuterAlt(localctx, 3)
                self.state = 75
                self.match(Assembly8085Parser.DIRECTIVE_DB)
                self.state = 76
                self.expressionValue(0)
                self.state = 81
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==2:
                    self.state = 77
                    self.match(Assembly8085Parser.T__1)
                    self.state = 78
                    self.expressionValue(0)
                    self.state = 83
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass
            elif token in [20]:
                self.enterOuterAlt(localctx, 4)
                self.state = 84
                self.match(Assembly8085Parser.DIRECTIVE_DS)
                self.state = 85
                self.expressionValue(0)
                pass
            else:
                raise NoViableAltException(self)

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

        def IDENTIFIER(self):
            return self.getToken(Assembly8085Parser.IDENTIFIER, 0)

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
        self.enterRule(localctx, 10, self.RULE_opcode)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 88
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 137453633536) != 0)):
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
        self.enterRule(localctx, 12, self.RULE_operand)
        try:
            self.state = 94
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 90
                self.register()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 91
                self.memoryReference()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 92
                self.immediate()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 93
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
        self.enterRule(localctx, 14, self.RULE_register)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 96
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 17163091968) != 0)):
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
        self.enterRule(localctx, 16, self.RULE_memoryReference)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 98
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

        def expressionValue(self):
            return self.getTypedRuleContext(Assembly8085Parser.ExpressionValueContext,0)


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
        self.enterRule(localctx, 18, self.RULE_immediate)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 101
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==3:
                self.state = 100
                self.match(Assembly8085Parser.T__2)


            self.state = 103
            self.expressionValue(0)
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
        self.enterRule(localctx, 20, self.RULE_label_reference)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 105
            self.match(Assembly8085Parser.IDENTIFIER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionValueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMBER(self):
            return self.getToken(Assembly8085Parser.NUMBER, 0)

        def CHARACTER(self):
            return self.getToken(Assembly8085Parser.CHARACTER, 0)

        def STRING(self):
            return self.getToken(Assembly8085Parser.STRING, 0)

        def IDENTIFIER(self):
            return self.getToken(Assembly8085Parser.IDENTIFIER, 0)

        def expressionValue(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Assembly8085Parser.ExpressionValueContext)
            else:
                return self.getTypedRuleContext(Assembly8085Parser.ExpressionValueContext,i)


        def operator(self):
            return self.getTypedRuleContext(Assembly8085Parser.OperatorContext,0)


        def getRuleIndex(self):
            return Assembly8085Parser.RULE_expressionValue

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpressionValue" ):
                listener.enterExpressionValue(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpressionValue" ):
                listener.exitExpressionValue(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpressionValue" ):
                return visitor.visitExpressionValue(self)
            else:
                return visitor.visitChildren(self)



    def expressionValue(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = Assembly8085Parser.ExpressionValueContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 22
        self.enterRecursionRule(localctx, 22, self.RULE_expressionValue, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 116
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [34]:
                self.state = 108
                self.match(Assembly8085Parser.NUMBER)
                pass
            elif token in [35]:
                self.state = 109
                self.match(Assembly8085Parser.CHARACTER)
                pass
            elif token in [36]:
                self.state = 110
                self.match(Assembly8085Parser.STRING)
                pass
            elif token in [37]:
                self.state = 111
                self.match(Assembly8085Parser.IDENTIFIER)
                pass
            elif token in [4]:
                self.state = 112
                self.match(Assembly8085Parser.T__3)
                self.state = 113
                self.expressionValue(0)
                self.state = 114
                self.match(Assembly8085Parser.T__4)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 124
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,13,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = Assembly8085Parser.ExpressionValueContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expressionValue)
                    self.state = 118
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 119
                    self.operator()
                    self.state = 120
                    self.expressionValue(2) 
                self.state = 126
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,13,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class OperatorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return Assembly8085Parser.RULE_operator

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOperator" ):
                listener.enterOperator(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOperator" ):
                listener.exitOperator(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOperator" ):
                return visitor.visitOperator(self)
            else:
                return visitor.visitChildren(self)




    def operator(self):

        localctx = Assembly8085Parser.OperatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_operator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 127
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 32704) != 0)):
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
        self.enterRule(localctx, 26, self.RULE_comment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 129
            self.match(Assembly8085Parser.COMMENT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[11] = self.expressionValue_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expressionValue_sempred(self, localctx:ExpressionValueContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 1)
         




