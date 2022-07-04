import prompt
import random

name = ''
answer = ''

if __name__ == '__main__':
    pervi()
    vtori()
    vtori_2()

def pervi():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print('Hello, ' + name + '!')
    return name
def vtori():
    answer = prompt.string('Your answer: ')
    return answer
def vtori_2():
    answer = prompt.integer('Your answer: ')
    return answer
