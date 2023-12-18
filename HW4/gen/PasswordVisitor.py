# Generated from /home/bijan/PycharmProjects/compiler-design/HW4/gen/Password.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .PasswordParser import PasswordParser
else:
    from PasswordParser import PasswordParser

# This class defines a complete generic visitor for a parse tree produced by PasswordParser.

class PasswordVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by PasswordParser#password.
    def visitPassword(self, ctx:PasswordParser.PasswordContext):
        return self.visitChildren(ctx)



del PasswordParser