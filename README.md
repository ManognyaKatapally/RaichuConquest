# Raichu Conquest

### Problem Statement
In a two player game on NxN board, for any player, Best optimal move must be returned at a given state of game

### Approach:
Implemented a successor function which returns all the possible moves for a given player and by using minmax algorithm we find the chances of a player winning by minimising the opposite player's winning chances.  We have used iterative deepening search to search the tree at different depts.
Every successor will be sent to minimum function where it calls maximum function recursively and therefore depth keeps increasing. If the depth reaches the limit mentioned, Evaluator is used to evaluate the score of board and returns it.
In the available time, we keep yielding the best possible moves found till then.

#### Successor function:
This generates all the possible moves of pichus, pikachus and raichus with the respective board score calculated for a given player.
 
#### Score evaluation:
Calculates the score by considering the number of whites and black players, their added weights and the kills a player can make.
 
#### Goal State:
Goal state of board is when one the player is out of the game(i.e when all the  pieces of a player gets captured).
 
Referenced the below video and Implemented alphabeta pruning<br>
Citation: https://www.youtube.com/watch?v=zp3VMe0Jpf8 


