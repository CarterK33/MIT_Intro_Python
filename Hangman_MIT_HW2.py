import string
import random

def is_Vowel(char):
    return char.lower() in 'aeiou'

def count_letters_unique_word(secret_word): 
    unique_chars_word = "".join(set(secret_word))
    return len(unique_chars_word)

def is_word_guessed(secret_word, letters_guessed):
    check_string = ""
    for char in secret_word:
        if char in letters_guessed: 
            check_string+=char 
    if check_string == secret_word:
        return True
    else: 
        return False

    
def get_guessed_word(secret_word, letters_guessed):
    word_string = ""
    for char in secret_word: 
        if char in letters_guessed:
            word_string+= char
        else: 
            word_string+='_' 

    return word_string 

def get_available_letters(letters_guessed): 
    alphabet = string.ascii_lowercase
    new_string = "" 

    for char in alphabet: 
        if char not in letters_guessed: 
            new_string+= char

    return new_string 





def main():
    user_guesses = 6 
    letter_guess_list = []
    user_warnings = 3 
    
    
    hangman_file = open("words.txt", 'r')
    contents = hangman_file.read()
    contents = contents.split()

    rand_num = random.randint(0, 5000)
    secret_word = contents[rand_num]

    print("Welcome to Hangman")  
    print(f"I am thinking of a word that is {len(secret_word)} letters long")
    print(f"You have {user_warnings} warnings left.")
    print("------------------------------------")
    
    while user_guesses > 0: 
        print(f"You have {user_guesses} guesses left.") 
        print(f"Available letters: {get_available_letters(letter_guess_list)}")
        
        char_guess = input("Please guess a letter: ")
        
        if char_guess.islower() and char_guess.isalpha() and (char_guess not in letter_guess_list):
            letter_guess_list.append(char_guess)

            if char_guess in secret_word: 
                print(f"Good Guess: {get_guessed_word(secret_word,letter_guess_list )}")
                if is_word_guessed(secret_word, letter_guess_list):
                    total_score = user_guesses * count_letters_unique_word(secret_word)
                    print("Congratulations, you won!")
                    print(f"Your total score for this game is: {total_score}")
                    break 
            else:
                if is_Vowel(char_guess):
                    user_guesses-=2
                    print(f"Oops! That letter is not in my word: {get_guessed_word(secret_word, letter_guess_list)}") 
                else: 
                    user_guesses-=1
                    print(f"Oops! That letter is not in my word: {get_guessed_word(secret_word, letter_guess_list)}")
        
        elif char_guess.islower() and char_guess.isalpha() and (char_guess in letter_guess_list):
            if user_warnings <= 0: 
                user_guesses-=1 
                print(f"Oops! You've already guessed that letter. you have {user_warnings} warnings left: {get_guessed_word(secret_word, letter_guess_list)}")
            else: 
                user_warnings-=1    
                print(f"Oops! You've already guessed that letter. you have {user_warnings} warnings left: {get_guessed_word(secret_word, letter_guess_list)}")
        else:
            if user_warnings <= 0:
                user_guesses-=1
                print(f"Oops! That is not a valid letter. You have {user_warnings} warnings left: {get_guessed_word(secret_word,letter_guess_list)}")
            else    
                user_warnings-=1
                print(f"Oops! That is not a valid letter. You have {user_warnings} warnings left: {get_guessed_word(secret_word,letter_guess_list)}")

        
        



        print("---------------")
        print("---------------")
    if not (is_word_guessed(secret_word,letter_guess_list)):    
        print(f"Sorry you ran out of guesses. The word was {secret_word}")


main() 













