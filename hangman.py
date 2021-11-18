import random

hangman_images = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

def choice():

    level_1_get = open("level_1.txt").read().split()

    level_1_word = random.choice(level_1_get)

    level_2_get = open("level_2.txt").read().split()

    level_2_word = random.choice(level_2_get)

    level_3_get = open("level_3.txt").read().split()

    level_3_word = random.choice(level_3_get)

    level_4_get = open("level_4.txt").read().split()

    level_4_word = random.choice(level_4_get)

    level_5_get = open("level_5.txt").read().split()

    level_5_word = random.choice(level_5_get)

    print(level_1_word)
    print(level_2_word)
    print(level_3_word)
    print(level_4_word)
    print(level_5_word)

choice()