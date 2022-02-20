import random
import prompt

def main():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print('Hello ' + name + '!')
    a = random.randint(0, 100)
    print ('Answer "yes" if the number is even, otherwise answer "no".')
    print ('Question: ' + str(a))
    b = input ('Your answer: ')
    if a % 2 == 0:
        if b == 'yes':
            print ('Correct!')
        else:
            print ("'yes' is wrong answer ;(. Correct answer was 'no'." + "\n" + "Let's try again, " + name)
    if a % 2 != 0:
        if b == 'no':
            print ('Correct!')
        else:
            print ("'no' is wrong answer ;(. Correct answer was 'yes'." + "\n" + "Let's try again, " + name)

if __name__ == '__main__':
    main()

  #    if b != 'yes':
        #   print ("'" + str(b) + "' is wrong answer ;(.")
    #   elif b != 'no':
        #   print ("'" + str(b) + "' is wrong answer ;(.")
    #   print ('Question: ' + str(random.randint(0,100)))
    #   print ('Your answer: ' + input())
    #   b = input()
    #   c
    #   if b/2 == 0:
       #    print ('Correct!')
    #   print ('Question: ' + str(random.randint(0,100)))
    #   print ('Your answer: ' + input())
    #   c = input()
    #   d
   #    if c/2 == 0:
       #    print ('Correct!')
        #   print ('Congratulations, Sam!')
