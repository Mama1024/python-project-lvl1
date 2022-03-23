import prompt
import random

if __name__ == '__main__':
    main()

def main():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print('Hello ' + name + '!')
    c = ''
    pravda = ''
    IsPrime_2 = ''
    def game():
        chislo = random.randint(0,100)
        print('Answer "yes" if given number is prime. Otherwise answer "no"' + '\n' + 'Question: ' + str(chislo))
        answer = prompt.string('Your answer: ')
        def IsPrime(n):
            pravda = 2
            while pravda * pravda <= n and n % pravda != 0:
                pravda += 1
            return pravda * pravda > n
        IsPrime_2 = IsPrime(chislo)
        if answer == 'yes':
            if IsPrime_2 == True:
                c = 'Correct!'
                print(c)
                return c
            else:
                print("'" + answer + "'" + "is wrong answer ;(. Correct answer was " + "'" + "no" + "'" + "\n" + "Let's try again, " + name + "!")
        if answer == 'no':
            if IsPrime_2 == False:
                c = 'Correct!'
                print(c)
                return c
            else:
                print("'" + answer + "'" + "is wrong answer ;(. Correct answer was " + "'" + "yes" + "'" + "\n" + "Let's try again, " + name + "!")
    c = game()
    if c == 'Correct!':
        game()
        if c == 'Correct!':
            game()
            if c == 'Correct!':
                print('Congratulations, ' + name + '!')
