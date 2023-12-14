# Generated from /home/bijan/PycharmProjects/compiler-design/HW3/gen/ExtractInfo.g4 by ANTLR 4.13.1
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
        4,1,8,40,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,6,
        1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,5,0,23,8,0,10,0,12,0,26,9,0,1,1,
        1,1,1,2,1,2,1,3,1,3,1,4,1,4,1,5,1,5,1,6,1,6,1,6,0,0,7,0,2,4,6,8,
        10,12,0,0,40,0,24,1,0,0,0,2,27,1,0,0,0,4,29,1,0,0,0,6,31,1,0,0,0,
        8,33,1,0,0,0,10,35,1,0,0,0,12,37,1,0,0,0,14,23,3,2,1,0,15,23,3,8,
        4,0,16,23,3,4,2,0,17,23,3,6,3,0,18,23,3,10,5,0,19,23,3,12,6,0,20,
        23,5,7,0,0,21,23,5,8,0,0,22,14,1,0,0,0,22,15,1,0,0,0,22,16,1,0,0,
        0,22,17,1,0,0,0,22,18,1,0,0,0,22,19,1,0,0,0,22,20,1,0,0,0,22,21,
        1,0,0,0,23,26,1,0,0,0,24,22,1,0,0,0,24,25,1,0,0,0,25,1,1,0,0,0,26,
        24,1,0,0,0,27,28,5,2,0,0,28,3,1,0,0,0,29,30,5,3,0,0,30,5,1,0,0,0,
        31,32,5,4,0,0,32,7,1,0,0,0,33,34,5,5,0,0,34,9,1,0,0,0,35,36,5,1,
        0,0,36,11,1,0,0,0,37,38,5,6,0,0,38,13,1,0,0,0,2,22,24
    ]

class ExtractInfoParser ( Parser ):

    grammarFileName = "ExtractInfo.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [  ]

    symbolicNames = [ "<INVALID>", "URL", "EMAIL", "NUMBER10", "NUMBER11", 
                      "FLOAT", "VERSION", "WORD", "WS" ]

    RULE_text = 0
    RULE_email = 1
    RULE_melli_number = 2
    RULE_phonenumber = 3
    RULE_float = 4
    RULE_url = 5
    RULE_version = 6

    ruleNames =  [ "text", "email", "melli_number", "phonenumber", "float", 
                   "url", "version" ]

    EOF = Token.EOF
    URL=1
    EMAIL=2
    NUMBER10=3
    NUMBER11=4
    FLOAT=5
    VERSION=6
    WORD=7
    WS=8

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class TextContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def email(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExtractInfoParser.EmailContext)
            else:
                return self.getTypedRuleContext(ExtractInfoParser.EmailContext,i)


        def float_(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExtractInfoParser.FloatContext)
            else:
                return self.getTypedRuleContext(ExtractInfoParser.FloatContext,i)


        def melli_number(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExtractInfoParser.Melli_numberContext)
            else:
                return self.getTypedRuleContext(ExtractInfoParser.Melli_numberContext,i)


        def phonenumber(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExtractInfoParser.PhonenumberContext)
            else:
                return self.getTypedRuleContext(ExtractInfoParser.PhonenumberContext,i)


        def url(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExtractInfoParser.UrlContext)
            else:
                return self.getTypedRuleContext(ExtractInfoParser.UrlContext,i)


        def version(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExtractInfoParser.VersionContext)
            else:
                return self.getTypedRuleContext(ExtractInfoParser.VersionContext,i)


        def WORD(self, i:int=None):
            if i is None:
                return self.getTokens(ExtractInfoParser.WORD)
            else:
                return self.getToken(ExtractInfoParser.WORD, i)

        def WS(self, i:int=None):
            if i is None:
                return self.getTokens(ExtractInfoParser.WS)
            else:
                return self.getToken(ExtractInfoParser.WS, i)

        def getRuleIndex(self):
            return ExtractInfoParser.RULE_text

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterText" ):
                listener.enterText(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitText" ):
                listener.exitText(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitText" ):
                return visitor.visitText(self)
            else:
                return visitor.visitChildren(self)




    def text(self):

        localctx = ExtractInfoParser.TextContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_text)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 24
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 510) != 0):
                self.state = 22
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [2]:
                    self.state = 14
                    self.email()
                    pass
                elif token in [5]:
                    self.state = 15
                    self.float_()
                    pass
                elif token in [3]:
                    self.state = 16
                    self.melli_number()
                    pass
                elif token in [4]:
                    self.state = 17
                    self.phonenumber()
                    pass
                elif token in [1]:
                    self.state = 18
                    self.url()
                    pass
                elif token in [6]:
                    self.state = 19
                    self.version()
                    pass
                elif token in [7]:
                    self.state = 20
                    self.match(ExtractInfoParser.WORD)
                    pass
                elif token in [8]:
                    self.state = 21
                    self.match(ExtractInfoParser.WS)
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 26
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class EmailContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EMAIL(self):
            return self.getToken(ExtractInfoParser.EMAIL, 0)

        def getRuleIndex(self):
            return ExtractInfoParser.RULE_email

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEmail" ):
                listener.enterEmail(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEmail" ):
                listener.exitEmail(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEmail" ):
                return visitor.visitEmail(self)
            else:
                return visitor.visitChildren(self)




    def email(self):

        localctx = ExtractInfoParser.EmailContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_email)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 27
            self.match(ExtractInfoParser.EMAIL)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Melli_numberContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMBER10(self):
            return self.getToken(ExtractInfoParser.NUMBER10, 0)

        def getRuleIndex(self):
            return ExtractInfoParser.RULE_melli_number

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMelli_number" ):
                listener.enterMelli_number(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMelli_number" ):
                listener.exitMelli_number(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMelli_number" ):
                return visitor.visitMelli_number(self)
            else:
                return visitor.visitChildren(self)




    def melli_number(self):

        localctx = ExtractInfoParser.Melli_numberContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_melli_number)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 29
            self.match(ExtractInfoParser.NUMBER10)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PhonenumberContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMBER11(self):
            return self.getToken(ExtractInfoParser.NUMBER11, 0)

        def getRuleIndex(self):
            return ExtractInfoParser.RULE_phonenumber

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPhonenumber" ):
                listener.enterPhonenumber(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPhonenumber" ):
                listener.exitPhonenumber(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPhonenumber" ):
                return visitor.visitPhonenumber(self)
            else:
                return visitor.visitChildren(self)




    def phonenumber(self):

        localctx = ExtractInfoParser.PhonenumberContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_phonenumber)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 31
            self.match(ExtractInfoParser.NUMBER11)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FloatContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FLOAT(self):
            return self.getToken(ExtractInfoParser.FLOAT, 0)

        def getRuleIndex(self):
            return ExtractInfoParser.RULE_float

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFloat" ):
                listener.enterFloat(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFloat" ):
                listener.exitFloat(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFloat" ):
                return visitor.visitFloat(self)
            else:
                return visitor.visitChildren(self)




    def float_(self):

        localctx = ExtractInfoParser.FloatContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_float)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 33
            self.match(ExtractInfoParser.FLOAT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class UrlContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def URL(self):
            return self.getToken(ExtractInfoParser.URL, 0)

        def getRuleIndex(self):
            return ExtractInfoParser.RULE_url

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUrl" ):
                listener.enterUrl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUrl" ):
                listener.exitUrl(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUrl" ):
                return visitor.visitUrl(self)
            else:
                return visitor.visitChildren(self)




    def url(self):

        localctx = ExtractInfoParser.UrlContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_url)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 35
            self.match(ExtractInfoParser.URL)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VersionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VERSION(self):
            return self.getToken(ExtractInfoParser.VERSION, 0)

        def getRuleIndex(self):
            return ExtractInfoParser.RULE_version

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVersion" ):
                listener.enterVersion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVersion" ):
                listener.exitVersion(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVersion" ):
                return visitor.visitVersion(self)
            else:
                return visitor.visitChildren(self)




    def version(self):

        localctx = ExtractInfoParser.VersionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_version)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 37
            self.match(ExtractInfoParser.VERSION)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





