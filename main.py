import random
import hangman_words

chosen_word = random.choice(hangman_words.word_list)
length = len(chosen_word)

# intro
print("Welcome to Hangman Game!!!")
print(''' 
                                        _     
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/  



''')

display = []
for letter in range(0, length):
    display += "_"
print(display)

# game status true means underscores are left
# game status false means underscores arent left

game_status = False
lives = 6
while not game_status:
    guess = input("\nGuess a letter!\n").lower()
    for place in range(0, length):
        if chosen_word[place] == guess:
            display[place] = guess
    print(display)

    if guess not in chosen_word:
        print("You have guessed incorrect letter!\nYou lose a life")
        lives -= 1
        if lives == 6:
            print('''  +---+
  |   |
      |
      |
      |
      |
=========
       ''')
        if lives == 5:
            print('''  +---+
  |   |
  O   |
      |
      |
      |
========= ''')
        if lives == 4:
            print('''  +---+
  |   |
  O   |
  |   |
      |
      |
========= ''')
        if lives == 3:
            print('''  +---+
  |   |
  O   |
 /|   |
      |
      |
========= ''')
        if lives == 2:
            print('''  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
      ''')
        if lives == 1:
            print('''  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
      ''')
        if lives == 0:
            game_status = True
            print('''  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
      ''')
            print("You Lost\nTry Again!")

    if "_" not in display:
        game_status = True
        print("Congratulations!!You Win.")

