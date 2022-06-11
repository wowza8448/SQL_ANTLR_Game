# Generated from Versus.g4 by ANTLR 4.9.3
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .VersusParser import VersusParser
else:
    from VersusParser import VersusParser

# This class defines a complete listener for a parse tree produced by VersusParser.
class VersusListener(ParseTreeListener):

    # Enter a parse tree produced by VersusParser#start.
    def enterStart(self, ctx:VersusParser.StartContext):
        pass

    # Exit a parse tree produced by VersusParser#start.
    def exitStart(self, ctx:VersusParser.StartContext):
        pass


    # Enter a parse tree produced by VersusParser#Player.
    def enterPlayer(self, ctx:VersusParser.PlayerContext):
        pass

    # Exit a parse tree produced by VersusParser#Player.
    def exitPlayer(self, ctx:VersusParser.PlayerContext):
        pass


    # Enter a parse tree produced by VersusParser#Game_time.
    def enterGame_time(self, ctx:VersusParser.Game_timeContext):
        pass

    # Exit a parse tree produced by VersusParser#Game_time.
    def exitGame_time(self, ctx:VersusParser.Game_timeContext):
        pass


    # Enter a parse tree produced by VersusParser#First_player.
    def enterFirst_player(self, ctx:VersusParser.First_playerContext):
        pass

    # Exit a parse tree produced by VersusParser#First_player.
    def exitFirst_player(self, ctx:VersusParser.First_playerContext):
        pass



del VersusParser