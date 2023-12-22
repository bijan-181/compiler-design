# Generated from /home/bijan/PycharmProjects/compiler-design/quiz1/gen/Calculator.g4 by ANTLR 4.13.1
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
        4,1,9,41,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,1,0,1,0,1,1,1,1,
        1,1,5,1,16,8,1,10,1,12,1,19,9,1,1,2,1,2,1,2,5,2,24,8,2,10,2,12,2,
        27,9,2,1,3,1,3,1,3,3,3,32,8,3,1,4,1,4,1,4,1,4,1,4,3,4,39,8,4,1,4,
        0,0,5,0,2,4,6,8,0,2,1,0,2,3,1,0,4,5,39,0,10,1,0,0,0,2,12,1,0,0,0,
        4,20,1,0,0,0,6,28,1,0,0,0,8,38,1,0,0,0,10,11,3,2,1,0,11,1,1,0,0,
        0,12,17,3,4,2,0,13,14,7,0,0,0,14,16,3,4,2,0,15,13,1,0,0,0,16,19,
        1,0,0,0,17,15,1,0,0,0,17,18,1,0,0,0,18,3,1,0,0,0,19,17,1,0,0,0,20,
        25,3,6,3,0,21,22,7,1,0,0,22,24,3,6,3,0,23,21,1,0,0,0,24,27,1,0,0,
        0,25,23,1,0,0,0,25,26,1,0,0,0,26,5,1,0,0,0,27,25,1,0,0,0,28,31,3,
        8,4,0,29,30,5,6,0,0,30,32,3,6,3,0,31,29,1,0,0,0,31,32,1,0,0,0,32,
        7,1,0,0,0,33,39,5,1,0,0,34,35,5,7,0,0,35,36,3,0,0,0,36,37,5,8,0,
        0,37,39,1,0,0,0,38,33,1,0,0,0,38,34,1,0,0,0,39,9,1,0,0,0,4,17,25,
        31,38
    ]

class CalculatorParser ( Parser ):

    grammarFileName = "Calculator.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "'+'", "'-'", "'*'", "'/'", 
                     "'^'", "'('", "')'" ]

    symbolicNames = [ "<INVALID>", "NUMBER", "PLUS", "MINUS", "MULTIPLY", 
                      "DIVIDE", "EXPONENTIATION", "LPAREN", "RPAREN", "WS" ]

    RULE_expression = 0
    RULE_additiveExpression = 1
    RULE_multiplicativeExpression = 2
    RULE_powerExpression = 3
    RULE_primaryExpression = 4

    ruleNames =  [ "expression", "additiveExpression", "multiplicativeExpression", 
                   "powerExpression", "primaryExpression" ]

    EOF = Token.EOF
    NUMBER=1
    PLUS=2
    MINUS=3
    MULTIPLY=4
    DIVIDE=5
    EXPONENTIATION=6
    LPAREN=7
    RPAREN=8
    WS=9

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def additiveExpression(self):
            return self.getTypedRuleContext(CalculatorParser.AdditiveExpressionContext,0)


        def getRuleIndex(self):
            return CalculatorParser.RULE_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpression" ):
                listener.enterExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpression" ):
                listener.exitExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression" ):
                return visitor.visitExpression(self)
            else:
                return visitor.visitChildren(self)




    def expression(self):

        localctx = CalculatorParser.ExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 10
            self.additiveExpression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AdditiveExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def multiplicativeExpression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CalculatorParser.MultiplicativeExpressionContext)
            else:
                return self.getTypedRuleContext(CalculatorParser.MultiplicativeExpressionContext,i)


        def PLUS(self, i:int=None):
            if i is None:
                return self.getTokens(CalculatorParser.PLUS)
            else:
                return self.getToken(CalculatorParser.PLUS, i)

        def MINUS(self, i:int=None):
            if i is None:
                return self.getTokens(CalculatorParser.MINUS)
            else:
                return self.getToken(CalculatorParser.MINUS, i)

        def getRuleIndex(self):
            return CalculatorParser.RULE_additiveExpression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAdditiveExpression" ):
                listener.enterAdditiveExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAdditiveExpression" ):
                listener.exitAdditiveExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAdditiveExpression" ):
                return visitor.visitAdditiveExpression(self)
            else:
                return visitor.visitChildren(self)




    def additiveExpression(self):

        localctx = CalculatorParser.AdditiveExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_additiveExpression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 12
            self.multiplicativeExpression()
            self.state = 17
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==2 or _la==3:
                self.state = 13
                _la = self._input.LA(1)
                if not(_la==2 or _la==3):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 14
                self.multiplicativeExpression()
                self.state = 19
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MultiplicativeExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def powerExpression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CalculatorParser.PowerExpressionContext)
            else:
                return self.getTypedRuleContext(CalculatorParser.PowerExpressionContext,i)


        def MULTIPLY(self, i:int=None):
            if i is None:
                return self.getTokens(CalculatorParser.MULTIPLY)
            else:
                return self.getToken(CalculatorParser.MULTIPLY, i)

        def DIVIDE(self, i:int=None):
            if i is None:
                return self.getTokens(CalculatorParser.DIVIDE)
            else:
                return self.getToken(CalculatorParser.DIVIDE, i)

        def getRuleIndex(self):
            return CalculatorParser.RULE_multiplicativeExpression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMultiplicativeExpression" ):
                listener.enterMultiplicativeExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMultiplicativeExpression" ):
                listener.exitMultiplicativeExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMultiplicativeExpression" ):
                return visitor.visitMultiplicativeExpression(self)
            else:
                return visitor.visitChildren(self)




    def multiplicativeExpression(self):

        localctx = CalculatorParser.MultiplicativeExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_multiplicativeExpression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 20
            self.powerExpression()
            self.state = 25
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==4 or _la==5:
                self.state = 21
                _la = self._input.LA(1)
                if not(_la==4 or _la==5):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 22
                self.powerExpression()
                self.state = 27
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PowerExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def primaryExpression(self):
            return self.getTypedRuleContext(CalculatorParser.PrimaryExpressionContext,0)


        def EXPONENTIATION(self):
            return self.getToken(CalculatorParser.EXPONENTIATION, 0)

        def powerExpression(self):
            return self.getTypedRuleContext(CalculatorParser.PowerExpressionContext,0)


        def getRuleIndex(self):
            return CalculatorParser.RULE_powerExpression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPowerExpression" ):
                listener.enterPowerExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPowerExpression" ):
                listener.exitPowerExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPowerExpression" ):
                return visitor.visitPowerExpression(self)
            else:
                return visitor.visitChildren(self)




    def powerExpression(self):

        localctx = CalculatorParser.PowerExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_powerExpression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 28
            self.primaryExpression()
            self.state = 31
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==6:
                self.state = 29
                self.match(CalculatorParser.EXPONENTIATION)
                self.state = 30
                self.powerExpression()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PrimaryExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMBER(self):
            return self.getToken(CalculatorParser.NUMBER, 0)

        def LPAREN(self):
            return self.getToken(CalculatorParser.LPAREN, 0)

        def expression(self):
            return self.getTypedRuleContext(CalculatorParser.ExpressionContext,0)


        def RPAREN(self):
            return self.getToken(CalculatorParser.RPAREN, 0)

        def getRuleIndex(self):
            return CalculatorParser.RULE_primaryExpression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrimaryExpression" ):
                listener.enterPrimaryExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrimaryExpression" ):
                listener.exitPrimaryExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrimaryExpression" ):
                return visitor.visitPrimaryExpression(self)
            else:
                return visitor.visitChildren(self)




    def primaryExpression(self):

        localctx = CalculatorParser.PrimaryExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_primaryExpression)
        try:
            self.state = 38
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1]:
                self.enterOuterAlt(localctx, 1)
                self.state = 33
                self.match(CalculatorParser.NUMBER)
                pass
            elif token in [7]:
                self.enterOuterAlt(localctx, 2)
                self.state = 34
                self.match(CalculatorParser.LPAREN)
                self.state = 35
                self.expression()
                self.state = 36
                self.match(CalculatorParser.RPAREN)
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





