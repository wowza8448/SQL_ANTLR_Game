# Generated from Versus.g4 by ANTLR 4.9.3
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\7")
        buf.write("/\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\3\2\3\2")
        buf.write("\3\2\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\4\3\4\3\4\3")
        buf.write("\5\6\5\36\n\5\r\5\16\5\37\3\5\6\5#\n\5\r\5\16\5$\5\5\'")
        buf.write("\n\5\3\6\6\6*\n\6\r\6\16\6+\3\6\3\6\2\2\7\3\3\5\4\7\5")
        buf.write("\t\6\13\7\3\2\3\5\2\13\f\17\17\"\"\2\62\2\3\3\2\2\2\2")
        buf.write("\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\3\r\3")
        buf.write("\2\2\2\5\20\3\2\2\2\7\31\3\2\2\2\t\35\3\2\2\2\13)\3\2")
        buf.write("\2\2\r\16\7X\2\2\16\17\7U\2\2\17\4\3\2\2\2\20\21\7f\2")
        buf.write("\2\21\22\7w\2\2\22\23\7t\2\2\23\24\7c\2\2\24\25\7v\2\2")
        buf.write("\25\26\7k\2\2\26\27\7q\2\2\27\30\7p\2\2\30\6\3\2\2\2\31")
        buf.write("\32\7/\2\2\32\33\7@\2\2\33\b\3\2\2\2\34\36\4\62;\2\35")
        buf.write("\34\3\2\2\2\36\37\3\2\2\2\37\35\3\2\2\2\37 \3\2\2\2 &")
        buf.write("\3\2\2\2!#\4\62;\2\"!\3\2\2\2#$\3\2\2\2$\"\3\2\2\2$%\3")
        buf.write("\2\2\2%\'\3\2\2\2&\"\3\2\2\2&\'\3\2\2\2\'\n\3\2\2\2(*")
        buf.write("\t\2\2\2)(\3\2\2\2*+\3\2\2\2+)\3\2\2\2+,\3\2\2\2,-\3\2")
        buf.write("\2\2-.\b\6\2\2.\f\3\2\2\2\7\2\37$&+\3\b\2\2")
        return buf.getvalue()


class VersusLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    NUMBER = 4
    WS = 5

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'VS'", "'duration'", "'->'" ]

    symbolicNames = [ "<INVALID>",
            "NUMBER", "WS" ]

    ruleNames = [ "T__0", "T__1", "T__2", "NUMBER", "WS" ]

    grammarFileName = "Versus.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.3")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


