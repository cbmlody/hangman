#!/usr/bin/python3

__author__:  "Tomasz Budkiewicz, Cezary Broś"
__version__: "1.0.3"

import random
import time

GUESS_TYPE = ['letter', 'l', 'w', 'word']

def random_capital(cap_list):
    '''takes list of strings, chooses random string and returns it as list'''
    index = random.randrange(0, len(cap_list))
    capital = cap_list[index]
    return(list(capital.upper()))


def convert_to_dash(answer, capital):
    '''converts list from 2nd argument to _ and saves it to list in first argument'''
    for index in range(len(capital)):
        capital[index]
        if capital[index] != ' ':
            answer.append('_')
        else:
            answer.append(' ')
    return(answer)


def check_letter(capital, answer, lifes, bad_choice, count):
    '''checks if user input lettr is in list of letters'''
    letter = input("Choose a letter: ")
    letter = letter.upper()
    if len(letter) == 1:
        count += 1
        if letter in capital:
            for index in range(len(capital)):
                if letter == capital[index]:
                    answer[index] = capital[index]
        else:
            lifes -= 1
            bad_choice.append(letter.upper())
    else:
        print('Wrong input.')
    return(answer, lifes, bad_choice, count)


def check_word(capital, answer, lifes, count):
    '''checks if user input string matches randomly selected string'''
    word = list(input("Type your answer: ").upper())
    count += 1
    if word == capital:
        for index in range(len(capital)):
            answer[index] = capital[index]
    else:
        lifes -= 2
    return(answer, lifes, count)


def guess(pl_answer, capital, pl_lifes, bad_choice, count):
    '''asks user if he want's to type letter or word'''
    guess = input("\n(l)etter or (w)ord? ")
    if guess in GUESS_TYPE:
        if guess == 'letter' or guess == 'l':
            pl_answer, pl_lifes, bad_choice, count = check_letter(capital,  # assign returned values to variables
              pl_answer, pl_lifes, bad_choice, count)
        elif guess == 'word' or guess == 'w':
            pl_answer, pl_lifes, count = check_word(capital, pl_answer,
              pl_lifes, count)
        print("\nBad choices: %s " % bad_choice)
    else:
        print("Wrong input, try again.\n")
    print('\nlifes:', pl_lifes)
    return(pl_answer, pl_lifes, bad_choice, count)


def try_again(again):
    '''asks user to try again'''
    again = input("\nDo you want to try again? (y/n) ")
    if again == 'y':
        pass
    elif again == 'n':
        again = 0
    return(again)


def save_score(count, capital, start_time, end_time):
    '''saves user score to txt file'''
    file = open("scores.txt", "a")
    name = input("\nWhat is your name?: ")
    date_time = time.strftime('%d/%m/%Y, %X')
    file.write(name + " | " + date_time + " | " + str(count) + " | "
      + str(''.join(capital)) + " | " + str(int((end_time - start_time))) + "s" + '\n')


def main():
    '''main loop of hangman game'''
    again = 1
    while again:
        count = 0
        lifes = 5
        answer = []
        bad_choice = []
        start = time.time()
        capital = random_capital(capitals_list)
        print(''.join(capital))  # kontrol!
        print(' '.join(convert_to_dash(answer, capital)))

        while answer != capital and lifes > 0:
            answer, lifes, bad_choice, count = guess(answer, capital, lifes,
              bad_choice, count)
            print(' '.join(answer))
            if lifes == 0:
                end = time.time()
                print("Correct answer is: " + ''.join(capital))
                print("\nGame Over, just like our world!\nYour time was: %s sec."
                  % str(int(end - start)))
                again = try_again(again)
            elif answer == capital:
                end = time.time()
                print("\nYou are winner and our world saviour!!!\n"
                  + "Your time was: ", int(end - start),
                  " seconds and u guessed in " + str(count) + " tries")
                save_score(count, capital, start, end)
                again = try_again(again)


if __name__ == '__main__':
    with open("capitals.txt", "r") as capitals:
        capitals_list = capitals.read().splitlines()
    main()
