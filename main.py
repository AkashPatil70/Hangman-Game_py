import random
# from hangman_art import stages,logo
import hangman_art
# import hangman_words
from hangman_words import word_list
stages = hangman_art.stages
logo = hangman_art.logo
# word_list = hangman_words.word_list
chosen_word = random.choice(word_list)
# print("word chosen :" + chosen_word)
dotted_line=""
for letter in chosen_word :
    dotted_line+="_"
print(dotted_line)

game_over = False
lives = 6
print(logo)
while not game_over :
    guess= (input("guess a letter..")).lower()
    new_state_dotted_line =""

    # print("guess letter: "+ guess)
    #for i in range(0,len(chosen_word)) :
    #for i in range(len(chosen_word)) :
    wrong_guess= True
    for position in range(len(chosen_word)) :
        if chosen_word[position] == guess :
            new_state_dotted_line+=guess
            wrong_guess = False
            if guess in dotted_line :
                print(f"******You have already guessed letter : {guess}")
        # elif dotted_line[position] !="_":
        else:
            new_state_dotted_line+= dotted_line[position]
    dotted_line = new_state_dotted_line
    # game_over = True
    # for char in dotted_line:
    #     if char == "_":
    #         game_over = False

    # if not guess in chosen_word :
    #     lives -= 1
    if wrong_guess :
        lives -= 1
        print(f"You guessed letter : {guess} is not present in the word")
        print(f"Remaining lives : {lives} ")
    print(stages[lives])
    if "_" not in dotted_line :
        print("****** You Won the Game ******")
        game_over = True
    elif not lives > 0:
        print("****** You lost the Game ******")
        print("The Word was :" + chosen_word)
        game_over = True
    print(dotted_line)