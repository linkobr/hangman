"""
Hangman: requires a random word to be generated and hidden, then ask for user input to guess a character 
in the word 

shows underscores, asks for input
if first guess in word, reveal.
if first guess not in word, try again 
if second guess in word, reveal.
if second guess not in word, try again.
if third guess in word, reveal.
if third guess not in word, you're done.


"""

import random 
from string import ascii_lowercase
import time as t 

# open the text file and read the lines
with open('1-1000.txt') as f:
    words = f.readlines()

#  defining what words from the text file are okay to generate as a random word
#  the words must be less than 3 characters
ok_words = []
for line in words:
    if len(line) > 3: 
        ok_words.append(line)

p = 1


############################################ INITIALIZE THE GAME #################################################

print("Welcome to Link's Hangman game! You have 3 chances for every letter you guess. Have fun!!!!!!!!!")
t.sleep(p)

#  random word generation takes a random index with randrange and ensures there is no whitespace
random_word = ok_words[random.randrange(0, len(ok_words), 1)].strip()
random_word_list = list(random_word)

guess = ""
# print(random_word)

# converting the random word into underscores, hidden is global to avoid local variable reference assignment error
count = 0
for char in random_word:
    count += 1 
global hidden 
hidden = '_' * count

# print the underscores and the length of the word 
print(hidden, len(hidden))
t.sleep(p)

############################################# ASK FOR INPUT ########################################
letter_guessed = [""]
global tries
tries = 3 


def input_step():
    print(" ")
    global letter_guessed
    if tries < 3:
        print("   O   ")
        t.sleep(p)
        if tries < 2:
            print("  /|\  ")
            t.sleep(p)
    print(" ")
    # ask the user to input their first guess
    if letter_guessed == [""]:
        guess = input("Enter your first guess:  ")
        check_input(guess)
    else:
        print("You have guessed these letters: " + str(letter_guessed))
        t.sleep(p)
        guess = input("Enter your next guess: ")
        check_input(guess)

def check_input(guess):
    global letter_guessed
    if guess in ascii_lowercase:
        if guess not in letter_guessed:
            letter_guessed += guess
            check_guess(guess)
        else:
            print("You already guessed that letter.")
            t.sleep(p)
            input_step()
    else:
        print("Not a valid guess.")
        t.sleep(p)
        input_step()

######################################################### CHECK GUESS ###############################################

def check_guess(guess):
    global tries
    if guess in random_word:
        print("Your guess is in the word!")
        t.sleep(p)
        reveal_letter(guess)
    else:
        print("Oops, that's wrong.")
        t.sleep(p)
        print(hidden)
        t.sleep(p)
        tries -= 1
        if tries == 0:
            print("Too bad, you lost.")
            t.sleep(p)
            print(" ")
            print("   O   ")
            print("  /|\  ")
            print("   ^   ")
            t.sleep(p)
            print("The word was " + random_word + ".")
            t.sleep(p)
            quit()
        else:
            print("You have " + str(tries) + " tries remaining.")
            t.sleep(p)
            input_step()

################## CORRECT GUESS CASE #######################

#  if the guess character is in the word, we need to reveal that letter in the word
def reveal_letter(guess):
    # identify the index of the guess with the method find() which returns an int
    global hidden 
    hidden_list = list(hidden)
    x = 0
    while x < len(random_word_list):
        # for x in range(0, random_word_list):
            if random_word_list[x] == guess:
                # change the index of the guess character which is an underscore into a guess
                hidden_list[x] = guess
            x += 1
    # make the underscores with the new correct guess character back into a string
    hidden = "".join(hidden_list)
    # prints the new hidden string with the correct guess character in it
    # print(random_word_list)
    # print(hidden_list)
    print(hidden)
    t.sleep(p)
    if hidden.find("_") == -1:
        print("Congrats, you did it! The word was " + random_word + ".")
        quit()
    input_step()


input_step()
    
