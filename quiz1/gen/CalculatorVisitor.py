# Generated from /home/bijan/PycharmProjects/compiler-design/quiz1/gen/Calculator.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .CalculatorParser import CalculatorParser
else:
    from CalculatorParser import CalculatorParser

# This class defines a complete generic visitor for a parse tree produced by CalculatorParser.

class CalculatorVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by CalculatorParser#expression.
    def visitExpression(self, ctx:CalculatorParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalculatorParser#additiveExpression.
    def visitAdditiveExpression(self, ctx:CalculatorParser.AdditiveExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalculatorParser#multiplicativeExpression.
    def visitMultiplicativeExpression(self, ctx:CalculatorParser.MultiplicativeExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalculatorParser#powerExpression.
    def visitPowerExpression(self, ctx:CalculatorParser.PowerExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalculatorParser#primaryExpression.
    def visitPrimaryExpression(self, ctx:CalculatorParser.PrimaryExpressionContext):
        return self.visitChildren(ctx)



del CalculatorParser