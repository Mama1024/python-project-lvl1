import prompt
import random

if __name__ == '__main__':
    main()

def main():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print('Hello, ' + name + '!')
    c = ''
    d = ''
    index = ''
    h = 'no'
    def test():
        print('What number is missing in the progression?')
    def nope():
        g = 'Nope'
    def game():
        d = list(range(random.randint(0, 100), random.randint(0, 100), random.randint(1, 100)))
        if len(d) > 5 and len(d) <= 10:
            index = random.randint(0, len(d) - 1)
            c = d[index]
            d[index] = '..'
            print('Question: ' + ' ' + str(d))
            answer = prompt.integer('Your answer: ')
            if answer == c:
                h = 'Correct!'
                print(h)
                return h
            else:
                print("'" + str(answer) + "'" + " is wrong answer ;(. " + "Correct answer was " + "'" + str(c) + "'" + "\n" + "Let's try again, " + name + "!")
                return nope()
        else:
            return game()
    test()
    h = game()
    if h == 'Correct!':
        test()
        game()
        if h == 'Correct!':
            test()
            game()
            if h == 'Correct!':
                print('Cogratulations, ' + name + '!')
