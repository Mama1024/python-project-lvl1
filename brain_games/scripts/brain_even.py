import random
import prompt
from brain_games.brain_osnova import name, answer, pervi, vtori

c = ''

def main():
    name = pervi()
    print ('Answer "yes" if the number is even, otherwise answer "no".')
    def main_game():
        a = random.randint(0, 100)
        print ('Question: ' + str(a))
        answer = vtori()
        if a % 2 == 0:
            if answer == 'yes':
                c = 'Correct!'
                print(c)
                return c
            else:
                d = "'no' is wrong answer ;(. Correct answer was 'yes'." + "\n" + "Let's try again, " + name
                print (d)
                return None
        elif a % 2 != 0:
            if answer == 'no':
                c = 'Correct!'
                print(c)
                return c
            else:
                d = "'yes' is wrong answer ;(. Correct answer was 'no'." + "\n" + "Let's try again, " + name
                print(d)
                return None
    c = main_game()
    if c == 'Correct!':
        i = 0
        while i < 2:
            main_game()
            i = i + 1
        print ('Congratulations, ' + name + '!')
    else:
        return None

if __name__ == '__main__':
    main()
