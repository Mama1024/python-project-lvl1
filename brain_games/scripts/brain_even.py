import random
import prompt

def main():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print('Hello ' + name + '!')
    a = random.randint(0, 100)
    print ('Answer "yes" if the number is even, otherwise answer "no".')
    print ('Question: ' + str(a))
    b = input('Your answer: ')
    if a % 2 == 0:
        if b == 'yes':
            c = 'Correct!'
            print (c)
        else:
            d = "'no' is wrong answer ;(. Correct answer was 'yes'." + "\n" + "Let's try again, " + name
            print (d)
            return
    if a % 2 != 0:
        if b == 'no':
            c = 'Correct!'
            print (c)
        else:
            d = "'yes' is wrong answer ;(. Correct answer was 'no'." + "\n" + "Let's try again, " + name
            print (d)
            return    
    a = random.randint(0,100)
    print ('Question: ' + str(a))
    b = input('Your answer: ')
    if a % 2 == 0:
        if b == 'yes':
            c = 'Correct!'
            print (c)
        else:
            d = "'no' is wrong answer ;(. Correct answer was 'yes'." + "\n" + "Let's try again, " + name
            print (d)
            return
    if a % 2 != 0:
        if b == 'no':
            c = 'Correct!'
            print (c)
        else:
            d = "'yes' is wrong answer ;(. Correct answer was 'no'." + "\n" + "Let's try again, " + name
            print (d)
            return
    a = random.randint(0,100)
    print ('Question: ' + str(a))
    b = input('Your answer: ')
    if a % 2 == 0:
        if b == 'yes':
            c = 'Correct!'
            print (c)
        else:
            d = "'no' is wrong answer ;(. Correct answer was 'yes'." + "\n" + "Let's try again, " + name
            print (d)
            return
    if a % 2 != 0:
        if b == 'no':
            c = 'Correct!'
            print (c)
        else:
            d = "'yes' is wrong answer ;(. Correct answer was 'no'." + "\n" + "Let's try again, " + name
            print (d)
            return
    print ('Congratulations, ' + name + '!')

if __name__ == '__main__':
    main()
