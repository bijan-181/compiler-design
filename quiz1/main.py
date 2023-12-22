from antlr4 import *
from gen.CalculatorLexer import CalculatorLexer
from gen.CalculatorParser import CalculatorParser
from gen.CalculatorVisitor import CalculatorVisitor

class CalculatorEvalVisitor(CalculatorVisitor):
    def visitExpression(self, ctx):
        return self.visit(ctx.additiveExpression())

    def visitAdditiveExpression(self, ctx):
        left = self.visit(ctx.multiplicativeExpression(0))
        for i in range(1, len(ctx.multiplicativeExpression())):
            op = ctx.getChild(2 * i - 1).getText()
            right = self.visit(ctx.multiplicativeExpression(i))
            if op == '+':
                left += right
            elif op == '-':
                left -= right
        return left

    def visitMultiplicativeExpression(self, ctx):
        left = self.visit(ctx.powerExpression(0))
        for i in range(1, len(ctx.powerExpression())):
            op = ctx.getChild(2 * i - 1).getText()
            right = self.visit(ctx.powerExpression(i))
            if op == '*':
                left *= right
            elif op == '/':
                left /= right
        return left

    def visitPowerExpression(self, ctx):
        left = self.visit(ctx.primaryExpression())
        if ctx.EXPONENTIATION():
            right = self.visit(ctx.powerExpression())
            return left ** right
        return left

    def visitPrimaryExpression(self, ctx):
        if ctx.NUMBER():
            return float(ctx.NUMBER().getText())
        elif ctx.LPAREN():
            return self.visit(ctx.expression())
        else:
            return 0  # Default value, you may want to handle this differently

def main():
    input_expr = "(5-2)*2^2"
    input_stream = InputStream(input_expr)
    lexer = CalculatorLexer(input_stream)
    tokens = CommonTokenStream(lexer)
    parser = CalculatorParser(tokens)
    tree = parser.expression()

    visitor = CalculatorEvalVisitor()
    result = visitor.visit(tree)

    print(f"Result of {input_expr} = {result}")

if __name__ == '__main__':
    main()
