# 201307211 Szafarczyk_Robert-CA05.py
# 11/17
# This is a hangman game. The user selects a category and from this category
# (a list) a random word is selected. User is informed how many letters the
# word has and that's how many tries to guess the word the user has.
# Repetitions do not count as a guess, invalid input does not count as a
# guess (e.g. 'ae'). Non-letters do count as a guess, strings with the same
# length as the word do count as a guess. The user is presented with a
# string with of underscores. Each underscore represents each letter from
# word. If a letter is guessed correctly the underscore is changed to this
# letter. If user has used up his guesses, then the program prints out the
# correctly and incorrectly guessed letters. Based on this information the
# user has to guess the whole word. After this guess the game ends.


def main():
    import random
    import sys

    def option_Exit():
        print()
        print()
        print("Goodbye!")
        sys.exit()


    def hangman():

        animal_list = ['lion', 'bat', 'anaconda', 'salmon', 'whale',
                       'grasshopper', 'aligator', 'rat', 'bear',
                       'frog',
                       'elephant', 'cat', 'dog', 'giraffe', 'eagle',
                       'lizard', 'earthworm', 'tiger', 'dolphin',
                       'mouse',
                       'owl', 'horse', 'donkey', 'antelope', 'cobra',
                       'duck', 'emu', 'fox', 'jaguar']
        fruit_list = ['apple', 'banana', 'strawberry', 'blackberry',
                      'orange', 'grapefruit', 'mango', 'peach',
                      'lime', 'cherry', 'date', 'pineapple', 'papaya',
                      'raspberry', 'honeyberry', 'tangerine',
                      'coconut', 'nectarine', 'passionfruit', 'plum',
                      'watermelon', 'currant']
        country_list = ['England', 'Poland', 'Germany', 'Brazil',
                        'Portugal', 'France', 'Australia', 'China',
                        'Japan',
                        'India', 'Canada', 'Egypt', 'Argentina', 'Russia',
                        'Austria', 'Spain', 'Columbia',
                        'Chechia',
                        'Hungary', 'Denmark', 'Italy', 'Ireland', 'Turkey',
                        'Afghanistan', 'Iraq', 'Mongolia',
                        'Thailand', 'Chile', 'Peru', 'Kenya', 'Algeria',
                        'Ghana']
        city_list_UK = ['Liverpool', 'Manchester', 'London', 'Plymouth',
                        'Newcastle', 'Lancaster', 'Birmingham',
                        'Leeds',
                        'Sheffield', 'Chester', 'Swansea', 'Oxford',
                        'Edinburgh', 'Glasgow', 'Colchester',
                        'Norwich',
                        'Exeter', 'Brighton', 'York', 'Cardiff',
                        'Aberdeen', ]

        def random_word(category):
            return random.choice(category).upper()

        def check_letter(guess, word, all_guessed):

            # this string will be the output to the user
            word_with_underscores = ""
            num_of_matched_letters = 0

            # loops through every letter in word
            # checks if letter from word is in list with all our guesses
            for letter in word:
                # ads letter in place of the letter in word
                if letter in all_guessed:
                    word_with_underscores += " " + letter + " "
                # ads underscore in place of letter
                else:
                    word_with_underscores += " _ "

                # counts how many times our guess occurs in word
                if letter == guess:
                    num_of_matched_letters += 1

            if num_of_matched_letters > 1:
                print()
                print("Correct! The word contains {} letters {}".
                      format(num_of_matched_letters, guess))
                print()
            elif num_of_matched_letters == 1:
                print()
                print("Correct! The word contains the letter {}".
                      format(guess))
                print()
            else:
                print()
                print("Sorry. The letter {} is not in the word".
                      format(guess))
                print()

            return word_with_underscores


        print()
        print()
        print("Welcome to hangman!")
        print()
        print("Categories of words:")
        print()
        print("A. Animals")
        print("B. Fruits")
        print("C. Countries")
        print("D. Cities in the UK")
        print()
        category = input("Select category A,B,C or D: ")
        category = category.upper()

        while category not in ("A", "B", "C", "D"):
            print()
            print("Wrong input!")
            category = input("Select category A,B,C or D: ")
            category = category.upper()

        # selecting random word from chosen category list
        if category == "A":
            word = random_word(animal_list)
            word_info = "Category: animals\n" \
                            "The word has {} letters".format(len(word))
        elif category == "B":
            word = random_word(fruit_list)
            word_info = "Category: fruits\n" \
                        "The word has {} letters".format(len(word))
        elif category == "C":
            word = random_word(country_list)
            word_info = "Category: country\n" \
                        "The word has {} letters".format(len(word))
        elif category == "D":
            word = random_word(city_list_UK)
            word_info = "Category: cities\n" \
                        "The word has {} letters".format(len(word))


        # initialising variables
        num_of_guesses = len(word)

        # seperate list for all guessed letters,
        # correct guessed and incorrect guessed
        # converting from list to set and back to remove repetitions
        all_guessed = []
        correct_guessed = []
        correct_guessed_distinct = list(set(correct_guessed))
        incorrect_guessed = []
        incorrect_guessed_distinct = list(set(incorrect_guessed))

        guess = ""
        # boolean variable for our while loop
        guessed = False

        print()
        print("Let's start!")
        print()
        print(word_info)
        print("You have {} guesses to guess the word.".format(len(word)))


        while guessed is False:
            if num_of_guesses > 0:
                print()
                guess = input("Guess a letter or the whole word: ")
                print()
                guess = guess.upper()

                # informing user if he guessed the letter already.
                # Does not count as guess
                if guess in all_guessed:
                    print("You already guessed {}".format(guess))
                    print("You still have {} guesses left".
                          format(num_of_guesses))
                    print()
                    print(word_info)
                    print()
                    print(word_after_guess)

                # user tries to guess whole word
                elif len(guess) == len(word):
                    if guess == word:
                        if num_of_guesses == len(word):
                            print("Congratulations! You guessed the word "
                                  "on your first try!")
                            guessed = True
                        else:
                            num_of_guesses -= 1
                            print("Congratulations! "
                                  "You guessed the word in {} tries".
                                  format(len(word) - num_of_guesses))
                            guessed = True

                    else:
                        num_of_guesses -= 1
                        print()
                        print("Sorry, this is not the word")
                        print()
                        print(word_info)
                        print()
                        print("You have {} guesses left".
                              format(num_of_guesses))

                # user guesses 1 letter
                elif len(guess) == 1:
                    if guess.isalpha():
                        num_of_guesses -= 1
                        # this list contains all alpha guesses
                        all_guessed.append(guess)

                        # function to check if guess in word
                        word_after_guess = check_letter(guess, word,
                                                        all_guessed)
                        if word_after_guess == word:
                            print("Congratulations! "
                                  "You guessed the word in {} tries".
                                  format(len(word) - num_of_guesses))
                            guessed = True

                        else:
                            print(word_after_guess)
                            print()
                            print(word_info)
                            print()
                            if num_of_guesses > 1:
                                print("You have {} guesses left".format
                                      (num_of_guesses))
                            if num_of_guesses == 1:
                                print("You have 1 guess left.")
                            print()

                            if guess in word_after_guess:
                                correct_guessed_distinct.append(guess)
                            else:
                                incorrect_guessed_distinct.append(guess)

                    # case where user's guess isn't a letter.
                    # Does count as guess
                    else:
                        num_of_guesses -= 1
                        word_after_guess = check_letter(guess, word,
                                                        all_guessed)
                        print()
                        print("Hint: words only contain letters")
                        print()
                        print(word_after_guess)
                        print()
                        print(word_info)
                        print()
                        if num_of_guesses > 1:
                            print("You have {} guesses left".
                                  format(num_of_guesses))
                        if num_of_guesses == 1:
                            print("You have 1 guess left.")
                        print()

                # if user's guess isn't a letter or the whole word
                else:
                    print()
                    print("Invalid entry.")
                    print()
                    print(word_after_guess)
                    print()
                    print(word_info)
                    print()
                    print("You have {} guesses left".
                          format(num_of_guesses))
                    print()

            # last guess. We output the correct and incorrect guesses
            elif num_of_guesses == 0:
                print("No guesses left!")
                print()
                print("Guess the word based on this information:")
                print("Correct guessed letters: {}".
                      format(", ".join(correct_guessed_distinct)))
                print("Incorrect guessed letters: {}".
                      format(", ".join(incorrect_guessed_distinct)))
                print()

                guess = input("Guess the word: ")
                guess = guess.upper()

                if guess == word:
                    print()
                    print("Congratulations! "
                          "You guessed the word on your last try")
                    guessed = True
                else:
                    print()
                    print()
                    print("Game over! The word was {}".format(word))
                    print()
                    if len(correct_guessed_distinct) != 1:
                        print("You have guessed {} letters correctly: {}".
                              format(len(correct_guessed_distinct),
                                     ", ".join(correct_guessed_distinct)))
                    else:
                        print("You have guessed 1 letter correctly: {}".
                              format(", ".join(correct_guessed_distinct)))

                    if len(incorrect_guessed_distinct) != 1:
                        print("You have guessed {} letters incorrectly: "
                              "{}".format(len(incorrect_guessed_distinct),
                                     ", ".
                                     join(incorrect_guessed_distinct)))
                    else:
                        print("You have guessed 1 letter incorrectly: {}".
                              format(", ".
                                     join(incorrect_guessed_distinct)))
                    guessed = True

            # user didn't guess the word
            else:
                print()
                print()
                print("Game over! The word was {}".format(word))
                print()
                if len(correct_guessed_distinct) != 1:
                    print("You have guessed {} letters correctly: {}".
                          format(len(correct_guessed_distinct),
                                 ", ".join(correct_guessed_distinct)))
                else:
                    print("You have guessed 1 letter correctly: {}".
                          format(", ".join(correct_guessed_distinct)))

                if len(incorrect_guessed_distinct) != 1:
                    print("You have guessed {} letters incorrectly: {}".
                          format(len(incorrect_guessed_distinct),
                                 ", ".join(incorrect_guessed_distinct)))
                else:
                    print("You have guessed 1 letter incorrectly: {}".
                          format(", ".join(incorrect_guessed_distinct)))

                guessed = True


        # hangman()

        option_end = ""

        while option_end != "NO" or option_end != "N":
            print()
            print()
            print()
            print()
            option_end = input("Play again? (yes/no): ")
            option_end = option_end.upper()

            while option_end not in ("NO", "YES", "N", "Y"):
                print()
                print("Invalid input")
                option_end = input("Play again? (yes/no): ")
                option_end = option_end.upper()

            if option_end == "YES" or option_end == "Y":
                hangman()
            else:
                option_Exit()



    ##################################################################
    # START HERE

    option = ""

    while option != "NO" or option != "N":
        print()
        print()
        print("Hangman Game")
        print()
        print()
        option = input("Play? (yes/no): ")
        option = option.upper()

        while option not in ("NO", "YES", "Y", "N"):
            print()
            print("Invalid input")
            print()
            option = input("Play? (yes/no): ")
            option = option.upper()

        if option == "YES" or option == "Y":
            hangman()

        elif option == "NO" or option == "N":
            option_Exit()



main()
