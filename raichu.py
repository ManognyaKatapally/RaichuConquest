#
# raichu.py : Play the game of Raichu
#
# PLEASE PUT YOUR NAMES AND USER IDS HERE!
#
# Based on skeleton code by D. Crandall, Oct 2021
#
import sys
import time
import copy
import random

def board_to_string(board, N):
    return "\n".join(board[i:i+N] for i in range(0, len(board), N))

import copy
#Returns all the possible moves of Pichus,pikachus and Raichus along with its board score.
def moves(board, player):
    moveslist=[]
    for i in range(len(board[0])):
        for j in range(len(board[0])):
            if board[i][j]=='w' or board[i][j]=='b':
               moveslist.extend(movable_pichu(board,i,j,player))
            if board[i][j]=='W' or board[i][j]=='B':
               moveslist.extend(movable_pikachu(board,i,j,player))
            if board[i][j]=='@' or board[i][j]=='$':
               moveslist.extend(movable_raichu(board,i,j,player))
   
    moveslist.reverse()
    return sorted(moveslist,key=lambda ele:(-ele[1],ele[0]))

#Converts all the pieces to Racichus if they reach the opposite extreme row.
def raichu_conversion(board,player,kill):
    score=0
    new_board=copy.deepcopy(board)
    for i in range(0,len(new_board)):
        if new_board[0][i]=='b' or new_board[0][i]=='B':
            new_board[0][i]='$'
        elif new_board[len(new_board)-1][i]=='w' or new_board[len(new_board)-1][i]=='W':
            new_board[len(new_board)-1][i]='@'
    score= eval(new_board,player,kill)
    return (new_board, score)

#Returns all possible moves of Pichus along with it's ability to capture opp player's piece
def movable_pichu(board,i,j,player):
    pichu_boards=[]
    if board[i][j]==player and player=='w':
        movable_locations_pichu=[]
        if j!=0 and j!= len(board)-1 and i<len(board)-1:
            movable_locations_pichu=[(i+1,j-1),(i+1,j+1)]
        elif j==0 and i<i<len(board)-1:
            movable_locations_pichu=[(i+1,j+1)]
        elif j== len(board)-1 and i<len(board)-1:
            movable_locations_pichu=[(i+1,j-1)]
        for loc in movable_locations_pichu:
            if board[loc[0]][loc[1]] == '.':
                board_pichucopy = copy.deepcopy(board)
                board_pichucopy[loc[0]][loc[1]]='w'
                board_pichucopy[i][j]='.'
                pichu_boards.append(raichu_conversion(board_pichucopy,player,0))

            if board[loc[0]][loc[1]] == 'b': 
                if loc[1]<j and loc[0]<len(board)-1:
                    if loc[1]==0:
                        break
                    else:
                        board_pichucopy = copy.deepcopy(board)
                        if board_pichucopy[loc[0]+1][loc[1]-1] == '.':
                            board_pichucopy[loc[0]+1][loc[1]-1] = 'w'
                            board_pichucopy[loc[0]][loc[1]]='.'
                            board_pichucopy[i][j]='.'
                            pichu_boards.append(raichu_conversion(board_pichucopy,player,1))

                elif loc[1]!=len(board)-1 and loc[0]<len(board)-1 and loc[1]>j:
                    board_pichucopy = copy.deepcopy(board)
                    if board_pichucopy[loc[0]+1][loc[1]+1] == '.':
                        board_pichucopy[loc[0]+1][loc[1]+1] = 'w'
                        board_pichucopy[loc[0]][loc[1]]='.'
                        board_pichucopy[i][j]='.'
                        pichu_boards.append(raichu_conversion(board_pichucopy,player,1))
                                
    elif player=='b' and board[i][j]=='b':
        movable_locations_pichu=[]
        if j!=0 and j!= len(board)-1 and i>0:
            movable_locations_pichu=[(i-1,j-1),(i-1,j+1)]
        elif j==0 and i>0:
            movable_locations_pichu=[(i-1,j+1)]
        elif j== len(board)-1 and i>0:
            movable_locations_pichu=[(i-1,j-1)]
        for loc in movable_locations_pichu:
            if board[loc[0]][loc[1]] == '.':
                board_pichucopy = copy.deepcopy(board)
                board_pichucopy[loc[0]][loc[1]]='b'
                board_pichucopy[i][j]='.'
                pichu_boards.append(raichu_conversion(board_pichucopy,player,0))

            if board[loc[0]][loc[1]] == 'w': 
                if loc[1]<j and loc[1]!=0 and loc[0]>0:
                    board_pichucopy = copy.deepcopy(board)
                    if board_pichucopy[loc[0]-1][loc[1]-1] == '.':
                        board_pichucopy[loc[0]-1][loc[1]-1] = 'b'
                        board_pichucopy[loc[0]][loc[1]]='.'
                        board_pichucopy[i][j]='.'
                        pichu_boards.append(raichu_conversion(board_pichucopy,player,1))
                elif loc[1]<len(board)-1 and loc[0]>0 and loc[1]>j:
                    board_pichucopy = copy.deepcopy(board)
                    if board_pichucopy[loc[0]-1][loc[1]+1] == '.':
                        board_pichucopy[loc[0]-1][loc[1]+1] = 'b'
                        board_pichucopy[loc[0]][loc[1]]='.'
                        board_pichucopy[i][j]='.'
                        pichu_boards.append(raichu_conversion(board_pichucopy,player,1))

    return pichu_boards

#Returns all possible moves of Pikachus along with it's ability to capture opp player's piece
def movable_pikachu(board,i,j,player):
    pikachu_boards=[]

    if player.upper()=='W' and board[i][j]=='W':
        movable_locations_pikachu=[]
        if j>0 and j< len(board)-1:
            if i<len(board)-1:
                movable_locations_pikachu=[(i+1,j),(i,j-1),(i,j+1)]
            else:
                movable_locations_pikachu=[(i,j-1),(i,j+1)]
        elif j==0:
            if i<len(board)-1:
                movable_locations_pikachu=[(i+1,j),(i,j+1)]
            else:
                movable_locations_pikachu=[(i,j+1)]

        elif j== len(board)-1:
            if i<len(board)-1:
                movable_locations_pikachu=[(i+1,j),(i,j-1)]
            else:
                movable_locations_pikachu=[(i,j-1)]

        for loc in movable_locations_pikachu:
            if board[loc[0]][loc[1]] == '.':
                board_pikachucopy = copy.deepcopy(board)
                board_pikachucopy[loc[0]][loc[1]]='W'
                board_pikachucopy[i][j]='.'
                pikachu_boards.append(raichu_conversion(board_pikachucopy,player,0))
                if loc[1]==j  and loc[0]<len(board)-1:
                    if board[loc[0]+1][loc[1]] == '.':
                        board_pikachucopy = copy.deepcopy(board)
                        board_pikachucopy[loc[0]+1][loc[1]]='W'
                        board_pikachucopy[i][j]='.'
                        pikachu_boards.append(raichu_conversion(board_pikachucopy,player,0))
                    if (board[loc[0]+1][loc[1]] == 'B' or board[loc[0]+1][loc[1]] == 'b') and loc[0]+1<len(board)-1: 
                            board_pikachucopy = copy.deepcopy(board)
                            if board_pikachucopy[loc[0]+2][loc[1]] == '.':
                                board_pikachucopy[loc[0]+2][loc[1]] = 'W'
                                #replace B to .
                                board_pikachucopy[loc[0]+1][loc[1]]='.'
                                board_pikachucopy[i][j]='.'
                                pikachu_boards.append(raichu_conversion(board_pikachucopy,player,2))

                #checking the second position left if the move is left
                if  loc[1]>0 and loc[1]<j:
                    if board[loc[0]][loc[1]-1] == '.':
                        board_pikachucopy = copy.deepcopy(board)
                        board_pikachucopy[loc[0]][loc[1]-1]='W'
                        board_pikachucopy[i][j]='.'
                        pikachu_boards.append(raichu_conversion(board_pikachucopy,player,0))
                    if (board[loc[0]][loc[1]-1] == 'B' or board[loc[0]][loc[1]-1] == 'b') and loc[1]-1>0: 
                            board_pikachucopy = copy.deepcopy(board)
                            if board_pikachucopy[loc[0]][loc[1]-2] == '.':
                                board_pikachucopy[loc[0]][loc[1]-2] = 'W'
                                #replace B to .
                                board_pikachucopy[loc[0]][loc[1]-1]='.'
                                board_pikachucopy[i][j]='.'
                                pikachu_boards.append(raichu_conversion(board_pikachucopy,player,2))

                #checking the second position right if the move is right
                if  loc[1]<len(board)-1 and loc[1]>j:
                    if board[loc[0]][loc[1]+1] == '.':
                        board_pikachucopy = copy.deepcopy(board)
                        board_pikachucopy[loc[0]][loc[1]+1]='W'
                        board_pikachucopy[i][j]='.'
                        pikachu_boards.append(raichu_conversion(board_pikachucopy,player,0))
                    if (board[loc[0]][loc[1]+1] == 'B'  or board[loc[0]][loc[1]+1] == 'b') and loc[1]+1<len(board)-1: 
                            board_pikachucopy = copy.deepcopy(board)
                            if board_pikachucopy[loc[0]][loc[1]+2] == '.':
                                board_pikachucopy[loc[0]][loc[1]+2] = 'W'
                                #replace B to .
                                board_pikachucopy[loc[0]][loc[1]+1]='.'
                                board_pikachucopy[i][j]='.'
                                pikachu_boards.append(raichu_conversion(board_pikachucopy,player,2))
            elif board[loc[0]][loc[1]] == 'b' or board[loc[0]][loc[1]] == 'B':
                #checking the second position forward if the move is forward
                if loc[1]==j  and loc[0]<len(board)-1:
                    if board[loc[0]+1][loc[1]] == '.':
                        board_pikachucopy = copy.deepcopy(board)
                        board_pikachucopy[loc[0]][loc[1]]='.'
                        board_pikachucopy[loc[0]+1][loc[1]]='W'
                        board_pikachucopy[i][j]='.'
                        pikachu_boards.append(raichu_conversion(board_pikachucopy,player,2))

                #checking the second position left if the move is left
                if  loc[1]>0 and loc[1]<j:
                    if board[loc[0]][loc[1]-1] == '.':
                        board_pikachucopy = copy.deepcopy(board)
                        board_pikachucopy[loc[0]][loc[1]]='.'
                        board_pikachucopy[loc[0]][loc[1]-1]='W'
                        board_pikachucopy[i][j]='.'
                        pikachu_boards.append(raichu_conversion(board_pikachucopy,player,2))
                  

                #checking the second position right if the move is right
                if  loc[1]<len(board)-1 and loc[1]>j:
                    if board[loc[0]][loc[1]+1] == '.':
                        board_pikachucopy = copy.deepcopy(board)
                        board_pikachucopy[loc[0]][loc[1]]='.'
                        board_pikachucopy[loc[0]][loc[1]+1]='W'
                        board_pikachucopy[i][j]='.'
                        pikachu_boards.append(raichu_conversion(board_pikachucopy,player,2))
    
    #If the player is b
    elif player=='b' and board[i][j]=='B':
        movable_locations_pikachu=[]
        if j>0 and j< len(board)-1:
            if i>0:
                movable_locations_pikachu=[(i-1,j),(i,j-1),(i,j+1)]
            else:
                movable_locations_pikachu=[(i,j-1),(i,j+1)]
        elif j==0:
            if i>0:
                movable_locations_pikachu=[(i-1,j),(i,j+1)]
            else:
                movable_locations_pikachu=[(i,j+1)]
            
        elif j== len(board)-1:
            if i>0:
                movable_locations_pikachu=[(i-1,j),(i,j-1)]
            else:
                movable_locations_pikachu=[(i,j-1)]


        for loc in movable_locations_pikachu:
            if board[loc[0]][loc[1]] == '.':
                board_pikachucopy = copy.deepcopy(board)
                board_pikachucopy[loc[0]][loc[1]]='B'
                board_pikachucopy[i][j]='.'
                pikachu_boards.append(raichu_conversion(board_pikachucopy,player,0))
                if loc[1]==j  and loc[0]>0:
                    if board[loc[0]-1][loc[1]] == '.':
                        board_pikachucopy = copy.deepcopy(board)
                        board_pikachucopy[loc[0]-1][loc[1]]='B'
                        board_pikachucopy[i][j]='.'
                        pikachu_boards.append(raichu_conversion(board_pikachucopy,player,0))
                    elif (board[loc[0]-1][loc[1]] == 'W' or board[loc[0]-1][loc[1]] =='w')  and loc[0]-1>0: 
                            board_pikachucopy = copy.deepcopy(board)
                            if board_pikachucopy[loc[0]-2][loc[1]] == '.':
                                board_pikachucopy[loc[0]-2][loc[1]] = 'B'
                                #replace B to .
                                board_pikachucopy[loc[0]-1][loc[1]]='.'
                                board_pikachucopy[i][j]='.'
                                pikachu_boards.append(raichu_conversion(board_pikachucopy,player,2))

                #checking the second position left if the move is left
                if  loc[1]>0 and loc[1]<j:
                    if board[loc[0]][loc[1]-1] == '.':
                        board_pikachucopy = copy.deepcopy(board)
                        board_pikachucopy[loc[0]][loc[1]-1]='B'
                        board_pikachucopy[i][j]='.'
                        pikachu_boards.append(raichu_conversion(board_pikachucopy,player,0))
                    if (board[loc[0]][loc[1]-1] == 'W' or board[loc[0]][loc[1]-1] == 'w') and loc[0]-1>0: 
                            board_pikachucopy = copy.deepcopy(board)
                            if board_pikachucopy[loc[0]][loc[1]-2] == '.':
                                board_pikachucopy[loc[0]][loc[1]-2] = 'B'
                                #replace B to .
                                board_pikachucopy[loc[0]][loc[1]-1]='.'
                                board_pikachucopy[i][j]='.'
                                pikachu_boards.append(raichu_conversion(board_pikachucopy,player,2))

                #checking the second position right if the move is right
                if  loc[1]<len(board)-1 and loc[1]>j:
                    if board[loc[0]][loc[1]+1] == '.':
                        board_pikachucopy = copy.deepcopy(board)
                        board_pikachucopy[loc[0]][loc[1]+1]='B'
                        board_pikachucopy[i][j]='.'
                        pikachu_boards.append(raichu_conversion(board_pikachucopy,player,0))
                    if (board[loc[0]][loc[1]+1] == 'W' or board[loc[0]][loc[1]+1] == 'w') and loc[1]+1<len(board)-1: 
                            board_pikachucopy = copy.deepcopy(board)
                            if board_pikachucopy[loc[0]][loc[1]+2] == '.':
                                board_pikachucopy[loc[0]][loc[1]+2] = 'B'
                                #replace B to .
                                board_pikachucopy[loc[0]][loc[1]+1]='.'
                                board_pikachucopy[i][j]='.'
                                pikachu_boards.append(raichu_conversion(board_pikachucopy,player,2))
                                
            elif board[loc[0]][loc[1]] == 'w' or board[loc[0]][loc[1]] == 'W':
                #checking the second position forward if the move is forward
                if loc[1]==j  and loc[0]>0:
                    if board[loc[0]-1][loc[1]] == '.':
                        board_pikachucopy = copy.deepcopy(board)
                        board_pikachucopy[loc[0]][loc[1]]='.'
                        board_pikachucopy[loc[0]-1][loc[1]]='B'
                        board_pikachucopy[i][j]='.'
                        pikachu_boards.append(raichu_conversion(board_pikachucopy,player,2))
                    else:
                        continue

                #checking the second position left if the move is left
                if  loc[1]>0 and loc[1]<j:
                    if board[loc[0]][loc[1]-1] == '.':
                        board_pikachucopy = copy.deepcopy(board)
                        board_pikachucopy[loc[0]][loc[1]]='.'
                        board_pikachucopy[loc[0]][loc[1]-1]='B'
                        board_pikachucopy[i][j]='.'
                        pikachu_boards.append(raichu_conversion(board_pikachucopy,player,2))

                #checking the second position right if the move is right
                if  loc[1]<len(board)-1 and loc[1]>j:
                    if board[loc[0]][loc[1]+1] == '.':
                        board_pikachucopy = copy.deepcopy(board)
                        board_pikachucopy[loc[0]][loc[1]]='.'
                        board_pikachucopy[loc[0]][loc[1]+1]='B'
                        board_pikachucopy[i][j]='.'
                        pikachu_boards.append(raichu_conversion(board_pikachucopy,player,2))
                    
    return pikachu_boards

#Returns all possible moves of Raichus along with it's ability to capture opp player's piece
def movable_raichu(board,i,j,player):
    capturable_pawns_w = '$bB'
    capturable_pawns_b = '@wW'
    raichu_boards=[]
    if board[i][j]=='@' and player=='w':
        #Upper
        for x in range(i-1,-1,-1):
            if board[x][j]=='.':
                board_raichucopy = copy.deepcopy(board)
                board_raichucopy[x][j]='@'
                board_raichucopy[i][j]='.'
                raichu_boards.append(raichu_conversion(board_raichucopy,player,0))
            elif board[x][j] in capturable_pawns_w and x>0:
                if board[x-1][j]!='.':
                    break
                else:
                    board_raichucopy = copy.deepcopy(board)
                    board_raichucopy[x-1][j]='@'
                    board_raichucopy[i][j]='.'
                    board_raichucopy[x][j]='.'
                    if  board[x][j] == '$':
                        raichu_boards.append(raichu_conversion(board_raichucopy,player,20))
                    elif board[x][j] == 'B':
                        raichu_boards.append(raichu_conversion(board_raichucopy,player,10))
                    else:
                        raichu_boards.append(raichu_conversion(board_raichucopy,player,5))
                    
                    break
            else:
                break
        #Down
        for x in range(i+1,len(board)):
            if board[x][j]=='.':
                board_raichucopy = copy.deepcopy(board)
                board_raichucopy[x][j]='@'
                board_raichucopy[i][j]='.'
                raichu_boards.append(raichu_conversion(board_raichucopy,player,0))
            elif board[x][j] in capturable_pawns_w and x<len(board)-1 :
                if board[x+1][j]!='.':
                    break
                else:
                    board_raichucopy = copy.deepcopy(board)
                    board_raichucopy[x+1][j]='@'
                    board_raichucopy[i][j]='.'
                    board_raichucopy[x][j]='.'
                    if  board[x][j] == '$':
                        raichu_boards.append(raichu_conversion(board_raichucopy,player,20))
                    elif board[x][j] == 'B':
                        raichu_boards.append(raichu_conversion(board_raichucopy,player,10))
                    else:
                        raichu_boards.append(raichu_conversion(board_raichucopy,player,5))
                    break
            else:
                break
        #left
        for x in range(j-1,-1,-1):
            if board[i][x]=='.':
                board_raichucopy = copy.deepcopy(board)
                board_raichucopy[i][x]='@'
                board_raichucopy[i][j]='.'
                raichu_boards.append(raichu_conversion(board_raichucopy,player,0))
            elif board[i][x] in capturable_pawns_w and x>0:
                if board[i][x-1]!='.':
                    break
                else:
                    board_raichucopy = copy.deepcopy(board)
                    board_raichucopy[i][x-1]='@'
                    board_raichucopy[i][j]='.'
                    board_raichucopy[i][x]='.'
                    if  board[i][x] == '$':
                        raichu_boards.append(raichu_conversion(board_raichucopy,player,20))
                    elif board[i][x] == 'B':
                        raichu_boards.append(raichu_conversion(board_raichucopy,player,10))
                    else:
                        raichu_boards.append(raichu_conversion(board_raichucopy,player,5))
                    break
            else:
                break
        #Right
        for x in range(j+1,len(board)):
            if board[i][x]=='.':
                board_raichucopy = copy.deepcopy(board)
                board_raichucopy[i][x]='@'
                board_raichucopy[i][j]='.'
                raichu_boards.append(raichu_conversion(board_raichucopy,player,0))
            elif board[i][x] in capturable_pawns_w and x<len(board)-1:
                if board[i][x+1]!='.':
                    break
                else:
                    board_raichucopy = copy.deepcopy(board)
                    board_raichucopy[i][x+1]='@'
                    board_raichucopy[i][j]='.'
                    board_raichucopy[i][x]='.'
                    if board[i][x] == '$':
                        raichu_boards.append(raichu_conversion(board_raichucopy,player,20))
                    elif board[i][x] == 'B':
                        raichu_boards.append(raichu_conversion(board_raichucopy,player,10))
                    else:
                        raichu_boards.append(raichu_conversion(board_raichucopy,player,5))
                    break
            else:
                break
        #RightUpperDiag
        for (x,y) in zip(range(i-1,-1,-1),range(j+1,len(board))):
            if board[x][y]=='.':
                board_raichucopy = copy.deepcopy(board)
                board_raichucopy[x][y]='@'
                board_raichucopy[i][j]='.'
                raichu_boards.append(raichu_conversion(board_raichucopy,player,0))
            elif board[x][y] in capturable_pawns_w and x>0 and y<len(board)-1:
                if board[x-1][y+1]!='.':
                    break
                else:
                    board_raichucopy = copy.deepcopy(board)
                    board_raichucopy[x-1][y+1]='@'
                    board_raichucopy[i][j]='.'
                    board_raichucopy[x][y]='.'
                    if board[x][y] == '$':
                        raichu_boards.append(raichu_conversion(board_raichucopy,player,20))
                    elif board[x][y] == 'B':
                        raichu_boards.append(raichu_conversion(board_raichucopy,player,10))
                    else:
                        raichu_boards.append(raichu_conversion(board_raichucopy,player,5))
                    break
            else:
                break
                
        #LeftDownDiag
        for (x,y) in zip(range(i+1,len(board)),range(j-1,-1,-1)):
            if board[x][y]=='.':
                board_raichucopy = copy.deepcopy(board)
                board_raichucopy[x][y]='@'
                board_raichucopy[i][j]='.'
                raichu_boards.append(raichu_conversion(board_raichucopy,player,0))
            elif (board[x][y] in capturable_pawns_w) and x<len(board)-1 and y>0 : 
                if board[x+1][y-1]!='.':
                    break
                else:
                    board_raichucopy = copy.deepcopy(board)
                    board_raichucopy[x+1][y-1]='@'
                    board_raichucopy[i][j]='.'
                    board_raichucopy[x][y]='.'
                    if board[x][y] == '$':
                        raichu_boards.append(raichu_conversion(board_raichucopy,player,20))
                    elif board[x][y] == 'B':
                        raichu_boards.append(raichu_conversion(board_raichucopy,player,10))
                    else:
                        raichu_boards.append(raichu_conversion(board_raichucopy,player,5))
                    break
            else:
                break
            
        #LeftUpperDiag
        for (x,y) in zip(range(i-1,-1,-1),range(j-1,-1,-1)):
            if board[x][y]=='.':
                board_raichucopy = copy.deepcopy(board)
                board_raichucopy[x][y]='@'
                board_raichucopy[i][j]='.'
                raichu_boards.append(raichu_conversion(board_raichucopy,player,0))
            elif board[x][y] in capturable_pawns_w and x>0 and y>0:
                if board[x-1][y-1]!='.':
                    break
                else:
                    board_raichucopy = copy.deepcopy(board)
                    board_raichucopy[x-1][y-1]='@'
                    board_raichucopy[i][j]='.'
                    board_raichucopy[x][y]='.'
                    if board[x][y] == '$':
                        raichu_boards.append(raichu_conversion(board_raichucopy,player,20))
                    elif board[x][y] == 'B':
                        raichu_boards.append(raichu_conversion(board_raichucopy,player,10))
                    else:
                        raichu_boards.append(raichu_conversion(board_raichucopy,player,5))
                    break
            else:
                break
        #RightDownDiag
        for (x,y) in zip(range(i+1,len(board)),range(j+1,len(board))):
            if board[x][y]=='.':
                board_raichucopy = copy.deepcopy(board)
                board_raichucopy[x][y]='@'
                board_raichucopy[i][j]='.'
                raichu_boards.append(raichu_conversion(board_raichucopy,player,0))
            elif board[x][y] in capturable_pawns_w and x<len(board)-1 and y< len(board)-1 :
                if board[x+1][y+1]!='.':
                    break
                else:
                    board_raichucopy = copy.deepcopy(board)
                    board_raichucopy[x+1][y+1]='@'
                    board_raichucopy[i][j]='.'
                    board_raichucopy[x][y]='.'
                    if board[x][y] == '$':
                        raichu_boards.append(raichu_conversion(board_raichucopy,player,20))
                    elif board[x][y] == 'B':
                        raichu_boards.append(raichu_conversion(board_raichucopy,player,10))
                    else:
                        raichu_boards.append(raichu_conversion(board_raichucopy,player,5))
                    break
            else:
                break
                
    elif board[i][j]=='$' and player=='b':
        #Upper
        for x in range(i-1,-1,-1):
            if board[x][j]=='.':
                board_raichucopy = copy.deepcopy(board)
                board_raichucopy[x][j]='$'
                board_raichucopy[i][j]='.'
                raichu_boards.append(raichu_conversion(board_raichucopy,player,0))
            elif board[x][j] in capturable_pawns_b and x>0:
                if board[x-1][j]!='.':
                    break
                else:
                    board_raichucopy = copy.deepcopy(board)
                    board_raichucopy[x-1][j]='$'
                    board_raichucopy[i][j]='.'
                    board_raichucopy[x][j]='.'
                    if board[x][j] == '@':
                        raichu_boards.append(raichu_conversion(board_raichucopy,player,20))
                    elif board[x][j] == 'W':
                        raichu_boards.append(raichu_conversion(board_raichucopy,player,10))
                    else:
                        raichu_boards.append(raichu_conversion(board_raichucopy,player,5))
                    break
            else:
                break
        #Down
        for x in range(i+1,len(board)):
            if board[x][j]=='.':
                board_raichucopy = copy.deepcopy(board)
                board_raichucopy[x][j]='$'
                board_raichucopy[i][j]='.'
                raichu_boards.append(raichu_conversion(board_raichucopy,player,0))
            elif board[x][j] in capturable_pawns_b and x<len(board)-1:
                if board[x+1][j]!='.':
                    break
                else:
                    board_raichucopy = copy.deepcopy(board)
                    board_raichucopy[x+1][j]='$'
                    board_raichucopy[i][j]='.'
                    board_raichucopy[x][j]='.'
                    if board[x][j] == '@':
                        raichu_boards.append(raichu_conversion(board_raichucopy,player,20))
                    elif board[x][j] == 'W':
                        raichu_boards.append(raichu_conversion(board_raichucopy,player,10))
                    else:
                        raichu_boards.append(raichu_conversion(board_raichucopy,player,5))
                    break
            else:
                break
        #left
        for x in range(j-1,-1,-1):
            if board[i][x]=='.':
                board_raichucopy = copy.deepcopy(board)
                board_raichucopy[i][x]='$'
                board_raichucopy[i][j]='.'
                raichu_boards.append(raichu_conversion(board_raichucopy,player,0))
            elif board[i][x] in capturable_pawns_b and x>0 :
                if board[i][x-1]!='.':
                    break
                else:
                    board_raichucopy = copy.deepcopy(board)
                    board_raichucopy[i][x-1]='$'
                    board_raichucopy[i][j]='.'
                    board_raichucopy[i][x]='.'
                    if board[i][x] == '@':
                        raichu_boards.append(raichu_conversion(board_raichucopy,player,20))
                    elif board[i][x] == 'W':
                        raichu_boards.append(raichu_conversion(board_raichucopy,player,10))
                    else:
                        raichu_boards.append(raichu_conversion(board_raichucopy,player,5))
                    break
            else:
                break
        #Right
        for x in range(j+1,len(board)):
            if board[i][x]=='.':
                board_raichucopy = copy.deepcopy(board)
                board_raichucopy[i][x]='$'
                board_raichucopy[i][j]='.'
                raichu_boards.append(raichu_conversion(board_raichucopy,player,0))
            elif board[i][x] in capturable_pawns_b and x<len(board)-1:
                if board[i][x+1]!='.':
                    break
                else:
                    board_raichucopy = copy.deepcopy(board)
                    board_raichucopy[i][x+1]='$'
                    board_raichucopy[i][j]='.'
                    board_raichucopy[i][x]='.'
                    if board[i][x] == '@':
                        raichu_boards.append(raichu_conversion(board_raichucopy,player,20))
                    elif board[i][x] == 'W':
                        raichu_boards.append(raichu_conversion(board_raichucopy,player,10))
                    else:
                        raichu_boards.append(raichu_conversion(board_raichucopy,player,5))
                    break
            else:
                break
        #RightUpperDiag
        for (x,y) in zip(range(i-1,-1,-1),range(j+1,len(board))):
            if board[x][y]=='.':
                board_raichucopy = copy.deepcopy(board)
                board_raichucopy[x][y]='$'
                board_raichucopy[i][j]='.'
                raichu_boards.append(raichu_conversion(board_raichucopy,player,0))
            elif board[x][y] in capturable_pawns_b and x>0 and y<len(board)-1:
                if board[x-1][y+1]!='.':
                    break
                else:
                    board_raichucopy = copy.deepcopy(board)
                    board_raichucopy[x-1][y+1]='$'
                    board_raichucopy[i][j]='.'
                    board_raichucopy[x][y]='.'
                    if board[x][y] == '@':
                        raichu_boards.append(raichu_conversion(board_raichucopy,player,20))
                    elif board[x][y] == 'W':
                        raichu_boards.append(raichu_conversion(board_raichucopy,player,10))
                    else:
                        raichu_boards.append(raichu_conversion(board_raichucopy,player,5))
                    break
            else:
                break
                    
        #LeftDownDiag
        for (x,y) in zip(range(i+1,len(board)),range(j-1,-1,-1)):
            if board[x][y]=='.':
                board_raichucopy = copy.deepcopy(board)
                board_raichucopy[x][y]='$'
                board_raichucopy[i][j]='.'
                raichu_boards.append(raichu_conversion(board_raichucopy,player,0))
            elif (board[x][y] in capturable_pawns_b) and x<len(board)-1 and y>0:
                if board[x+1][y-1]!='.':
                    break
                else:
                    board_raichucopy = copy.deepcopy(board)
                    board_raichucopy[x+1][y-1]='$'
                    board_raichucopy[i][j]='.'
                    board_raichucopy[x][y]='.'
                    if board[x][y] == '@':
                        raichu_boards.append(raichu_conversion(board_raichucopy,player,20))
                    elif board[x][y] == 'W':
                        raichu_boards.append(raichu_conversion(board_raichucopy,player,10))
                    else:
                        raichu_boards.append(raichu_conversion(board_raichucopy,player,5))
                    break
            else:
                break
            
        #LeftUpperDiag
        for (x,y) in zip(range(i-1,-1,-1),range(j-1,-1,-1)):
            if board[x][y]=='.':
                board_raichucopy = copy.deepcopy(board)
                board_raichucopy[x][y]='$'
                board_raichucopy[i][j]='.'
                raichu_boards.append(raichu_conversion(board_raichucopy,player,0))
            elif board[x][y] in capturable_pawns_b and  x>0 and y>0:
                if board[x-1][y-1]!='.':
                    break
                else:
                    board_raichucopy = copy.deepcopy(board)
                    board_raichucopy[x-1][y-1]='$'
                    board_raichucopy[i][j]='.'
                    board_raichucopy[x][y]='.'
                    if board[x][y] == '@':
                        raichu_boards.append(raichu_conversion(board_raichucopy,player,20))
                    elif board[x][y] == 'W':
                        raichu_boards.append(raichu_conversion(board_raichucopy,player,10))
                    else:
                        raichu_boards.append(raichu_conversion(board_raichucopy,player,5))
                    break
            else:
                break
        #RightDownDiag
        for (x,y) in zip(range(i+1,len(board)),range(j+1,len(board))):
            if board[x][y]=='.':
                board_raichucopy = copy.deepcopy(board)
                board_raichucopy[x][y]='$'
                board_raichucopy[i][j]='.'
                raichu_boards.append(raichu_conversion(board_raichucopy,player,0))
            elif board[x][y] in capturable_pawns_b and x<len(board)-1 and y<len(board)-1:
                if board[x+1][y+1]!='.':
                    break
                else:
                    board_raichucopy = copy.deepcopy(board)
                    board_raichucopy[x+1][y+1]='$'
                    board_raichucopy[i][j]='.'
                    board_raichucopy[x][y]='.'
                    if board[x][y] == '@':
                        raichu_boards.append(raichu_conversion(board_raichucopy,player,20))
                    elif board[x][y] == 'W':
                        raichu_boards.append(raichu_conversion(board_raichucopy,player,10))
                    else:
                        raichu_boards.append(raichu_conversion(board_raichucopy,player,5))
                    break
            else:
                break
                    
    return raichu_boards

# Returns the score of a particular board
def eval(board,player,kill):
    w_score = 0
    b_score =0
    W_score = 0
    B_score = 0
    Rw_score = 0
    Rb_score = 0
    for i in range(len(board[0])):
        for j in range(len(board[0])):
            if board[i][j]=='w':
                w_score+=1
            elif board[i][j]=='W':
                W_score+=2
            elif board[i][j]=='@':
                Rw_score+=3
            elif board[i][j]=='b':
                b_score+=1
            elif board[i][j]=='B':
                B_score+=2
            elif board[i][j]=='$':
                Rb_score+=3
    


    res1= (w_score-b_score)+1
    res2= (W_score-B_score)+3
    res3 = (Rw_score-Rb_score)+5
    if kill:
     result=(res1+res2+res3)*kill*40
    else:
     result=(res1+res2+res3)*20
    if player=='w':
       return result
    else:
        return -result

#Returns if the end state is found or not
def end_state(board):
    w_score = 0
    b_score =0
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j]=='w' or board[i][j]=='W' or board[i][j]=='@':
                w_score += 1
            if board[i][j]=='b' or board[i][j]=='B'or board[i][j]=='$':
                b_score += 1
    if w_score == 0 or b_score == 0:
        return True
    else:
        return False

# Citation: https://www.youtube.com/watch?v=zp3VMe0Jpf8 
# Implemented the below alphabeta pruning and minimax from the above video
def alphabetaPruning(alpha,beta,board,player,main_player,level):
    res = None
    for successormove,score in sorted(moves(board,player),key=lambda ele:(ele[1],ele[0])):
        min=minimumfunc(successormove,alpha,beta,level-1,player, main_player)
        if min>score:
            score=min
            res = successormove
    if res != None:
        res = ''.join([''.join(x) for x in res])
    return res
        
def minimumfunc(board,alpha,beta,level,player, main_player):
    if level==0 or end_state(board):
       return eval(board,main_player,beta)

    minn=888889999
    player = 'b' if player == 'w' else 'w'

    for successormove,score in sorted(moves(board,player),key=lambda ele:(-ele[1],ele[0])):
        maxx=maximumfunc(successormove,alpha,beta,level-1,player, main_player)
        maxx = max(minn,alpha)
        if maxx<beta:
            beta=maxx
        return maxx

    return minn

def maximumfunc(board,alpha,beta,level,player, main_player):
    if level==0 or end_state(board):
       return eval(board,main_player,alpha)
    localmaximum=-999999999999
    player = 'b' if player == 'w' else 'w'

    for succ,score in sorted(moves(board,player),key=lambda ele:(ele[1],ele[0])):
        min=minimumfunc(succ,alpha,beta,level-1,player, main_player)
        localmaximum=max(min,localmaximum)
        if min>=beta:
            return localmaximum
        alpha=max(min,alpha)
    return localmaximum

###-------------------------------------------------###

def find_best_move(board, N, player, timelimit):
    # This sample code just returns the same board over and over again (which
    # isn't a valid move anyway.) Replace this with your code!
    #
    # return moves(board,player)
    main_player=player
    level = 2
    while timelimit > 0:
        start = time.time()
        new_board = alphabetaPruning(-999999999999,8888888888888,board,player, main_player, level)
        level += 2
        timelimit -= (time.time()-start)
        yield new_board


if __name__ == "__main__":
    if len(sys.argv) != 5:
        raise Exception("Usage: Raichu.py N player board timelimit")
        
    (_, N, player, board, timelimit) = sys.argv
    N=int(N)
    timelimit=int(timelimit)
    if player not in "wb":
        raise Exception("Invalid player.")

    if len(board) != N*N or 0 in [c in "wb.WB@$" for c in board]:
        raise Exception("Bad board string.")

    print("Searching for best move for " + player + " from board state: \n" + board_to_string(board, N))
    print("Here's what I decided:")

    #cite https://www.geeksforgeeks.org/convert-a-string-into-a-square-matrix-grid-of-characters:
    #string to matric conversion 
    board_matrix=[]
    for i in range(0,N*N,N):
        boardlist = []
        str = board[i:i+N]
        for k in str:
            boardlist.append(k)
        board_matrix.append(boardlist)

    for new_board in find_best_move(board_matrix, N, player, timelimit):
        print(new_board)
