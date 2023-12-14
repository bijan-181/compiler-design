# Generated from /home/bijan/PycharmProjects/compiler-design/HW3/gen/ExtractInfo.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .ExtractInfoParser import ExtractInfoParser
else:
    from ExtractInfoParser import ExtractInfoParser

# This class defines a complete generic visitor for a parse tree produced by ExtractInfoParser.

class ExtractInfoVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by ExtractInfoParser#text.
    def visitText(self, ctx:ExtractInfoParser.TextContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExtractInfoParser#email.
    def visitEmail(self, ctx:ExtractInfoParser.EmailContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExtractInfoParser#melli_number.
    def visitMelli_number(self, ctx:ExtractInfoParser.Melli_numberContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExtractInfoParser#phonenumber.
    def visitPhonenumber(self, ctx:ExtractInfoParser.PhonenumberContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExtractInfoParser#float.
    def visitFloat(self, ctx:ExtractInfoParser.FloatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExtractInfoParser#url.
    def visitUrl(self, ctx:ExtractInfoParser.UrlContext):
        return self.visitChildren(ctx)



del ExtractInfoParser