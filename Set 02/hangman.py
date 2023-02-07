# Problem Set 2, hangman.py
# Name: 
# Collaborators:
# Time spent:

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string

WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist



def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''

    # define boolean variable 
    boo_Boo = False 

    # Cycle through letters_guessed characters against secret_word characters 
    for char1 in secret_word: 
      if not char1 in letters_guessed: 
        boo_Boo = False 
        break
      else:
        boo_Boo = True 

    return(boo_Boo)

    # FILL IN YOUR CODE HERE AND DELETE "pass"
    # pass



def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''

    # Define holding variable 
    guessed_word = "" 

    for char1 in secret_word: 
        if char1 in letters_guessed: 
            guessed_word += (char1)
        else: 
            guessed_word += ("_ ")

    return(guessed_word)

    # # FILL IN YOUR CODE HERE AND DELETE "pass"
    # pass



def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''

    available_letters = ""
    all_letters = string.ascii_lowercase 

    for char in all_letters: 
      if char not in letters_guessed: 
          available_letters += char 

    return available_letters

    # # FILL IN YOUR CODE HERE AND DELETE "pass"
    # pass
    
    

def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!
    
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
    
    Follows the other limitations detailed in the problem write-up.
    '''

    word_length = len(secret_word)
    guesses = 6 
    warnings = 3 
    str_available_letters = string.ascii_lowercase 
    letters_guessed = []
    underscore_count_old = word_length
    guessed_word = get_guessed_word(secret_word, letters_guessed)
    vowels = ['a', 'e', 'i', 'o', 'u']
    char_secret_word = []

    for char in secret_word: 
      char_secret_word.append(char)

    secret_word_char_unique = 26 - len(get_available_letters(char_secret_word))

    print("Welcome to the game Hangman!")
    print("I am thinking of a word that is " + str(word_length) + " letters long.")
    print("You have " + str(warnings) + " warnings left.")
    print("-------------")

    # Phase 2 - Guessing Game 
    while guesses > 0: 

      print("You have " + str(guesses) + " guesses left.")
      print("Available letters: " + str_available_letters)
      letter_guess = str.lower(input("Please guess a letter: "))

      if letter_guess not in string.ascii_lowercase: 
        warnings -= 1 
        print("Oops!  That is not a valid letter.  You have " + str(warnings) + " warnings left: " + guessed_word)
        print("-------------")
        if warnings < 0: 
          guesses -= 1

      elif letter_guess not in str_available_letters: 
        warnings -=1 

        if warnings >=0: 
          print("Oops!  You've already guessed that letter.  You have " + str(warnings) + " warnings left: " + guessed_word)
          print("-------------")
        else: 
          print("Oops!  You've already guessed that letter.  You have no warnings left so you lose one guess: " + guessed_word)
          print("-------------")
          guesses -=1 

      else: 
        letters_guessed.append(letter_guess)
        available_letters = get_available_letters(letters_guessed)
        guessed_word = get_guessed_word(secret_word, letters_guessed)

        underscore_count_new = 0 

        for char in guessed_word: 
            if char == "_": 
                underscore_count_new += 1

        if underscore_count_new == underscore_count_old: 
          print("Oops!  That letter is not in my word: " + guessed_word)
          print("-------------")
          if letter_guess in vowels: 
            guesses -= 2
          else: 
            guesses -= 1
        else: 
          print("Good guess: " + guessed_word)
          print("-------------")

        str_available_letters = available_letters
        underscore_count_old = underscore_count_new

        boo_word_guessed = is_word_guessed(secret_word, letters_guessed)

        if boo_word_guessed == True: 
          print("Congratulations, you won!")
          total_score = guesses * secret_word_char_unique
          print("Your total score for this game is: " + str(total_score))
          break 

    if guesses <= 0: 
      print("-------------")
      print("Sorry, you ran out of guesses. The word was " + str(secret_word) + ".")

    # # FILL IN YOUR CODE HERE AND DELETE "pass"
    # pass



# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
#(hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------



def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
    '''

    char_counter = 0
    boo_word = True 
    my_word_chars = [] 

    for char in my_word: 
      if char == "_": 
        char_counter += 2 
      elif char != " ":
        my_word_chars.append(char)
        char_counter += 1

    char_counter = 0 

    if len(other_word) != len(my_word.replace(" ","")): 
      boo_word = False
    else: 
      for char in other_word:  
        my_word_char = my_word[char_counter]
        if my_word_char == "_" and char not in my_word_chars: 
          # do nothing and advance to next other_word character 
          char_counter += 2 
        elif char != my_word_char: 
          boo_word = False 
          char_counter += 1
          break 
        else: 
          char_counter += 1

    return boo_word 

    # # FILL IN YOUR CODE HERE AND DELETE "pass"
    # pass



def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    # my_word_stripped = my_word.replace(" ","") 
    # my_word_length = len(my_word_stripped)
    word_match_string = ""

    for word in wordlist: 
      if match_with_gaps(my_word, word) == True: 
        word_match_string += word + str(" ")

    if len(word_match_string) == 0:
      print("No matches found")
    else: 
      print(word_match_string)




    # # FILL IN YOUR CODE HERE AND DELETE "pass"
    # pass



def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses
    
    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter
      
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
      
    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word. 
    
    Follows the other limitations detailed in the problem write-up.
    '''

    word_length = len(secret_word)
    guesses = 6 
    warnings = 3 
    str_available_letters = string.ascii_lowercase 
    letters_guessed = []
    underscore_count_old = word_length
    guessed_word = get_guessed_word(secret_word, letters_guessed)
    vowels = ['a', 'e', 'i', 'o', 'u']
    char_secret_word = []

    for char in secret_word: 
      char_secret_word.append(char)

    secret_word_char_unique = 26 - len(get_available_letters(char_secret_word))

    print("Welcome to the game Hangman!")
    print("I am thinking of a word that is " + str(word_length) + " letters long.")
    print("You have " + str(warnings) + " warnings left.")
    print("-------------")

    # Phase 2 - Guessing Game 
    while guesses > 0: 

      print("You have " + str(guesses) + " guesses left.")
      print("Available letters: " + str_available_letters)
      letter_guess = str.lower(input("Please guess a letter: "))

      if letter_guess == '*': 
        show_possible_matches(guessed_word)

      elif letter_guess not in string.ascii_lowercase: 
        warnings -= 1 
        print("Oops!  That is not a valid letter.  You have " + str(warnings) + " warnings left: " + guessed_word)
        print("-------------")
        if warnings < 0: 
          guesses -= 1

      elif letter_guess not in str_available_letters: 
        warnings -=1 

        if warnings >=0: 
          print("Oops!  You've already guessed that letter.  You have " + str(warnings) + " warnings left: " + guessed_word)
          print("-------------")
        else: 
          print("Oops!  You've already guessed that letter.  You have no warnings left so you lose one guess: " + guessed_word)
          print("-------------")
          guesses -=1 

      else: 
        letters_guessed.append(letter_guess)
        available_letters = get_available_letters(letters_guessed)
        guessed_word = get_guessed_word(secret_word, letters_guessed)

        underscore_count_new = 0 

        for char in guessed_word: 
            if char == "_": 
                underscore_count_new += 1

        if underscore_count_new == underscore_count_old: 
          print("Oops!  That letter is not in my word: " + guessed_word)
          print("-------------")
          if letter_guess in vowels: 
            guesses -= 2
          else: 
            guesses -= 1
        else: 
          print("Good guess: " + guessed_word)
          print("-------------")

        str_available_letters = available_letters
        underscore_count_old = underscore_count_new

        boo_word_guessed = is_word_guessed(secret_word, letters_guessed)

        if boo_word_guessed == True: 
          print("Congratulations, you won!")
          total_score = guesses * secret_word_char_unique
          print("Your total score for this game is: " + str(total_score))
          break 

    if guesses <= 0: 
      print("-------------")
      print("Sorry, you ran out of guesses. The word was " + str(secret_word) + ".")

    # # FILL IN YOUR CODE HERE AND DELETE "pass"
    # pass



# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


#if __name__ == "__main__":
    # pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.
    
# secret_word = choose_word(wordlist)
# hangman(secret_word)

# secret_word = "tact" 
# letters_guessed = ['e','i', 'k', 'p', 'r', 's'] 
# hangman(secret_word)

###############
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    
secret_word = choose_word(wordlist)
# secret_word = "apple"
hangman_with_hints(secret_word)


# # print(match_with_gaps("a_ ple", "apple"))
# show_possible_matches("a_ _ l_ ")