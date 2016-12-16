#!/usr/bin/python
import random
import sys

#Class Definitions
#Pos class to hold a position on the board or the dimension of the board (used to make handling moves easier).
class Pos:
    #Constructed with the x and y values.
    def __init__(self,x,y):
        self.x = x
        self.y = y
        return
    def __str__(self):
        return "("+str(self.x)+","+str(self.y)+")"
    def __repr__(self):
        return "("+str(self.x)+","+str(self.y)+")"

#Board class to hold all of the state needed for each attempt.
class Board:
    #Constructed with the width and height values of the board.
    def __init__(self,width,height):
        self.tiles = []
        self.width = width
        self.height = height
        self.move_counter = 1
        self.person = Pos(0,0)
        for y in range(height):
            row = []
            for x in range(width):
               row.append("x") 
            self.tiles.append(row)
        self.tiles[0][0] = "1"
        return
    def __str__(self):
        output = ""
        for y in range(self.height):
            for x in range(self.width):
                output += self.tiles[y][x] + " " 
            output += "\n"

        return output

#Check if the give pos is with in given dim both parameters are type Pos.
def aabb(pos,dim):
    return pos.x < dim.x and pos.x > 0 and pos.y < dim.y and pos.y > 0

#Checks if the submitted offset (i.e the move) is valid, if it is valid it adds it to the list of valid moves.
def check_move(board,offset_x,offset_y,moves):
    move = Pos(board.person.x+offset_x,board.person.y+offset_y)
    if aabb(move,Pos(board.width,board.height)):
        if board.tiles[move.y][move.x] == "x":
            moves.append(move)
        return
    return
        
#Looks at all possible moves, and returns a list of the valid moves.
def check_moves(board):
    moves = []
    check_move(board,2,1,moves)
    check_move(board,-2,1,moves)
    check_move(board,2,-1,moves)
    check_move(board,-2,-1,moves)
    check_move(board,1,2,moves)
    check_move(board,-1,2,moves)
    check_move(board,1,-2,moves)
    check_move(board,-1,-2,moves)
    return moves

#Picks a move randomly and move the knight to the position.

    moves = check_moves(board)
    numb_of_moves = len(moves) 
    if(numb_of_moves > 0):
        numb = random.randint(0,len(moves)-1)
        move = moves[numb]
        board.move_counter += 1
        board.tiles[move.y][move.x] = str(board.move_counter)
        board.person = move
        return True
    else:
        return False

#Checks if the board is a success or a failure.
def check_board(board):
    for row in board.tiles:
        for tile in row:
            if tile == "x":
                return False
    return True

#Set initial variables.
width = int(sys.argv[1])
height = int(sys.argv[2])
attempts = int(sys.argv[3])

#Loop over the number of attempts.
for x in range(attempts):
    board = Board(width,height)
    #Loop over the moves till knight can not move.
    while(pick_move(board)):
        continue
    #Check is this attempt succeed.
    if(check_board(board)):
        print "SUCCESS:"
        print board
        break
    #If the attempt failed and it is the last attempt then print FAIL.
    if(x == attempts-1):
        print "FAIL:"
        print board



