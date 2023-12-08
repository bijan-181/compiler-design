# Generated from EMail.g4 by ANTLR 4.7.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing import TextIO
import sys


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\n")
        buf.write("\t\4\2\t\2\3\2\3\2\3\2\3\2\3\2\2\2\3\2\2\2\2\7\2\4\3\2")
        buf.write("\2\2\4\5\7\4\2\2\5\6\7\3\2\2\6\7\7\5\2\2\7\3\3\2\2\2\2")
        return buf.getvalue()


class EMailParser(Parser):
    grammarFileName = "EMail.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [DFA(ds, i) for i, ds in enumerate(atn.decisionToState)]

    sharedContextCache = PredictionContextCache()

    literalNames = ["<INVALID>", "'@'"]

    symbolicNames = ["<INVALID>", "<INVALID>", "LocalPart", "Domain", "LocalPartRule",
                     "LETTER", "PrintableCharacters", "DIGIT", "ListOfDomain"]

    RULE_start = 0

    ruleNames = ["start"]

    EOF = Token.EOF
    T__0 = 1
    LocalPart = 2
    Domain = 3
    LocalPartRule = 4
    LETTER = 5
    PrintableCharacters = 6
    DIGIT = 7
    ListOfDomain = 8

    def __init__(self, input: TokenStream, output: TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None

    class StartContext(ParserRuleContext):

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LocalPart(self):
            return self.getToken(EMailParser.LocalPart, 0)

        def Domain(self):
            return self.getToken(EMailParser.Domain, 0)

        def getRuleIndex(self):
            return EMailParser.RULE_start

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterStart"):
                listener.enterStart(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitStart"):
                listener.exitStart(self)

    def start(self):

        localctx = EMailParser.StartContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_start)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2
            self.match(EMailParser.LocalPart)
            self.state = 3
            self.match(EMailParser.T__0)
            self.state = 4
            self.match(EMailParser.Domain)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx
