"""
Filename: WGLib.py
Date: Oct 03, 2025
Author: Natalie Lai
NetID: ntl12

Description:
    - This module includes a handful of helper functions for you to implement.
    - While we specify some minimal behavior for each function, you should implement
        them as best fit your needs for the game you wish to make! This includes
        allowing you to specify the names and number of variables you need for
        some functions!
    - Implementing ALL of these functions is required.
    - Some functions ask you to write new documentation that describes the intended behavior
        of the function in the context of your game.
    - Some functions also ask you to write "doctests", small unit tests within the docstrings
        themselves, to illustrate the intended behavior. We have included (failing) examples
        for you. See the end of the assignment writeup for more details!
    - Running the main block of this module will run the doctests. You are encouraged to run
        it to check your work!
"""

### include any imports here, e.g., `import random`

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

    >>> validate('apple', ['apple', 'banana'], set(), 5, 'a')
    True
    >>> validate('apple', ['apple', 'banana'], {'apple'}, 5, 'a')
    False
    >>> validate('apple', ['banana'], set(), 5, 'a')
    False
    >>> validate('apple', ['apple', 'banana'], set(), 4, 'a')
    False
    >>> validate('apple', ['apple', 'banana'], set(), 5, 'b')
    False
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
    points = 0
    required_length = 3
    start_letter = random.choice("abcdefghijklmnopqrstuvwxyz")
    regenerations_left = 3
    used_words = set()

    print(start_letter)

    while required_length <= 10 and regenerations_left > 0 :
        print("Next word must: start with " + start_letter + " and be " + str(required_length) + " letters long")
        print("Current score:" + str(points))
        player_word = input("Enter your word (or 'regenerate' to get a new starting letter): ").lower().strip()

        if player_word == "regenerate":
            regenerations_left -= 1
            required_length = 3
            start_letter = random.choice("abcdefghijklmnopqrstuvwxyz")
            print("Regenerating..." + str(regenerations_left))
            continue

        if getValidInput(player_word, words, used_words, required_length, start_letter):
            used_words.add(player_word)
            points += len(player_word)
            start_letter = player_word[-1]
            required_length += 1
            print(f"Valid! +{len(player_word)} points. Total: {points}")
        else:
            print(f"Try again! + 0 points. Total: {points}")

        if required_length > 10:
            print("Chain complete! Auto-regenerating...")
            regenerations_left -= 1
            required_length = 3
            start_letter = random.choice("abcdefghijklmnopqrstuvwxyz")

    print("\nGame Over!")

    return points

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
        play_again = promptPlayAgain()
        if not play_again:
            break
    return scores
'''


def getValidInput(prompt, words, used_words, required_length=None,
                  start_letter=None):
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

    >>> getValidInput('Enter word: ', ['cat', 'dog'], [], 3, 'c')  # doctest: +SKIP
    'cat'
    >>> getValidInput('Enter word: ', ['apple', 'ant'], [], 5, 'a')  # doctest: +SKIP
    'apple'
    """
    while True:
        user_input = input(prompt).strip().lower()

        # Allow "regenerate" to pass through
        if user_input == "regenerate":
            return user_input

        # Validate using your existing validate function
        if validate(user_input, words, used_words, required_length,
                    start_letter):
            return user_input
        else:
            print("Invalid input. Please try again.")

def parseWordsFile(wordsFilePath):
    """
    Given the path to a file with one word per line, return a list of those words in the order in which they were read,
        omitting any trailing whitespace or newline characters. Do NOT call `selectWords()` in this function!

    :param wordsFilePath: A string that is the path to a plaintext file containing one English word per line.
    :returns: A list of the strings in the file at `wordsFilePath`.

    >>> words = parseWordsFile('lowerwords.txt'); words[9323]
    'computer'
    >>> words = parseWordsFile('lowerwords.txt'); words[36096]
    'science'
    """
    words = []
    with open(wordsFilePath, "r") as file:
        for line in file:
            words.append(line.strip())  # remove newline characters and spaces
    return words
'''
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


def getValidInput(prompt, words, used_words, required_length=None,
                  start_letter=None):
    """
    Prompts the user for a string input until a valid word is entered according to `validate()`.

    The function will repeatedly prompt the user using the given `prompt` string until the word:
        - exists in the list `words`,
        - has not been used before (not in `used_words`),
        - optionally has the specified `required_length`,
        - optionally starts with `start_letter`.

    :param prompt: A string prompt to display to the user.
    :param words: A list of valid words.
    :param used_words: A list of words that have already been used.
    :param required_length: Optional integer specifying required word length.
    :param start_letter: Optional string specifying the required starting letter.
    :returns: A valid word entered by the user.
    """
    while True:
        user_input = input(prompt).strip().lower()
        if validate(user_input, words, used_words, required_length,
                    start_letter):
            return user_input
        else:
            print("Invalid input. Please try again.")

'''
def selectWords(words, num, start_letter=None):
    """
    Returns a list of words from `words` that satisfy optional conditions.

    - If `num` is 0, return all valid words satisfying the conditions.
    - If `num` is smaller than the number of valid words, return `num` of them.
    - Words may be filtered to start with `start_letter` if provided.

    :param words: A list of lowercase English words.
    :param num: Number of words to select (0 means all).
    :param start_letter: Optional filter for words starting with this letter.
    :returns: A list of selected words.

    >>> selectWords(['duke', 'blue', 'devil', 'spice', 'eared', 'print'], 0, 'e')
    ['eared']
    >>> selectWords(['duke', 'blue', 'devil', 'spice', 'eared', 'print'], 0, 'd')
    ['duke', 'devil']
    """
    filtered = [w for w in words if
                start_letter is None or w.startswith(start_letter)]
    if num == 0 or num >= len(filtered):
        return filtered
    return filtered[:num]


def createDisplayString(last_guess, used_words, scores, turn_number):
    """
    Constructs a display string summarizing the current game state.

    :param last_guess: The word most recently guessed by the player.
    :param used_words: List of words used so far.
    :param scores: List of scores corresponding to the words used, or a single score as an int.
    :param turn_number: Current turn number.
    :returns: A formatted string describing the game state.

    >>> createDisplayString('whale', ['shark', 'bread'], [3,4,5], 3)
    '** STARTING TURN 3 **\\n\\tCurrent Score: 12\\n\\tYou last guessed: whale'
    >>> createDisplayString('apple', ['pear'], [2], 1)
    '** STARTING TURN 1 **\\n\\tCurrent Score: 2\\n\\tYou last guessed: apple'
    """
    # Handle both int and list inputs
    if isinstance(scores, int):
        total_score = scores
    else:
        total_score = sum(scores)

    return f"** STARTING TURN {turn_number} **\n\tCurrent Score: {total_score}\n\tYou last guessed: {last_guess}"

def processValidInput(new_word, used_words, current_score):
    """
    Updates the game state with a newly validated word.

    - Appends `new_word` to `used_words`.
    - Increases `current_score` by the length of `new_word`.

    :param new_word: A word that has been validated.
    :param used_words: List of words used so far (this will be mutated).
    :param current_score: Integer score (will be updated and returned).
    :returns: Updated score after adding the new word.

    >>> words = ['duke', 'alex']
    >>> score = 7
    >>> score = processValidInput('bluedevil', words, score)
    >>> words
    ['duke', 'alex', 'bluedevil']
    >>> score
    16
    >>> words2 = ['cat']
    >>> score2 = 3
    >>> score2 = processValidInput('dog', words2, score2)
    >>> words2
    ['cat', 'dog']
    >>> score2
    6
    """
    used_words.append(new_word)
    current_score += len(new_word)
    return current_score


if __name__ == "__main__":
    import doctest
    doctest.testmod() # runs the doctests in your docstrings above