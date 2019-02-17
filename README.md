# Tic Tac Toe (Game) - Python 3

<p> Tic Tac Toe game It's a game for two people </p>

        [1][2][3]             [x][0][x]      
        [4][5][6]   ---->     [0][x][0] 
        [7][8][9]             [x][0][x]

# Game stages

1. The first player chooses to be x or 0 , The second   player is affected by the choice of the first player .
2.  The first player selecting a number between 1-8 to marks the board by x or 0 .
3. Now it's the turn of the second player .

4. The game continues until one of the players wins Or there will be a draw between the players .

5. The game asked if players would want to play another game , if "yes" Go back to step 1 , Other go to step 6 .

6. The program prints out that the game is over

# Victory options

<p>Players can win if they get one of the following sequences </p>

<p>We selected -X for example</p>

    [x][ ][ ]     [ ][x][ ]    [ ][ ][x] 
    [x][ ][ ]     [ ][x][ ]    [ ][ ][x]
    [x][ ][ ]  ,  [ ][x][ ] ,  [ ][ ][x]

    [x][x][x]     [ ][ ][ ]    [ ][ ][ ]
    [ ][ ][ ]     [x][x][x]    [ ][ ][ ]
    [ ][ ][ ]  ,  [ ][ ][ ] ,  [x][x][x]

    [ ][ ][x]     [x][ ][ ]    
    [ ][x][ ]     [ ][x][ ]    
    [x][ ][ ]  ,  [ ][ ][x]  

<p>If the board is full and there are no winners ,Then there is a draw between the players .</p>

# Simulation of a program run
         
    Welcome to Tic Tac Toe Game
    
    - - - - - - -  
    | 1 | 2 | 3 |
    - - - - - - -  
    | 4 | 5 | 6 |
    - - - - - - -  
    | 7 | 8 | 9 |
    - - - - - - -  
    Please pick a marker 'x' or 'O' :
    x
    player 1 Please make your move typing in the number you want place your item  
    1
    - - - - - - -  
    | x | 2 | 3 |
    - - - - - - -  
    | 4 | 5 | 6 |
    - - - - - - -  
    | 7 | 8 | 9 |
    - - - - - - -  
    player 2 Please make your move typing in the number you want place your item  
    5
    - - - - - - -  
    | x | 2 | 3 |
    - - - - - - -  
    | 4 | 0 | 6 |
    - - - - - - -  
    | 7 | 8 | 9 |
    - - - - - - -  
    player 1 Please make your move typing in the number you want place your item  
    2
    - - - - - - -  
    | x | x | 3 |
    - - - - - - -  
    | 4 | 0 | 6 |
    - - - - - - -  
    | 7 | 8 | 9 |
    - - - - - - -  
    player 2 Please make your move typing in the number you want place your item  
    8
    - - - - - - -  
    | x | x | 3 |
    - - - - - - -  
    | 4 | 0 | 6 |
    - - - - - - -  
    | 7 | 0 | 9 |
    - - - - - - -  
    player 1 Please make your move typing in the number you want place your item  
    3
    - - - - - - -  
    | x | x | x |
    - - - - - - -  
    | 4 | 0 | 6 |
    - - - - - - -  
    | 7 | 0 | 9 |
    - - - - - - -  
    ---------------
    player 1 is win
    ---------------

    You want to start a new game 'yes'/'no
    no

    - Game Over -
    -------------


 
          
