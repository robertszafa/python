# Mini go game using 2 dimensional arrays
# Extended Requirements: playing against the computer
# and a computer simulation of the game


def main():
    def option_x():
        print()
        print()
        print("Goodbye!")


    def game(game_option):

        import math
        from random import choice

        def print_matrix(matrix):
            print()
            for row in matrix:
                for item in row:
                    print(item, end=" ")
                print()
            print()

        def move(num, board, positions, is_comp1, is_comp2):

            # Converting into row and column from the 5x5 array
            def get_row_col(pos):
                # Function ceil rounds up the result of division.
                row = int(math.ceil(pos / 5)) - 1
                # The remainder from the division of pos-1 gives us the
                # column
                col = (pos - 1) % 5
                return row, col

            def check_won(row, col, board):
                # There are 4 cases of the pos input being wining
                # The input has to be one of the items in a 2x2 array
                if row != 4 and col != 4:
                    if board[row][col] == board[row][col + 1] \
                            == board[row + 1][col] \
                            == board[row + 1][col + 1]:
                        return True

                if row != 4 and col != 0:
                    if board[row][col] == board[row][col - 1] \
                            == board[row + 1][col] \
                            == board[row + 1][col - 1]:
                        return True

                if row != 0 and col != 4:
                    if board[row][col] == board[row][col + 1] \
                            == board[row - 1][col] \
                            == board[row - 1][col + 1]:
                        return True

                if row != 0 and col != 0:
                    if board[row][col] == board[row][col - 1] \
                            == board[row - 1][col] \
                            == board[row - 1][col - 1]:
                        return True

            # EXTENDED
            def computer(positions, board, num1):
                won_p1 = False
                won_p2 = False
                item = 0

                if num1 == 1:
                    num2 = 2
                elif num1 == 2:
                    num2 = 1

                while item <= len(positions) and not won_p1 and not won_p2:
                    p_input = positions[item - 1]
                    row, col = get_row_col(p_input)

                    # The algorithm would also work without specifying
                    # player num, but it then wouldn't care if to select
                    # a position that wins or a position that prevents
                    # the wining of the opponent
                    board[row][col] = num1
                    won_p1 = check_won(row, col, board)

                    # If winning position is found, then it's returned.
                    # If not, check if it would be winning
                    # for other player. If yes, change it to 1
                    if not won_p1:
                        board[row][col] = num2
                        won_p2 = check_won(row, col, board)
                        if won_p2:
                            board[row][col] = num1
                        else:
                            board[row][col] = 0
                    item += 1

                if not won_p1 and not won_p2:
                    # This doesn't improve the algorithm, but gives a
                    # more user friendly experience
                    p_input = choice(positions)

                return p_input

            def output(is_comp1, is_comp2, num, board, p_input, won, draw):
                if won:
                    if (not is_comp1 and not is_comp2) \
                            or (not is_comp1 and is_comp2):
                        print()
                        print("Player {} played position {}".
                              format(num, p_input))
                        print("This is the final board")
                        print_matrix(board)
                        print("Congratulations Player {}! You won!".
                              format(num))
                    elif is_comp1 and not is_comp2:
                        print()
                        print("Computer played position {}".
                              format(p_input))
                        print("This is the final board")
                        print_matrix(board)
                        print("Game over! You lost.")
                    else:
                        print()
                        print("Player {} played position {}".
                              format(num, p_input))
                        print("This is the final board")
                        print_matrix(board)
                        print("Player {} won!".format(num))

                elif draw:
                    print()
                    print("Player {} played position {}".
                          format(num, p_input))
                    print("This is the final board")
                    print_matrix(board)
                    print("Game over. Draw!")

                else:
                    if is_comp1 and not is_comp2:
                        print()
                        print("Computer played position {}".
                              format(p_input))
                    else:
                        print()
                        print("Player {} played position {}".
                              format(num, p_input))
                    print_matrix(board)

            won = False
            draw = False
            finished = False

            if not is_comp1:
                print()
                p_input = input(
                    "Player {}, select position to play: ".format(num))
                while not p_input.isnumeric():
                    print()
                    print("Invalid input!")
                    p_input = input(
                        "Player {}, select position to play: ".format(num))
                p_input = int(p_input)
            else:
                p_input = computer(positions, board, num)

            while p_input not in positions:
                if p_input not in list(range(1, 26)):
                    print()
                    print("You can only choose squares from 1 to 25")
                else:
                    print()
                    print("This square is occupied")

                p_input = input(
                    "Player {}, select position to play: ".format(num))

                while not p_input.isnumeric():
                    print()
                    print("Invalid input!")
                    p_input = input(
                        "Player {}, select position to play: ".format(num))
                p_input = int(p_input)

            row, col = get_row_col(p_input)
            board[row][col] = num
            won = check_won(row, col, board)
            positions.remove(p_input)
            if len(positions) == 0:
                draw = True

            if won or draw:
                finished = True

            output(is_comp1, is_comp2, num, board, p_input, won, draw)

            return board, positions, finished

        # Initialise
        board = [[0 for row in range(5)] for col in range(5)]
        positions = list(range(1, 26))
        round_nr = 1
        is_comp1 = False
        is_comp2 = False
        finished = False

        # EXTENDED
        if game_option == "A":
            is_comp2 = True
            is_comp1 = False
        elif game_option == "B":
            is_comp2 = True
            is_comp1 = True
        elif game_option == "C":
            is_comp2 = False
            is_comp1 = False

        if not is_comp1 or not is_comp2:
            print()
            print("Obtain a 2x2 square to win")
            print()
            print("This is the board")
            print_matrix(board)

        while not finished:
            print()
            print("Round {}".format(round_nr))

            # both is_comp1 and is_comp2 go onto the move() function to
            # assure output according to selected option

            # Player 1 (is_comp1)
            board, positions, finished = move(1, board, positions,
                                              is_comp1, is_comp2)
            if finished:
                continue

            # Player 2 (is_comp2)
            board, positions, finished = move(2, board, positions,
                                              is_comp2, is_comp1)
            if finished:
                continue

            print()
            round_nr += 1

    game_option = ""
    while game_option != "X":
        print()
        print()
        print("Mini Go game")
        print()
        print("A. Play against the computer")
        print("B. See two computers play")
        print("C. Multiplayer")
        print("X. Exit")
        print()
        game_option = input("Enter option A,B,C or X: ")
        game_option = game_option.upper()

        while game_option not in ("A", "B", "C", "X"):
            print()
            print("Invalid input!")
            game_option = input("Enter option A,B or C: ")
            game_option = game_option.upper()

        if game_option == "X":
            option_x()
            pass
        else:
            game(game_option)


main()
