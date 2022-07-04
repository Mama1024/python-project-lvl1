#!/usr/bin/env python
import prompt
import random
from brain_games.brain_osnova import name, answer, pervi, vtori_2

if __name__ == '__main__':
        main()

def main():
    name = pervi()
    c = ''
    print('Find the greatest common divisor of given numbers.')
    def main_game():
        first = random.randint(0, 100)
        second = random.randint(0, 100)
        nod = '' 
        print('Question: ' +  str(first) + ' ' + str(second))
        answer = vtori_2()
        while first != 0 and second != 0:
            if first > second:
                first = first % second
            else:
                second = second % first  
        if answer == first or answer == second:
            c = ('Correct!')
            print(c)
            return c
        else:
            print("'" + str(answer) + "'" + "is wrong answer ;(. Correct answer was " + "'" + str(first + second) + "' ." + "\n" + "Let's try again, " + name + "!")

    c = main_game()
    i = 0
    if c == 'Correct!':
        while i < 2:
            main_game()
            i = i + 1
        print('Congratulations, ' + name + '!')
