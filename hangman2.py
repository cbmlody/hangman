#!/usr/bin/python3

import random
import time

__author__ = u"Tomasz Budkiewicz, Cezary Broś"
__version__ = "1.0.3"

GUESS_TYPE = ['letter', 'l', 'w', 'word']


def random_capital(cap_list):
    '''takes list of strings, chooses random string and returns it as list'''
    index = random.randrange(0, len(cap_list))
    capital = cap_list[index]
    return(list(capital.upper()))


def convert_to_dash(answer, capital):
    '''takes two arguments (list 1 empty, list 2 with content) and converts
       content from list 2 to _ signs, saves them in list 1 and returns list 1'''
    for index in range(len(capital)):
        capital[index]
        if capital[index] != ' ':
            answer.append('_')
        else:
            answer.append(' ')
    return answer


def check_letter(capital, answer, lifes, bad_choice, count):
    '''checks if user input lettr is in list of letters'''
    letter = input("Choose a letter: ")
    letter = letter.upper()
    if len(letter) == 1 and str(letter).isalpha():
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
    return answer, lifes, bad_choice, count


def check_word(capital, answer, lifes, count):
    '''checks if user input string matches randomly selected string'''
    word = list(input("Type your answer: ").upper())
    count += 1
    if word == capital:
        for index in range(len(capital)):
            answer[index] = capital[index]
    else:
        lifes -= 2
    return answer, lifes, count


def guess(pl_answer, capital, pl_lifes, bad_choice, count):
    '''asks user if he want's to type letter or word and then passes values to
       check_word or check_letter function'''
    guess = input("\n(l)etter or (w)ord? ")
    if guess in GUESS_TYPE:
        if guess == 'letter' or guess == 'l':
            pl_answer, pl_lifes, bad_choice, count = check_letter(capital, pl_answer, pl_lifes, bad_choice, count)
        elif guess == 'word' or guess == 'w':
            pl_answer, pl_lifes, count = check_word(capital, pl_answer, pl_lifes, count)
        print("\nBad choices: %s " % bad_choice)
    else:
        print("Wrong input, try again.\n")
    print('\nlifes:', pl_lifes)
    return pl_answer, pl_lifes, bad_choice, count


def try_again(again):
    '''asks user to try again'''
    again = input("\nDo you want to try again? (y/n) ")
    if again == 'y':
        pass
    elif again == 'n':
        again = 0
    return again


def save_score(count, capital, end_time):  # save scores as csv
    '''adds and saves user score to txt file'''
    name = input("\nWhat is your name?: ")
    date_time = time.strftime('%d/%m/%Y')
    score_list = [name, date_time, ''.join(capital), count, end_time]
    with open('scores.txt', 'a') as scores:
        scores.write(score_list)


def show_scores(file):  # read scores from csv
    with open(file, 'r+') as scores:
        score_table = scores.read().splitlines()
    return score_table


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
            answer, lifes, bad_choice, count = guess(answer, capital, lifes, bad_choice, count)
            print(' '.join(answer))
            if lifes <= 0:
                end_time = int(time.time() - start)
                print("\nCorrect answer is: " + ''.join(capital))
                print("\nGame Over, just like our world!\nYour time was: %s sec." % end_time)
                again = try_again(again)
            elif answer == capital:
                end_time = int(time.time() - start)
                print("\nYou are winner and our world saviour!!!\n" + "Your time was: ", int(end_time), " seconds\
                      and you guessed in " + str(count) + " tries")
                save_score(count, capital, end_time)
                score_table = show_scores('scores.txt')
                print('\n*** HIGH SCORES ***\n')
                time.sleep(0.8)
                for x, y in enumerate(score_table, 1):
                    print(x, ' | '.join(y))
                again = try_again(again)


if __name__ == '__main__':
    with open("capitals.txt", "r") as capitals:
        capitals_list = capitals.read().splitlines()
    main()
