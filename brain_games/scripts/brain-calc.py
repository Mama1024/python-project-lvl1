#!/usr/bin/env python
import prompt
import random
from brain_games.brain_osnova import name, answer, pervi, vtori_2

if __name__ == '__main__':
    main()

def main():
    name = pervi()
    znaki = ['+', '-', '*']
    print('What is the result of the expression?')
    def main_game():
        znaki = ['+', '-', '*']
        znak = random.choice(znaki)
        chislo = random.randint(0, 100)
        chislo_2 = random.randint(0, 100)
        print('Question: ' + str(chislo) + ' ' + str(znak) + ' ' + str(chislo_2))
        answer = vtori_2()
        if znak == '+':
            if answer == chislo + chislo_2:
                c = 'Correct!'
                print(c)
                return c
            else:
                print("'" + str(answer) + "'" + "is wrong answer ;(. Correct answer was " + str(chislo + chislo_2) + '\n' + "Let's try again, " + name)
                return
        if znak == '-':
            if answer == chislo - chislo_2:
                c = 'Correct!'
                print(c)
                return c
            else:
                print("'" + str(answer) + "'" + "is wrong answer ;(. Correct answer was " + str(chislo - chislo_2) + '\n' + "Let's try again, " + name)
                return
        if znak == '*':
            if answer == chislo * chislo_2:
                c = 'Correct!'
                print(c)
                return c
            else:
                print("'" + str(answer) + "'" + "is wrong answer ;(. Correct answer was " + str(chislo * chislo_2) + '\n' + "Let's try again, " + name)
    c = main_game()
    i = 0
    if c == 'Correct!':
        while i < 2:
            main_game()
            i = i + 1
        print('Congratulations, ' + name + '!')
