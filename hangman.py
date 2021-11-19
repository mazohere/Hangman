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

def gameplay(full_game_word_list):

  game_word = []
  missing_letters = 0

  for i in full_game_word_list[0]:

    game_word.append(i)

    missing_letters = missing_letters + 1

  print("_" * missing_letters)



  level_1_list = list(full_game_word_list[0])

  print(level_1_list)



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

  full_game_words_list = [level_1_word, level_2_word, level_3_word, level_4_word, level_5_word]

  gameplay(full_game_words_list)

  print(full_game_words_list)

choice()