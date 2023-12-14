# Generated from /home/bijan/PycharmProjects/compiler-design/HW3/gen/ExtractInfo.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .ExtractInfoParser import ExtractInfoParser
else:
    from ExtractInfoParser import ExtractInfoParser

# This class defines a complete listener for a parse tree produced by ExtractInfoParser.
class ExtractInfoListener(ParseTreeListener):

    # Enter a parse tree produced by ExtractInfoParser#text.
    def enterText(self, ctx:ExtractInfoParser.TextContext):
        pass

    # Exit a parse tree produced by ExtractInfoParser#text.
    def exitText(self, ctx:ExtractInfoParser.TextContext):
        pass


    # Enter a parse tree produced by ExtractInfoParser#email.
    def enterEmail(self, ctx:ExtractInfoParser.EmailContext):
        pass

    # Exit a parse tree produced by ExtractInfoParser#email.
    def exitEmail(self, ctx:ExtractInfoParser.EmailContext):
        pass


    # Enter a parse tree produced by ExtractInfoParser#melli_number.
    def enterMelli_number(self, ctx:ExtractInfoParser.Melli_numberContext):
        pass

    # Exit a parse tree produced by ExtractInfoParser#melli_number.
    def exitMelli_number(self, ctx:ExtractInfoParser.Melli_numberContext):
        pass


    # Enter a parse tree produced by ExtractInfoParser#phonenumber.
    def enterPhonenumber(self, ctx:ExtractInfoParser.PhonenumberContext):
        pass

    # Exit a parse tree produced by ExtractInfoParser#phonenumber.
    def exitPhonenumber(self, ctx:ExtractInfoParser.PhonenumberContext):
        pass


    # Enter a parse tree produced by ExtractInfoParser#float.
    def enterFloat(self, ctx:ExtractInfoParser.FloatContext):
        pass

    # Exit a parse tree produced by ExtractInfoParser#float.
    def exitFloat(self, ctx:ExtractInfoParser.FloatContext):
        pass


    # Enter a parse tree produced by ExtractInfoParser#url.
    def enterUrl(self, ctx:ExtractInfoParser.UrlContext):
        pass

    # Exit a parse tree produced by ExtractInfoParser#url.
    def exitUrl(self, ctx:ExtractInfoParser.UrlContext):
        pass



del ExtractInfoParser