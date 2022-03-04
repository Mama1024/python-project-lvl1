#!/usr/bin/env python
import prompt
import random

if __name__ == '__main__':
        main()
def main():

    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print('Hello ' + name + '!')
    c = ''
    def game():
        first = random.randint(0, 100)
        second = random.randint(0, 100)
        print('Find the greatest common divisor of given numbers.' + '\n' + 'Question: ' + str(first) + ' ' + str(second))
        answer = prompt.integer('Your answer: ')
        if first % answer == second % answer:
            c = ('Correct!')
            print(c)
            return c
        else:
             while first != 0 and second != 0:
                if first > second:
                    first = first % second
                else:
                    second = second % first
        print("'" + str(answer) + "'" + "is wrong answer ;(. Correct answer was " + "'" + str(first + second) + "' ." + "\n" + "Let's try again, " + name + "!")

    c = game()
    if c == 'Correct!':
        game()
        if c == 'Correct!':
            game()
            if c == 'Correct!':
                print('Congratulations, ' + name + '!')
