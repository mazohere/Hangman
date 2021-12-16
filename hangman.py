import random
import numpy as np

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

def itterations(full_game_word_list):

  game_word = []
  missing_letters = 0

  for i in full_game_word_list[0]:

    game_word.append(i)

    missing_letters = missing_letters + 1

  print("_" * missing_letters)

  print(game_word)


  level_1_list = list(full_game_word_list[0])
  level_2_list = list(full_game_word_list[1])
  level_3_list = list(full_game_word_list[2])
  level_4_list = list(full_game_word_list[3])
  level_5_list = list(full_game_word_list[4])

  print(level_1_list)

  print(full_game_word_list)

  # stage 2
  gameplay(missing_letters, hangman_images, game_word)
 
def gameplay(missing_letters, hangman_images, game_word):
  

  hangman_value = 0
  
  inncorect = 0
  game_word_while_playing = []

  itteration = -1

  for i in game_word:
    game_word_while_playing.append("_")

  while True:
    print(missing_letters, hangman_images[hangman_value], game_word)

    
    print("guess a letter")

    guess = input()

    for i in game_word:
      print("itteration", itteration)

      if i != guess:
        inncorect_testing = inncorect + 1
        print("inncorect", inncorect_testing)

      if i == guess:
        index_value = game_word.index(i)
        missing_letters_testing = missing_letters - 1
        print("missing_letters", missing_letters_testing)
        game_word_while_playing.pop(index_value)
        game_word_while_playing.insert(index_value, i)

    if inncorect_testing == missing_letters:
      hangman_value = hangman_value + 1
      print(hangman_images[hangman_value])
      print("incorrect")


    elif inncorect_testing != missing_letters:
      print(game_word_while_playing)




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

  itterations(full_game_words_list)

  print(full_game_words_list)

choice()