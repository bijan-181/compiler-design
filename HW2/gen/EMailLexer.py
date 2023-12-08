# Generated from EMail.g4 by ANTLR 4.7.2
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\n")
        buf.write("F\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\3\2\3\2\3\3\6\3\27\n\3\r\3\16\3\30\3")
        buf.write("\4\3\4\3\4\3\4\7\4\37\n\4\f\4\16\4\"\13\4\3\4\3\4\3\4")
        buf.write("\3\5\3\5\3\5\3\5\5\5+\n\5\3\6\3\6\3\7\3\7\3\b\3\b\3\t")
        buf.write("\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3")
        buf.write("\t\3\t\3\t\3\t\5\tE\n\t\2\2\n\3\3\5\4\7\5\t\6\13\7\r\b")
        buf.write("\17\t\21\n\3\2\5\4\2C\\c|\f\2##%),-//\61\61??AA`b}}\177")
        buf.write("\u0080\3\2\62;\2Q\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2")
        buf.write("\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21")
        buf.write("\3\2\2\2\3\23\3\2\2\2\5\26\3\2\2\2\7\32\3\2\2\2\t*\3\2")
        buf.write("\2\2\13,\3\2\2\2\r.\3\2\2\2\17\60\3\2\2\2\21D\3\2\2\2")
        buf.write("\23\24\7B\2\2\24\4\3\2\2\2\25\27\5\t\5\2\26\25\3\2\2\2")
        buf.write("\27\30\3\2\2\2\30\26\3\2\2\2\30\31\3\2\2\2\31\6\3\2\2")
        buf.write("\2\32 \5\13\6\2\33\37\5\13\6\2\34\37\5\17\b\2\35\37\7")
        buf.write("/\2\2\36\33\3\2\2\2\36\34\3\2\2\2\36\35\3\2\2\2\37\"\3")
        buf.write("\2\2\2 \36\3\2\2\2 !\3\2\2\2!#\3\2\2\2\" \3\2\2\2#$\7")
        buf.write("\60\2\2$%\5\21\t\2%\b\3\2\2\2&+\5\13\6\2\'+\5\17\b\2(")
        buf.write("+\5\r\7\2)+\7\60\2\2*&\3\2\2\2*\'\3\2\2\2*(\3\2\2\2*)")
        buf.write("\3\2\2\2+\n\3\2\2\2,-\t\2\2\2-\f\3\2\2\2./\t\3\2\2/\16")
        buf.write("\3\2\2\2\60\61\t\4\2\2\61\20\3\2\2\2\62\63\7e\2\2\63\64")
        buf.write("\7q\2\2\64E\7o\2\2\65\66\7q\2\2\66\67\7t\2\2\67E\7i\2")
        buf.write("\289\7p\2\29:\7g\2\2:E\7v\2\2;<\7k\2\2<E\7t\2\2=>\7k\2")
        buf.write("\2>?\7p\2\2?@\7h\2\2@E\7q\2\2AB\7i\2\2BC\7q\2\2CE\7x\2")
        buf.write("\2D\62\3\2\2\2D\65\3\2\2\2D8\3\2\2\2D;\3\2\2\2D=\3\2\2")
        buf.write("\2DA\3\2\2\2E\22\3\2\2\2\b\2\30\36 *D\2")
        return buf.getvalue()


class EMailLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    LocalPart = 2
    Domain = 3
    LocalPartRule = 4
    LETTER = 5
    PrintableCharacters = 6
    DIGIT = 7
    ListOfDomain = 8

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'@'" ]

    symbolicNames = [ "<INVALID>",
            "LocalPart", "Domain", "LocalPartRule", "LETTER", "PrintableCharacters", 
            "DIGIT", "ListOfDomain" ]

    ruleNames = [ "T__0", "LocalPart", "Domain", "LocalPartRule", "LETTER", 
                  "PrintableCharacters", "DIGIT", "ListOfDomain" ]

    grammarFileName = "EMail.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


