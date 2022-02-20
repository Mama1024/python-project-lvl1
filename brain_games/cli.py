import prompt

def welcome_user():
    name = prompt.string('May I have your name? ')
    print('Hello, ' + name + '!')
    name = str(name)
    return name
