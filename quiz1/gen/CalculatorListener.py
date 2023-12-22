# Generated from /home/bijan/PycharmProjects/compiler-design/quiz1/gen/Calculator.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .CalculatorParser import CalculatorParser
else:
    from CalculatorParser import CalculatorParser

# This class defines a complete listener for a parse tree produced by CalculatorParser.
class CalculatorListener(ParseTreeListener):

    # Enter a parse tree produced by CalculatorParser#expression.
    def enterExpression(self, ctx:CalculatorParser.ExpressionContext):
        pass

    # Exit a parse tree produced by CalculatorParser#expression.
    def exitExpression(self, ctx:CalculatorParser.ExpressionContext):
        pass


    # Enter a parse tree produced by CalculatorParser#additiveExpression.
    def enterAdditiveExpression(self, ctx:CalculatorParser.AdditiveExpressionContext):
        pass

    # Exit a parse tree produced by CalculatorParser#additiveExpression.
    def exitAdditiveExpression(self, ctx:CalculatorParser.AdditiveExpressionContext):
        pass


    # Enter a parse tree produced by CalculatorParser#multiplicativeExpression.
    def enterMultiplicativeExpression(self, ctx:CalculatorParser.MultiplicativeExpressionContext):
        pass

    # Exit a parse tree produced by CalculatorParser#multiplicativeExpression.
    def exitMultiplicativeExpression(self, ctx:CalculatorParser.MultiplicativeExpressionContext):
        pass


    # Enter a parse tree produced by CalculatorParser#powerExpression.
    def enterPowerExpression(self, ctx:CalculatorParser.PowerExpressionContext):
        pass

    # Exit a parse tree produced by CalculatorParser#powerExpression.
    def exitPowerExpression(self, ctx:CalculatorParser.PowerExpressionContext):
        pass


    # Enter a parse tree produced by CalculatorParser#primaryExpression.
    def enterPrimaryExpression(self, ctx:CalculatorParser.PrimaryExpressionContext):
        pass

    # Exit a parse tree produced by CalculatorParser#primaryExpression.
    def exitPrimaryExpression(self, ctx:CalculatorParser.PrimaryExpressionContext):
        pass



del CalculatorParser