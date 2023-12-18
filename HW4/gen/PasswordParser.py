# Generated from /home/bijan/PycharmProjects/compiler-design/HW4/gen/Password.g4 by ANTLR 4.13.1
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
        4, 1, 3, 101, 2, 0, 7, 0, 1, 0, 1, 0, 1, 0, 5, 0, 6, 8, 0, 10, 0, 12, 0, 9, 9, 0, 1, 0, 1, 0,
        1, 0, 5, 0, 14, 8, 0, 10, 0, 12, 0, 17, 9, 0, 1, 0, 1, 0, 1, 0, 5, 0, 22, 8, 0, 10, 0, 12, 0,
        25, 9, 0, 1, 0, 1, 0, 1, 0, 5, 0, 30, 8, 0, 10, 0, 12, 0, 33, 9, 0, 1, 0, 1, 0, 1, 0, 5, 0, 38,
        8, 0, 10, 0, 12, 0, 41, 9, 0, 1, 0, 1, 0, 1, 0, 5, 0, 46, 8, 0, 10, 0, 12, 0, 49, 9, 0, 1, 0,
        1, 0, 1, 0, 5, 0, 54, 8, 0, 10, 0, 12, 0, 57, 9, 0, 1, 0, 1, 0, 1, 0, 5, 0, 62, 8, 0, 10, 0,
        12, 0, 65, 9, 0, 1, 0, 1, 0, 1, 0, 5, 0, 70, 8, 0, 10, 0, 12, 0, 73, 9, 0, 1, 0, 1, 0, 1, 0,
        5, 0, 78, 8, 0, 10, 0, 12, 0, 81, 9, 0, 1, 0, 1, 0, 1, 0, 5, 0, 86, 8, 0, 10, 0, 12, 0, 89,
        9, 0, 1, 0, 1, 0, 1, 0, 5, 0, 94, 8, 0, 10, 0, 12, 0, 97, 9, 0, 3, 0, 99, 8, 0, 1, 0, 0, 0, 1,
        0, 0, 4, 1, 0, 1, 2, 1, 0, 1, 3, 2, 0, 1, 1, 3, 3, 1, 0, 2, 3, 116, 0, 98, 1, 0, 0, 0, 2, 3, 5,
        1, 0, 0, 3, 7, 5, 2, 0, 0, 4, 6, 7, 0, 0, 0, 5, 4, 1, 0, 0, 0, 6, 9, 1, 0, 0, 0, 7, 5, 1, 0, 0,
        0, 7, 8, 1, 0, 0, 0, 8, 10, 1, 0, 0, 0, 9, 7, 1, 0, 0, 0, 10, 11, 5, 3, 0, 0, 11, 15, 1, 0, 0,
        0, 12, 14, 7, 1, 0, 0, 13, 12, 1, 0, 0, 0, 14, 17, 1, 0, 0, 0, 15, 13, 1, 0, 0, 0, 15, 16,
        1, 0, 0, 0, 16, 99, 1, 0, 0, 0, 17, 15, 1, 0, 0, 0, 18, 19, 5, 1, 0, 0, 19, 23, 5, 3, 0, 0,
        20, 22, 7, 2, 0, 0, 21, 20, 1, 0, 0, 0, 22, 25, 1, 0, 0, 0, 23, 21, 1, 0, 0, 0, 23, 24, 1,
        0, 0, 0, 24, 26, 1, 0, 0, 0, 25, 23, 1, 0, 0, 0, 26, 27, 5, 2, 0, 0, 27, 31, 1, 0, 0, 0, 28,
        30, 7, 1, 0, 0, 29, 28, 1, 0, 0, 0, 30, 33, 1, 0, 0, 0, 31, 29, 1, 0, 0, 0, 31, 32, 1, 0, 0,
        0, 32, 99, 1, 0, 0, 0, 33, 31, 1, 0, 0, 0, 34, 35, 5, 2, 0, 0, 35, 39, 5, 1, 0, 0, 36, 38,
        7, 0, 0, 0, 37, 36, 1, 0, 0, 0, 38, 41, 1, 0, 0, 0, 39, 37, 1, 0, 0, 0, 39, 40, 1, 0, 0, 0,
        40, 42, 1, 0, 0, 0, 41, 39, 1, 0, 0, 0, 42, 43, 5, 3, 0, 0, 43, 47, 1, 0, 0, 0, 44, 46, 7,
        1, 0, 0, 45, 44, 1, 0, 0, 0, 46, 49, 1, 0, 0, 0, 47, 45, 1, 0, 0, 0, 47, 48, 1, 0, 0, 0, 48,
        99, 1, 0, 0, 0, 49, 47, 1, 0, 0, 0, 50, 51, 5, 2, 0, 0, 51, 55, 5, 3, 0, 0, 52, 54, 7, 3, 0,
        0, 53, 52, 1, 0, 0, 0, 54, 57, 1, 0, 0, 0, 55, 53, 1, 0, 0, 0, 55, 56, 1, 0, 0, 0, 56, 58,
        1, 0, 0, 0, 57, 55, 1, 0, 0, 0, 58, 59, 5, 1, 0, 0, 59, 63, 1, 0, 0, 0, 60, 62, 7, 1, 0, 0,
        61, 60, 1, 0, 0, 0, 62, 65, 1, 0, 0, 0, 63, 61, 1, 0, 0, 0, 63, 64, 1, 0, 0, 0, 64, 99, 1,
        0, 0, 0, 65, 63, 1, 0, 0, 0, 66, 67, 5, 3, 0, 0, 67, 71, 5, 1, 0, 0, 68, 70, 7, 2, 0, 0, 69,
        68, 1, 0, 0, 0, 70, 73, 1, 0, 0, 0, 71, 69, 1, 0, 0, 0, 71, 72, 1, 0, 0, 0, 72, 74, 1, 0, 0,
        0, 73, 71, 1, 0, 0, 0, 74, 75, 5, 2, 0, 0, 75, 79, 1, 0, 0, 0, 76, 78, 7, 1, 0, 0, 77, 76,
        1, 0, 0, 0, 78, 81, 1, 0, 0, 0, 79, 77, 1, 0, 0, 0, 79, 80, 1, 0, 0, 0, 80, 99, 1, 0, 0, 0,
        81, 79, 1, 0, 0, 0, 82, 83, 5, 3, 0, 0, 83, 87, 5, 2, 0, 0, 84, 86, 7, 3, 0, 0, 85, 84, 1,
        0, 0, 0, 86, 89, 1, 0, 0, 0, 87, 85, 1, 0, 0, 0, 87, 88, 1, 0, 0, 0, 88, 90, 1, 0, 0, 0, 89,
        87, 1, 0, 0, 0, 90, 91, 5, 1, 0, 0, 91, 95, 1, 0, 0, 0, 92, 94, 7, 1, 0, 0, 93, 92, 1, 0, 0,
        0, 94, 97, 1, 0, 0, 0, 95, 93, 1, 0, 0, 0, 95, 96, 1, 0, 0, 0, 96, 99, 1, 0, 0, 0, 97, 95,
        1, 0, 0, 0, 98, 2, 1, 0, 0, 0, 98, 18, 1, 0, 0, 0, 98, 34, 1, 0, 0, 0, 98, 50, 1, 0, 0, 0, 98,
        66, 1, 0, 0, 0, 98, 82, 1, 0, 0, 0, 99, 1, 1, 0, 0, 0, 13, 7, 15, 23, 31, 39, 47, 55, 63,
        71, 79, 87, 95, 98
    ]


class PasswordParser(Parser):
    grammarFileName = "Password.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [DFA(ds, i) for i, ds in enumerate(atn.decisionToState)]

    sharedContextCache = PredictionContextCache()

    literalNames = []

    symbolicNames = ["<INVALID>", "CHARS", "DIGITS", "SPECIALCHARS"]

    RULE_password = 0

    ruleNames = ["password"]

    EOF = Token.EOF
    CHARS = 1
    DIGITS = 2
    SPECIALCHARS = 3

    def __init__(self, input: TokenStream, output: TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None

    class PasswordContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CHARS(self, i: int = None):
            if i is None:
                return self.getTokens(PasswordParser.CHARS)
            else:
                return self.getToken(PasswordParser.CHARS, i)

        def DIGITS(self, i: int = None):
            if i is None:
                return self.getTokens(PasswordParser.DIGITS)
            else:
                return self.getToken(PasswordParser.DIGITS, i)

        def SPECIALCHARS(self, i: int = None):
            if i is None:
                return self.getTokens(PasswordParser.SPECIALCHARS)
            else:
                return self.getToken(PasswordParser.SPECIALCHARS, i)

        def getRuleIndex(self):
            return PasswordParser.RULE_password

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterPassword"):
                listener.enterPassword(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitPassword"):
                listener.exitPassword(self)

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitPassword"):
                return visitor.visitPassword(self)
            else:
                return visitor.visitChildren(self)

    def password(self):

        localctx = PasswordParser.PasswordContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_password)
        self._la = 0  # Token type
        try:
            self.state = 98
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input, 12, self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 2
                self.match(PasswordParser.CHARS)
                self.state = 3
                self.match(PasswordParser.DIGITS)
                self.state = 7
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la == 1 or _la == 2:
                    self.state = 4
                    _la = self._input.LA(1)
                    if not (_la == 1 or _la == 2):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 9
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 10
                self.match(PasswordParser.SPECIALCHARS)
                self.state = 15
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & 14) != 0):
                    self.state = 12
                    _la = self._input.LA(1)
                    if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 14) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 17
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 18
                self.match(PasswordParser.CHARS)
                self.state = 19
                self.match(PasswordParser.SPECIALCHARS)
                self.state = 23
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la == 1 or _la == 3:
                    self.state = 20
                    _la = self._input.LA(1)
                    if not (_la == 1 or _la == 3):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 25
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 26
                self.match(PasswordParser.DIGITS)
                self.state = 31
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & 14) != 0):
                    self.state = 28
                    _la = self._input.LA(1)
                    if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 14) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 33
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 34
                self.match(PasswordParser.DIGITS)
                self.state = 35
                self.match(PasswordParser.CHARS)
                self.state = 39
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la == 1 or _la == 2:
                    self.state = 36
                    _la = self._input.LA(1)
                    if not (_la == 1 or _la == 2):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 41
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 42
                self.match(PasswordParser.SPECIALCHARS)
                self.state = 47
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & 14) != 0):
                    self.state = 44
                    _la = self._input.LA(1)
                    if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 14) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 49
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 50
                self.match(PasswordParser.DIGITS)
                self.state = 51
                self.match(PasswordParser.SPECIALCHARS)
                self.state = 55
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la == 2 or _la == 3:
                    self.state = 52
                    _la = self._input.LA(1)
                    if not (_la == 2 or _la == 3):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 57
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 58
                self.match(PasswordParser.CHARS)
                self.state = 63
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & 14) != 0):
                    self.state = 60
                    _la = self._input.LA(1)
                    if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 14) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 65
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 66
                self.match(PasswordParser.SPECIALCHARS)
                self.state = 67
                self.match(PasswordParser.CHARS)
                self.state = 71
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la == 1 or _la == 3:
                    self.state = 68
                    _la = self._input.LA(1)
                    if not (_la == 1 or _la == 3):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 73
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 74
                self.match(PasswordParser.DIGITS)
                self.state = 79
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & 14) != 0):
                    self.state = 76
                    _la = self._input.LA(1)
                    if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 14) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 81
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 82
                self.match(PasswordParser.SPECIALCHARS)
                self.state = 83
                self.match(PasswordParser.DIGITS)
                self.state = 87
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la == 2 or _la == 3:
                    self.state = 84
                    _la = self._input.LA(1)
                    if not (_la == 2 or _la == 3):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 89
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 90
                self.match(PasswordParser.CHARS)
                self.state = 95
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & 14) != 0):
                    self.state = 92
                    _la = self._input.LA(1)
                    if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 14) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 97
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx
