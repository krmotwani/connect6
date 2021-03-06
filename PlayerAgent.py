from Tkinter import Tk, Button, Frame, Canvas
from tkFont import Font
from copy import deepcopy
import random
from enum import Enum
import time
from Main_GUI import *
from ConnectBoard import *

class PlayerType(Enum):
    Human = 1
    Bot = 2
    Random = 3

class RandomAgent():
    def move(self,obj,turn):
        if (obj.turnCount == 0):
            move = random.choice(obj.avail_cols())
            obj.board = obj.board.move(move,turn)
            obj.game = obj.update()
        else:
            for i in range(2):
                if obj.game==False:
                    move = random.choice(obj.avail_cols())
                    obj.board = obj.board.move(move,turn)
                    obj.game = obj.update()
        obj.turnCount = obj.turnCount + 1

class Human():
    def move(self,obj,x,turn):
        for i in x:
            if obj.game==False:
                obj.board = obj.board.move(i,turn)
                obj.game = obj.update()
        obj.turnCount = obj.turnCount + 1

class Bot():
    def move(self,obj, turn):
        pass
    #def move(self,obj,turn):
    #    if (obj.turnCount == 0):
    #        move = random.choice(obj.avail_cols())
    #       obj.board = obj.board.move(move,turn)
    #        obj.game = obj.update()
    #    else:
    #        for i in range(2):
    #            if obj.game==False:
    #                move = random.choice(obj.avail_cols())
    #                obj.board = obj.board.move(move,turn)
    #                obj.game = obj.update()
    #    obj.turnCount = obj.turnCount + 1
