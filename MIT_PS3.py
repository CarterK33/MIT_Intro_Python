# 6.0001 Problem Set 3
#
# The 6.0001 Word Game
# Created by: Kevin Luu <luuk> and Jenna Wiens <jwiens>
#
# Name          : <your name>
# Collaborators : <your collaborators>
# Time spent    : <total time>

import math
import random
import string

VOWELS = 'aeiou'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
HAND_SIZE = 20

SCRABBLE_LETTER_VALUES = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10, '*':0
}

# -----------------------------------
# Helper code
# (you don't need to understand this helper code)

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
    # wordlist: list of strings
    wordlist = []
    for line in inFile:
        wordlist.append(line.strip().lower())
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def get_frequency_dict(sequence):
    """
    Returns a dictionary where the keys are elements of the sequence
    and the values are integer counts, for the number of times that
    an element is repeated in the sequence.

    sequence: string or list
    return: dictionary
    """
    
    # freqs: dictionary (element_type -> int)
    freq = {}
    for x in sequence:
        freq[x] = freq.get(x,0) + 1
    return freq
	

# (end of helper code)
# -----------------------------------

#
# Problem #1: Scoring a word
#
def get_word_score(word, n):
    
    word = word.lower()
    sum_of_letters = 0 
    second_component = 7 * len(word) - 3 * (n - len(word))

    for char in word: 
        sum_of_letters+=SCRABBLE_LETTER_VALUES[char]

    if second_component < 0: 
        return sum_of_letters * 1
    
    return sum_of_letters * second_component
    
    
    pass  # TO DO... Remove this line when you implement this function

#
# Make sure you understand how this function works and what it does!
#
def display_hand(hand):
    """
    Displays the letters currently in the hand.

    For example:
       display_hand({'a':1, 'x':2, 'l':3, 'e':1})
    Should print out something like:
       a x x l l l e
    The order of the letters is unimportant.

    hand: dictionary (string -> int)
    """
    
    for letter in hand.keys():
        for j in range(hand[letter]):
             print(letter, end=' ')      # print all on the same line
    print()                              # print an empty line

#
# Make sure you understand how this function works and what it does!
# You will need to modify this for Problem #4.
#
def deal_hand(n):
    """
    Returns a random hand containing n lowercase letters.
    ceil(n/3) letters in the hand should be VOWELS (note,
    ceil(n/3) means the smallest integer not less than n/3).

    Hands are represented as dictionaries. The keys are
    letters and the values are the number of times the
    particular letter is repeated in that hand.

    n: int >= 0
    returns: dictionary (string -> int)
    """
    
    hand={}
    num_vowels = int(math.ceil(n / 3))

    #add 1 wild card to hand, take 1 away from vowel total 
    hand["*"] = 1

    for i in range(num_vowels-1):
        x = random.choice(VOWELS)
        hand[x] = hand.get(x, 0) + 1 

    
    for i in range(num_vowels, n):    
        x = random.choice(CONSONANTS)
        hand[x] = hand.get(x, 0) + 1
    
    return hand

#
# Problem #2: Update a hand by removing letters
#
def update_hand(hand, word):
    
    word = word.lower()
    new_hand = hand.copy()

    for char in word: 
        if char in new_hand.keys():
            new_hand[char]-=1 
        if new_hand[char] == 0: 
            del new_hand[char]

    return new_hand


#
# Problem #3: Test word validity
#
def is_valid_word(word, hand, word_list):
    if ('*' in word.lower()):
        for vowel in VOWELS:
            new_word = word.replace('*', vowel)
            if (new_word in word_list):
                return True

    if (word.lower() not in word_list):
        return False

    # now check hand of letters
    new_hand = hand.copy()

    for letter in word.lower():
        if (letter not in new_hand):
            return False

        new_hand[letter] -= 1

        # check if we ran out of letters
        if (new_hand[letter] < 0):
            return False

    return True
             

    
    
    """
    Returns True if word is in the word_list and is entirely
    composed of letters in the hand. Otherwise, returns False.
    Does not mutate hand or word_list.
   
    word: string
    hand: dictionary (string -> int)
    word_list: list of lowercase strings
    returns: boolean
    """


#
# Problem #5: Playing a hand
#
def calculate_handlen(hand):
    num_of_letters = 0 

    for letter in hand: 
        if hand[letter] >= 1: 
            num_of_letters+=hand[letter]
    
    
    return num_of_letters  # TO DO... Remove this line when you implement this function

def play_hand(hand, word_list):

    total_score = 0

    while calculate_handlen(hand) > 0: 

        print("Current Hand: ", end=" ")
        display_hand(hand)
        user_input = input("Enter word, or !! to indicate that you are finished: ")
        
        if user_input == "!!": 
            break 
        
        if is_valid_word(user_input, hand, word_list): 
            print(f"{user_input} earned {get_word_score(user_input, calculate_handlen(hand))}", end=" ")
            total_score+=get_word_score(user_input,calculate_handlen(hand))
            print(f"Total Score: {total_score}")
            new_hand = update_hand(hand, user_input)
            hand = new_hand
            
        else: 
            print("This is not a valid word. Please choose another word.")

    
    print(f"Ran out of letters. Total score for hand: {total_score}")
    print(" ")
    return total_score

def substitute_hand(hand, letter):
    new_hand = hand.copy()

    if letter not in new_hand: 
        return new_hand
    
    random_letter = random.choice(VOWELS + CONSONANTS)
    new_hand[random_letter] = new_hand.pop(letter)
    
    return new_hand

    """ 
    Allow the user to replace all copies of one letter in the hand (chosen by user)
    with a new letter chosen from the VOWELS and CONSONANTS at random. The new letter
    should be different from user's choice, and should not be any of the letters
    already in the hand.

    If user provide a letter not in the hand, the hand should be the same.

    Has no side effects: does not mutate hand.

    For example:
        substitute_hand({'h':1, 'e':1, 'l':2, 'o':1}, 'l')
    might return:
        {'h':1, 'e':1, 'o':1, 'x':2} -> if the new letter is 'x'
    The new letter should not be 'h', 'e', 'l', or 'o' since those letters were
    already in the hand.
    
    hand: dictionary (string -> int)
    letter: string
    returns: dictionary (string -> int)
    """
    
    pass  # TO DO... Remove this line when you implement this function
       
    
def play_game(word_list):
    total_score = 0
    num_of_hands = int(input("Enter total number of hands: "))
    
    hand = deal_hand(HAND_SIZE)
    print(f"Current hand: ", end="")
    display_hand(hand)
    change_letter_input = input("Would you like to substitute a letter? ")
    
    while num_of_hands > 0:

        if change_letter_input == 'yes' or change_letter_input == 'Yes':
            char_input = input("Which letter would you like to replace: ")
            hand = substitute_hand(hand, char_input)
            print(" ")
            total_score += play_hand(hand, word_list)
            num_of_hands-=1
            print("----")
            hand_redo = input("Would you like to replay this hand? ")
            
        elif change_letter_input == 'no' or change_letter_input == 'No':
            print(" ")
            total_score += play_hand(hand, word_list)
            num_of_hands-=1
            print("----")
            hand_redo = input("Would you like to replay this hand? ")

        elif change_letter_input != None:
            print("Wrong Input, Start Game Again!!")
            break
        
        
        change_letter_input = None #only needed for first iteration
        if hand_redo == "no": 
            hand = deal_hand(HAND_SIZE)
        
        print(" ")
        total_score += play_hand(hand, word_list)
        num_of_hands-=1
        print("----")
        hand_redo = input("Would you like to replay this hand? ")


    print("---------------------------------")    
    print(f"Total Score over all hands: {total_score}") # TO DO... Remove this line when you implement this function
    
    
    """
    Allow the user to play a series of hands

    * Asks the user to input a total number of hands

    * Accumulates the score for each hand into a total score for the 
      entire series
 
    * For each hand, before playing, ask the user if they want to substitute
      one letter for another. If the user inputs 'yes', prompt them for their
      desired letter. This can only be done once during the game. Once the
      substitue option is used, the user should not be asked if they want to
      substitute letters in the future.

    * For each hand, ask the user if they would like to replay the hand.
      If the user inputs 'yes', they will replay the hand and keep 
      the better of the two scores for that hand.  This can only be done once 
      during the game. Once the replay option is used, the user should not
      be asked if they want to replay future hands. Replaying the hand does
      not count as one of the total number of hands the user initially
      wanted to play.

            * Note: if you replay a hand, you do not get the option to substitute
                    a letter - you must play whatever hand you just had.
      
    * Returns the total score for the series of hands

    word_list: list of lowercase strings
    """
    
    
    


#
# Build data structures used for entire session and play game
# Do not remove the "if __name__ == '__main__':" line - this code is executed
# when the program is run directly, instead of through an import statement
#
if __name__ == '__main__':
    word_list = load_words()
    play_game(word_list)
   
    
