def welcome_user():

    import prompt
    name = prompt.string('May I have your name? ')

    if name != '':
        print('Hello, ' + name + '!')
