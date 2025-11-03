import WGLib
import random # to set the random seed

'''
def validate(player_word, words, used_words, required_length, start_letter):
    """
       Validates whether a player's word input meets all game requirements.

       Checks if the word: exists in the dictionary, hasn't been used before,
       has the correct length, and starts with the required letter.

       :param player_word: The word entered by the player
       :param words: List of valid words from the dictionary
       :param used_words: Set of words already used in this game
       :param required_length: The required length for the current word
       :param start_letter: The letter the word must start with
       :returns: True if the word is valid, False otherwise
       """
    if player_word not in words:
        return False
    if player_word in used_words:
        return False
    if len(player_word) != required_length:
        return False
    if player_word[0] != start_letter:
        return False
    return True


def promptPlayAgain():
    """
    :param choice: Prompts the player to play again and returns their choice.
    :returns: True if player wants to play again, False otherwise
    """
    while True:
        choice = input("Would you like to play again? (y/n): ").lower().strip()
        if choice == 'y':
            print("Great! Starting a new game...")
            return True
        elif choice == 'n':
            print("Thanks for playing!")
            return False
        else:
            print("Invalid input. Please enter 'y' or 'n'.")
'''
def howManyRounds():
    while True:
        choice = input("How many rounds do you want to play? (1 or 3): ").strip()
        if choice == '1':
            print("Great! Starting 1 round...")
            return 1
        elif choice == '3':
            print("Great! Starting 3 rounds...")
            return 3
        else:
            print("Invalid input. Please enter 1 or 3.")

def playGame(words):
    """
    This function sets up the game, runs each round/turn, then returns a non-negative
        integer representing the player's score.

    :param words: A list of strings, each string containing exactly one word composed of letters of the Latin alphabet (a-z).
    :returns: The player's score at the end of a game. If the game has only two conclusions, win or lose, consider 0 for lose and 1 for win.
    """
    current_score = 0
    required_length = 3
    start_letter = random.choice("abcdefghijklmnopqrstuvwxyz")
    regenerations_left = 3
    used_words = set()

    print(start_letter)

    while required_length <= 10 and regenerations_left > 0 :
        print("Next word must: start with " + start_letter + " and be " + str(required_length) + " letters long")
        print("Current score:" + str(current_score))
        player_word = input("Enter your word (or 'regenerate' to get a new starting letter): ").lower().strip()

        if player_word == "regenerate":
            regenerations_left -= 1
            required_length = 3
            start_letter = random.choice("abcdefghijklmnopqrstuvwxyz")
            print("Regenerating..." + str(regenerations_left))
            continue

        is_valid = WGLib.validate(player_word, words, used_words, required_length,
                              start_letter)

        if is_valid:
            current_score += WGLib.processValidInput(player_word, words,
                                                     current_score)
            start_letter = player_word[-1]
            used_words.add(player_word)
            required_length += 1
            print(f"Valid! +{len(player_word)} points. Total: {current_score}")
            print(WGLib.createDisplayString(player_word, used_words, current_score,
                                            3 - regenerations_left))
        else:
            print(f"Try again! + 0 points. Total: {current_score}")
            print(WGLib.createDisplayString(player_word, used_words, current_score,
                                            3 - regenerations_left))

        if required_length > 10:
            print("Chain complete! Auto-regenerating...")
            regenerations_left -= 1
            required_length = 3
            start_letter = random.choice("abcdefghijklmnopqrstuvwxyz")
    print("\nGame Over!")
    return current_score

'''
        filtered_words = [w for w in WGLib.selectWords(words, 0, start_letter) if len(w) == required_length]
        if player_word in filtered_words and player_word not in used_words:
            if WGLib.getValidInput(player_word, words, used_words, required_length, start_letter):
                current_score += WGLib.processValidInput(player_word, words, current_score)
                start_letter = player_word[-1]
                used_words.add(player_word)
                required_length += 1
                print(f"Valid! +{len(player_word)} points. Total: {current_score}")
                print(WGLib.createDisplayString(player_word, used_words, current_score, 3- regenerations_left))
        else:
            print(f"Try again! + 0 points. Total: {current_score}")
            print(WGLib.createDisplayString(player_word, used_words, current_score, 3- regenerations_left))

        if required_length > 10:
            print("Chain complete! Auto-regenerating...")
            regenerations_left -= 1
            required_length = 3
            start_letter = random.choice("abcdefghijklmnopqrstuvwxyz")

    print("\nGame Over!")

    return current_score
'''

def startSession(words, seed=None):
    """
    Facilitates an interactive session, allowing the user to play your game multiple times.
    """

    if seed is not None:
        random.seed(seed)  # DO NOT REMOVE OR CALL THIS METHOD ANY OTHER WAY!

    scores = []
    # Ask how many rounds to play at the start
    while True:
        rounds = howManyRounds()
        for round_num in range(1, rounds + 1):
            print(f"\n--- Round {round_num} ---")
            score = playGame(words)
            scores.append(score)
        play_again = WGLib.promptPlayAgain()
        if not play_again:
            break
    return scores
'''
def getValidInput(prompt, words, used_words, required_length=None, start_letter=None):
        """
        Prompt the player to enter a valid string according to the `validate()` function.

        Functional Requirements:
        - Repeatedly prompt the player for input until `validate()` returns True.
        - If the input is invalid, print a message containing the word "invalid" and reprompt.

        Documentation Requirements:
        - All parameters have meaningful names and can be customized for your game.

        Tip:
        - Refer to example implementations of `validate()` to see how this function can be
          used in different game scenarios.

        :param prompt: The string displayed to the player when asking for input.
        :param words: List of valid words.
        :param used_words: List of words that have already been used.
        :param required_length: Optional integer specifying the required length of the word.
        :param start_letter: Optional string specifying the required starting letter of the word.
        :returns: A valid string entered by the player.
        """
        while True:
            user_input = input(prompt).strip().lower()
            if validate(user_input, words, used_words, required_length,
                        start_letter):
                return user_input
            else:
                print("Invalid input. Please try again.")
'''

if __name__ == "__main__":

    # To play a single game:
    random.seed(101) # remove to allow random module to produce different values each run
    words = WGLib.parseWordsFile('lowerwords.txt') # implement this first in WGLib.py (or hard-code your own list of words for testing).
    score = playGame(words)
    print('Your score is: ', score)

    # # To play multiple games in a row, call:
    #words = WGLib.parseWordsFile('lowerwords.txt')
    #scores = startSession(words, 101) # second parameter will be used as the random seed; remove or replace as desired for testing.
    #print('Your scores were:', ", ".join(str(s) for s in scores))