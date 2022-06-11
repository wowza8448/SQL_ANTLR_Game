from antlr4 import * 
from VersusLexer import VersusLexer
from VersusParser import VersusParser
from VersusVisitor import VersusVisitor
import time
from threading import Timer
import subprocess



def main():
    lexer = VersusLexer (FileStream("players_input"))
    token_stream = CommonTokenStream(lexer)
    parser = VersusParser(token_stream)
    visitor = VersusVisitor()
    while True: 
        tree = parser.start()
        if tree.expr() == None:
            break
        visitor.visit(tree)

if __name__ == '__main__':
    #Run main
    main()
    game_time = VersusVisitor.get_game_time()
    #Run game engine with timer
    if game_time == 0:
        subprocess.call(['python3', 'game_engine.py'])
    else:
        try:
            subprocess.call(['python3', 'game_engine.py'], timeout=game_time)
        except subprocess.TimeoutExpired:
            print("Game exited after duration passed")