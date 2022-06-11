# Generated from Versus.g4 by ANTLR 4.9.3
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\7")
        buf.write("\23\4\2\t\2\4\3\t\3\3\2\3\2\5\2\t\n\2\3\3\3\3\3\3\3\3")
        buf.write("\3\3\3\3\5\3\21\n\3\3\3\2\2\4\2\4\2\2\2\23\2\b\3\2\2\2")
        buf.write("\4\20\3\2\2\2\6\t\5\4\3\2\7\t\3\2\2\2\b\6\3\2\2\2\b\7")
        buf.write("\3\2\2\2\t\3\3\2\2\2\n\13\7\3\2\2\13\21\7\6\2\2\f\r\7")
        buf.write("\4\2\2\r\21\7\6\2\2\16\17\7\5\2\2\17\21\7\6\2\2\20\n\3")
        buf.write("\2\2\2\20\f\3\2\2\2\20\16\3\2\2\2\21\5\3\2\2\2\4\b\20")
        return buf.getvalue()


class VersusParser ( Parser ):

    grammarFileName = "Versus.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'VS'", "'duration'", "'->'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "NUMBER", "WS" ]

    RULE_start = 0
    RULE_expr = 1

    ruleNames =  [ "start", "expr" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    NUMBER=4
    WS=5

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.3")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class StartContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(VersusParser.ExprContext,0)


        def getRuleIndex(self):
            return VersusParser.RULE_start

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStart" ):
                listener.enterStart(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStart" ):
                listener.exitStart(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStart" ):
                return visitor.visitStart(self)
            else:
                return visitor.visitChildren(self)




    def start(self):

        localctx = VersusParser.StartContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_start)
        try:
            self.state = 6
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [VersusParser.T__0, VersusParser.T__1, VersusParser.T__2]:
                self.enterOuterAlt(localctx, 1)
                self.state = 4
                self.expr()
                pass
            elif token in [VersusParser.EOF]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return VersusParser.RULE_expr

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class PlayerContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a VersusParser.ExprContext
            super().__init__(parser)
            self.name = None # Token
            self.copyFrom(ctx)

        def NUMBER(self):
            return self.getToken(VersusParser.NUMBER, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPlayer" ):
                listener.enterPlayer(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPlayer" ):
                listener.exitPlayer(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPlayer" ):
                return visitor.visitPlayer(self)
            else:
                return visitor.visitChildren(self)


    class Game_timeContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a VersusParser.ExprContext
            super().__init__(parser)
            self.time = None # Token
            self.copyFrom(ctx)

        def NUMBER(self):
            return self.getToken(VersusParser.NUMBER, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterGame_time" ):
                listener.enterGame_time(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitGame_time" ):
                listener.exitGame_time(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitGame_time" ):
                return visitor.visitGame_time(self)
            else:
                return visitor.visitChildren(self)


    class First_playerContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a VersusParser.ExprContext
            super().__init__(parser)
            self.player1 = None # Token
            self.copyFrom(ctx)

        def NUMBER(self):
            return self.getToken(VersusParser.NUMBER, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFirst_player" ):
                listener.enterFirst_player(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFirst_player" ):
                listener.exitFirst_player(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFirst_player" ):
                return visitor.visitFirst_player(self)
            else:
                return visitor.visitChildren(self)



    def expr(self):

        localctx = VersusParser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_expr)
        try:
            self.state = 14
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [VersusParser.T__0]:
                localctx = VersusParser.PlayerContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 8
                self.match(VersusParser.T__0)
                self.state = 9
                localctx.name = self.match(VersusParser.NUMBER)
                pass
            elif token in [VersusParser.T__1]:
                localctx = VersusParser.Game_timeContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 10
                self.match(VersusParser.T__1)
                self.state = 11
                localctx.time = self.match(VersusParser.NUMBER)
                pass
            elif token in [VersusParser.T__2]:
                localctx = VersusParser.First_playerContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 12
                self.match(VersusParser.T__2)
                self.state = 13
                localctx.player1 = self.match(VersusParser.NUMBER)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





