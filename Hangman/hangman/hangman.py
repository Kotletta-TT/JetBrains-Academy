# Write your code here
import random
alphabet = 'abcdefghijklmnopqrstuvwxyz'
list_words = ["python", "java", "kotlin", "javascript"]


def start():
    attempts = 0
    letters = set()
    all_letters = set()
    guess_word = random.choice(list_words)
    while attempts != 8:
        print()
        print(code_word(guess_word, letters))
        user_input = input("Input a letter:")
        if user_input in all_letters:
            print("You already typed this letter")
            continue
        if len(user_input) > 1 or len(user_input) <= 0:
            print("You should input a single letter")
            continue
        if user_input not in alphabet:
            print("It is not an ASCII lowercase letter")
            continue
        if user_input not in guess_word:
            all_letters.add(user_input)
            print("No such letter in the word")
            attempts += 1
            continue
        letters.add(user_input)
        all_letters.add(user_input)
        if len(letters) == len(set(guess_word)):
            print("You guessed the word!")
            print("You survived!")
            exit()
    print("You are hanged!")

def code_word(word, letters):
    code = []
    for letter in word:
        if letter in letters:
            code.append(letter)
        else:
            code.append("-")
    return "".join(code)

def run():
    print("H A N G M A N")
    while True:
        usr_input = input('Type "play" to play the game, "exit" to quit:')
        if usr_input == "play":
            start()
        if usr_input == "exit":
            exit()

run()