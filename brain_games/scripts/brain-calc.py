#!/usr/bin/env python
import prompt
import random

if __name__ == '__main__':
    main()

def main():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I gave your name? ')
    print('Hello, ' + name + '!')
    znaki = ['+', '-', '*']
    znak = random.choice(znaki)
    chislo = random.randint(0, 100)
    chislo_2 = random.randint(0, 100)
    print('What is the result of the expression?')
    print('Question: ' + str(chislo) + ' ' + str(znak) + ' ' + str(chislo_2))
    otvet = prompt.integer('Your answer: ')
    if znak == '+':
        if otvet == chislo + chislo_2:
            c = 'Correct'
            print(c)
        else:
            print("'" + str(otvet) + "'" + "is wrong answer ;(. Correct answer was " + str(chislo + chislo_2) + '\n' + "Let's try again, " + name)
            return
    if znak == '-':
        if otvet == chislo - chislo_2:
            c = 'Correct'
            print(c)
        else:
            print("'" + str(otvet) + "'" + "is wrong answer ;(. Correct answer was " + str(chislo - chislo_2) + '\n' + "Let's try again, " + name)
            return
    if znak == '*':
        if otvet == chislo * chislo_2:
            c = 'Correct'
            print(c)
        else:
            print("'" + str(otvet) + "'" + "is wrong answer ;(. Correct answer was " + str(chislo * chislo_2) + '\n' + "Let's try again, " + name)
    znak = random.choice(znaki)
    chislo = random.randint(0, 100)
    chislo_2 = random.randint(0, 100)
    print('What is the result of the expression?')
    print('Question: ' + str(chislo) + ' ' + str(znak) + ' ' + str(chislo_2))
    otvet = prompt.integer('Your answer: ')
    if znak == '+':
        if otvet == chislo + chislo_2:
            c = 'Correct'
            print(c)
        else:
            print("'" + str(otvet) + "'" + "is wrong answer ;(. Correct answer was " + str(chislo + chislo_2) + '\n' + "Let's try again, " + name)
            return
    if znak == '-':
        if otvet == chislo - chislo_2:
            c = 'Correct'
            print(c)
        else:
            print("'" + str(otvet) + "'" + "is wrong answer ;(. Correct answer was " + str(chislo - chislo_2) + '\n' + "Let's try again, " + name)
            return
    if znak == '*':
        if otvet == chislo * chislo_2:
            c = 'Correct'
            print(c)
        else:
            print("'" + str(otvet) + "'" + "is wrong answer ;(. Correct answer was " + str(chislo * chislo_2) + '\n' + "Let's try again, " + name)
    znak = random.choice(znaki)
    chislo = random.randint(0, 100)
    chislo_2 = random.randint(0, 100)
    print('What is the result of the expression?')
    print('Question: ' + str(chislo) + ' ' + str(znak) + ' ' + str(chislo_2))
    otvet = prompt.integer('Your answer: ')
    if znak == '+':
        if otvet == chislo + chislo_2:
            c = 'Correct'
            print(c)
        else:
            print("'" + str(otvet) + "'" + "is wrong answer ;(. Correct answer was " + str(chislo + chislo_2) + '\n' + "Let's try again, " + name)
            return
    if znak == '-':
        if otvet == chislo - chislo_2:
            c = 'Correct'
            print(c)
        else:
            print("'" + str(otvet) + "'" + "is wrong answer ;(. Correct answer was " + str(chislo - chislo_2) + '\n' + "Let's try again, " + name)
            return
    if znak == '*':
        if otvet == chislo * chislo_2:
            c = 'Correct'
            print(c)
        else:
            print("'" + str(otvet) + "'" + "is wrong answer ;(. Correct answer was " + str(chislo * chislo_2) + '\n' + "Let's try again, " + name)
            return
    print('Congratulations, ' + name)
