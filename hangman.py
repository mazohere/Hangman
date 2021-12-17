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


# creates an array of letters out of the current word then calls gameplay() with the word array
def iterations(full_game_word_list, game_trackers):

  print(full_game_word_list)

  game_word = []

  for i in full_game_word_list[game_trackers[2]]:
    game_word.append(i)

  gameplay(hangman_images, game_word, game_trackers, full_game_word_list)

    
# check and adjust the users choice to make sure is a lowercase, single letter the user hasn't chosen before
def choice_get(incorrect_guesses, user_game_word):

  choice = input()

  while True:

    if choice.isnumeric() or choice in incorrect_guesses or len(choice) != 1 == True or choice in user_game_word:
      print("invalid choice, please choose a single letter you haven't chosen before: ")
      choice = input()
      continue


    if choice.isalpha():
      if choice.isupper():
        choice = choice.lower()
        return choice
      elif choice.islower():
        return choice


def game_result(location, game_trackers, full_game_word_list):

  # internal function to save time and lines of code, asks the user to play again and responds accordingly with their input and the gamestate
  def play_again():
    print("would you like to play again? Y/N")
    while True:
      play_again = input()
      if play_again == "Y" or play_again == "y":
        choice(game_trackers[0], game_trackers[1], game_trackers[2], full_game_word_list)
        break
      elif play_again == "N" or play_again == "n":
        print("see you next time")
        break
      else:
        print("invalid response, please type either 'Y' or 'N'")
  
  # if the user loses the game the game iterations are set back to zero and the computers score is increased, the play_again() internal function is then called 
  if location == "hangman_loss":
    print("the man is dead :(")
    game_trackers[1] += 1
    game_trackers[2] = 0
    print("player score: ", game_trackers[0])
    print("computer_score: ", game_trackers[1])
    print("level: ", game_trackers[2])
    play_again()

  # if the user wins the iterations are increased and the game continues with the player_score having increased. there is also a checker to see if the user has beaten level 5, in which case the option 
  # for continuing from level 1 is available
  elif location == "hangman_win":
    print("you win!")
    game_trackers[0] += 1
    game_trackers[2] += 1
    print("player score: ", game_trackers[0])
    print("computer_score: ", game_trackers[1])
    if game_trackers[2] == 5:
      print("congratulations, you beat every level! you can keep playing if you want but it's gonna loop back around to level 1, there'll be different words though")
      game_trackers[2] = 0
    play_again()

# defines variables then creates a new array with the same amount of underscores as the original array had of letter, this is for the user is compared to the original word until either they are the same or
# the amount of guesses runs out.
def gameplay(hangman_images, game_word, game_trackers, full_game_word_list):
  
  user_game_word = []
  hangman_value = 0
  incorrect_guesses = []


  for i in game_word:
    user_game_word.append("_")

  print("level: ", game_trackers[2])

# while loop that repeatedly checks for win/lose conditions, asks for users choice, and adjusts incorrect guesses and the word the user is writing
  while True:
    print(user_game_word)
    print(hangman_images[hangman_value])
    if hangman_value == 6:
      game_result("hangman_loss", game_trackers, full_game_word_list)
      break

    if user_game_word == game_word:
      game_result("hangman_win", game_trackers, full_game_word_list)
      break
    
    print("incorrect guesses: ", incorrect_guesses)
    print("guess a letter: ")

    

    # if user choice has an index value in game_word, pop out the index values in user_game_word and add the value, if user choice doesn't have an index value in game_word, add it to incorrect_guesses
    # and continue to the next hangman picture

    choice = choice_get(incorrect_guesses, user_game_word)

    letter_tracker = [i for i, x in enumerate(game_word) if x == choice]

    if letter_tracker == []:
      incorrect_guesses.append(choice)
      hangman_value += 1

    elif letter_tracker != []:
      for i in range(0, len(letter_tracker)):
        user_game_word.pop(letter_tracker[i])
        user_game_word.insert(letter_tracker[i], choice)

# selects words from the word bank or continues with the current words based on iteration's value. Assigns player_score, computer_score, and iteraion to game_trackers array for easier access
# functional incrementaion, calls iterations()
def choice(player_score, computer_score, iteration, full_game_word_list):

  game_trackers = [player_score, computer_score, iteration]

  if iteration == 0:
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

    full_game_word_list = [level_1_word, level_2_word, level_3_word, level_4_word, level_5_word]
    
  iterations(full_game_word_list, game_trackers)


# initial values for choice() so it correctly selects random words from the word banks
choice(0, 0, 0, [])