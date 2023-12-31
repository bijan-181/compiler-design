# Generated from /home/bijan/PycharmProjects/compiler-design/HW4/gen/Password.g4 by ANTLR 4.13.1
from antlr4 import *
from io import StringIO
import sys

if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


def serializedATN():
    return [
        4, 0, 3, 22, 6, -1, 2, 0, 7, 0, 2, 1, 7, 1, 2, 2, 7, 2, 1, 0, 4, 0, 9, 8, 0, 11, 0, 12, 0, 10,
        1, 1, 4, 1, 14, 8, 1, 11, 1, 12, 1, 15, 1, 2, 4, 2, 19, 8, 2, 11, 2, 12, 2, 20, 0, 0, 3, 1,
        1, 3, 2, 5, 3, 1, 0, 3, 2, 0, 65, 90, 97, 122, 1, 0, 48, 57, 7, 0, 33, 42, 44, 44, 46, 46,
        58, 60, 62, 64, 92, 92, 94, 94, 24, 0, 1, 1, 0, 0, 0, 0, 3, 1, 0, 0, 0, 0, 5, 1, 0, 0, 0, 1,
        8, 1, 0, 0, 0, 3, 13, 1, 0, 0, 0, 5, 18, 1, 0, 0, 0, 7, 9, 7, 0, 0, 0, 8, 7, 1, 0, 0, 0, 9, 10,
        1, 0, 0, 0, 10, 8, 1, 0, 0, 0, 10, 11, 1, 0, 0, 0, 11, 2, 1, 0, 0, 0, 12, 14, 7, 1, 0, 0, 13,
        12, 1, 0, 0, 0, 14, 15, 1, 0, 0, 0, 15, 13, 1, 0, 0, 0, 15, 16, 1, 0, 0, 0, 16, 4, 1, 0, 0,
        0, 17, 19, 7, 2, 0, 0, 18, 17, 1, 0, 0, 0, 19, 20, 1, 0, 0, 0, 20, 18, 1, 0, 0, 0, 20, 21,
        1, 0, 0, 0, 21, 6, 1, 0, 0, 0, 4, 0, 10, 15, 20, 0
    ]


class PasswordLexer(Lexer):
    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [DFA(ds, i) for i, ds in enumerate(atn.decisionToState)]

    CHARS = 1
    DIGITS = 2
    SPECIALCHARS = 3

    channelNames = [u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN"]

    modeNames = ["DEFAULT_MODE"]

    literalNames = ["<INVALID>",
                    ]

    symbolicNames = ["<INVALID>",
                     "CHARS", "DIGITS", "SPECIALCHARS"]

    ruleNames = ["CHARS", "DIGITS", "SPECIALCHARS"]

    grammarFileName = "Password.g4"

    def __init__(self, input=None, output: TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None
