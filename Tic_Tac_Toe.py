'''
  Tic Tac Toe Game .
  [1][2][3]
  [4][5][6]
  [7][8][9]
  The game gets two arrays  One for printing and the Other for 
  Check which place you can insert 'x' or '0' [1,2......9]
  The second array is small and small in one Until lea() = 0 = []
  This means that there is no more space available in arr It means There are no winners
  else In some iteration there is a winner and he prints who win.

  *python Tic_Tac_Toe

'''
import os  # for os.system()


# The function checks that the player selects between 'X' and '0'
def Not_good_choice():
    while (True):
        print("Please pick a marker 'x' or 'O':")
        choice = input()
        if choice == "x" or choice == 0:
            return choice


# The function checks whether a player has entered an incorrect selection or the Place is not available
def Not_good_num(board_begin):
    while (True):
        print(
            "Please choose a place from the numbers Who remained on the board")
        choice = input()
        if choice in board_begin:
            return choice


#Print a game to the screen after each iteration
def place_marker(board, marker, position):
    board[position - 1] = marker
    print("- - - - - - -  ")
    print("| {} | {} | {} |".format(board[0], board[1], board[2]))
    print("- - - - - - -  ")
    print("| {} | {} | {} |".format(board[3], board[4], board[5]))
    print("- - - - - - -  ")
    print("| {} | {} | {} |".format(board[6], board[7], board[8]))
    print("- - - - - - -  ")
    return board


# The function checks for a winner
def player_win(game_board):

    if game_board[0] == game_board[1] and game_board[1] == game_board[2]:
        return True
    elif game_board[3] == game_board[4] and game_board[4] == game_board[5]:
        return True
    elif game_board[6] == game_board[7] and game_board[7] == game_board[8]:
        return True

    elif game_board[0] == game_board[3] and game_board[3] == game_board[6]:
        return True
    elif game_board[1] == game_board[4] and game_board[4] == game_board[7]:
        return True
    elif game_board[2] == game_board[5] and game_board[5] == game_board[8]:
        return True

    elif game_board[0] == game_board[4] and game_board[4] == game_board[8]:
        return True
    elif game_board[2] == game_board[4] and game_board[4] == game_board[6]:
        return True
    else:  # no winner
        return False


# Tic Tac Toe Game ( skeleton )
def game():
    replay = "yes"  # default for loop 1
    while (replay != "no"):  # loop 1
        print_game = "There are no winners"  # Screen prints  default
        indx = 0  # Indx for Removing a member of the second array
        we_have_a_winners = False
        board_begin = [1, 2, 3, 4, 5, 6, 7, 8,
                       9]  # The second array for testing Free space
        game_board = [1, 2, 3, 4, 5, 6, 7, 8, 9]  # Board for printing
        player2 = 0  # default for player 2
        board_begin = place_marker(board_begin, 1,
                                   1)  # display_board(board_begin)
        print("Please pick a marker 'x' or 'O' :")
        player1 = input()
        if player1 != "x" and player1 != '0':
            player1 = Not_good_choice()

        if player1 == "x":
            player2 = 0
        else:
            player2 = "x"

        while (len(board_begin) !=
               0):  # loop 2 ,if arr 2 is null break (There are no winners)
            print(
                "player 1 Please make your move typing in the number you want place your item  "
            )
            position = int(input())
            if position not in board_begin:
                position = Not_good_num(board_begin)

            game_board = place_marker(game_board, player1,
                                      position)  # Update the array 1
            indx = board_begin.index(
                position
            )  # Searches for the index of the number to be deleted from the array
            board_begin.pop(indx)  # Length arr_2 - 1 According to the index

            we_have_a_winners = player_win(game_board)  # True / False
            if we_have_a_winners == True:
                print_game = "player 1 is win"  # Update print
                break

            if (
                    len(board_begin) == 0
            ):  # if arr 2 is null , break (There are no winners) Because the array is uneven
                break

            print(
                "player 2 Please make your move typing in the number you want place your item  "
            )
            position = input()
            if position not in board_begin:
                position = Not_good_num(board_begin)

            game_board = place_marker(game_board, player2,
                                      position)  # Update the array 1
            indx = board_begin.index(
                position
            )  # Searches for the index of the number to be deleted from the array
            board_begin.pop(indx)  # Length arr_2 - 1 According to the index

            we_have_a_winners = player_win(game_board)  # True / False
            if we_have_a_winners == True:
                print_game = "player 2 is win"  # Update print
                break

        print("---------------")
        print("{}").format(print_game)
        print("---------------")
        print("You want to start a new game 'yes'/'no' ")
        replay = input()

        # clear the screen in python
        if os.name == 'nt':
            os.system('cls')  # on windows
        else:
            os.system('clear')  # on linux / os x

    print("-------------")
    print("- Game Over -")
    print("-------------")


# main game
if __name__ == "__main__":
    game()
