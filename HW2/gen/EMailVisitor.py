# Generated from /home/bijan/PycharmProjects/compiler-design/HW2/gen/EMail.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .EMailParser import EMailParser
else:
    from EMailParser import EMailParser

# This class defines a complete generic visitor for a parse tree produced by EMailParser.

class EMailVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by EMailParser#start.
    def visitStart(self, ctx:EMailParser.StartContext):
        return self.visitChildren(ctx)



del EMailParser