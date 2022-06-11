# Generated from Versus.g4 by ANTLR 4.9.3
import shutil
import errno
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .VersusParser import VersusParser
else:
    from VersusParser import VersusParser

# This class defines a complete generic visitor for a parse tree produced by VersusParser.
game_time = 0

class VersusVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by VersusParser#start.
    def visitStart(self, ctx:VersusParser.StartContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VersusParser#Player.
    def visitPlayer(self, ctx:VersusParser.PlayerContext):
        global game_time
        player_name = ctx.name.text
        src = 'players_LIB/' + player_name
        dest = 'players/' + player_name
        try:
            shutil.copytree(src, dest)
        except:
            print("File exists")
        return self.visitChildren(ctx)
	
    # Visit a parse tree produced by VersusParser#Game_time.
    def visitGame_time(self, ctx:VersusParser.Game_timeContext):
        global game_time
        duration = ctx.time.text
        game_time = duration
        return self.visitChildren(ctx)
		
	# Visit a parse tree produced by VersusParser#First_player.
    def visitFirst_player(self, ctx:VersusParser.First_playerContext):
        player_name = ctx.player1.text
        src = 'players_LIB/' + player_name
        dest = 'players/' + player_name
        try:
            shutil.copytree(src, dest)
        except:
            print("File exists")
        return self.visitChildren(ctx)
	
    def get_game_time():
        global game_time
        game_time = int(game_time)
        return game_time

del VersusParser