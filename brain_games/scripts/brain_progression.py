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
    def game():
        print('What number is missing in the progression?')
        def test():
            d = list(range(random.randint(0,100), random.randint(0,100), random.randint(1,100)))
            if len(d) > 5 and len(d) <= 10:
                print('Question: ' + ' ' + str(d))
                return d
            else:
                test()
        d = test()
        print(d)
        index = random.choice(d)
        print(index)
        answer = prompt.integer('Your answer: ')
    game()

