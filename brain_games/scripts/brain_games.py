#!/usr/bin/env python
from brain_games.cli import welcome_user
from brain_gamse.scripts.brain_even import game
def main():

    print("Welcome to the Brain Games!")
    welcome_user()
    game()

if __name__ == '__main__':
    main()
