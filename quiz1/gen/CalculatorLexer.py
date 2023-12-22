# Generated from /home/bijan/PycharmProjects/compiler-design/quiz1/gen/Calculator.g4 by ANTLR 4.13.1
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


def serializedATN():
    return [
        4,0,9,57,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,
        6,7,6,2,7,7,7,2,8,7,8,2,9,7,9,1,0,4,0,23,8,0,11,0,12,0,24,1,0,1,
        0,4,0,29,8,0,11,0,12,0,30,3,0,33,8,0,1,1,1,1,1,2,1,2,1,3,1,3,1,4,
        1,4,1,5,1,5,1,6,1,6,1,7,1,7,1,8,4,8,50,8,8,11,8,12,8,51,1,8,1,8,
        1,9,1,9,0,0,10,1,1,3,2,5,3,7,4,9,5,11,6,13,7,15,8,17,9,19,0,1,0,
        2,3,0,9,10,13,13,32,32,1,0,48,57,59,0,1,1,0,0,0,0,3,1,0,0,0,0,5,
        1,0,0,0,0,7,1,0,0,0,0,9,1,0,0,0,0,11,1,0,0,0,0,13,1,0,0,0,0,15,1,
        0,0,0,0,17,1,0,0,0,1,22,1,0,0,0,3,34,1,0,0,0,5,36,1,0,0,0,7,38,1,
        0,0,0,9,40,1,0,0,0,11,42,1,0,0,0,13,44,1,0,0,0,15,46,1,0,0,0,17,
        49,1,0,0,0,19,55,1,0,0,0,21,23,3,19,9,0,22,21,1,0,0,0,23,24,1,0,
        0,0,24,22,1,0,0,0,24,25,1,0,0,0,25,32,1,0,0,0,26,28,5,46,0,0,27,
        29,3,19,9,0,28,27,1,0,0,0,29,30,1,0,0,0,30,28,1,0,0,0,30,31,1,0,
        0,0,31,33,1,0,0,0,32,26,1,0,0,0,32,33,1,0,0,0,33,2,1,0,0,0,34,35,
        5,43,0,0,35,4,1,0,0,0,36,37,5,45,0,0,37,6,1,0,0,0,38,39,5,42,0,0,
        39,8,1,0,0,0,40,41,5,47,0,0,41,10,1,0,0,0,42,43,5,94,0,0,43,12,1,
        0,0,0,44,45,5,40,0,0,45,14,1,0,0,0,46,47,5,41,0,0,47,16,1,0,0,0,
        48,50,7,0,0,0,49,48,1,0,0,0,50,51,1,0,0,0,51,49,1,0,0,0,51,52,1,
        0,0,0,52,53,1,0,0,0,53,54,6,8,0,0,54,18,1,0,0,0,55,56,7,1,0,0,56,
        20,1,0,0,0,5,0,24,30,32,51,1,6,0,0
    ]

class CalculatorLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    NUMBER = 1
    PLUS = 2
    MINUS = 3
    MULTIPLY = 4
    DIVIDE = 5
    EXPONENTIATION = 6
    LPAREN = 7
    RPAREN = 8
    WS = 9

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'+'", "'-'", "'*'", "'/'", "'^'", "'('", "')'" ]

    symbolicNames = [ "<INVALID>",
            "NUMBER", "PLUS", "MINUS", "MULTIPLY", "DIVIDE", "EXPONENTIATION", 
            "LPAREN", "RPAREN", "WS" ]

    ruleNames = [ "NUMBER", "PLUS", "MINUS", "MULTIPLY", "DIVIDE", "EXPONENTIATION", 
                  "LPAREN", "RPAREN", "WS", "DIGIT" ]

    grammarFileName = "Calculator.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


