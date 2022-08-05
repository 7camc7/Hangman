import random
import hangman_words
from hangman_words import word_list
import hangman_art 
from hangman_art import logo
from hangman_art import stages

chosen_word = random.choice(word_list)
word_length = len(chosen_word)
word_list = hangman_words.word_list
end_of_game = False
lives = 6

print(logo)
print(f'Pssst, the solution is {chosen_word}.')

display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    for letter in display:
      if guess == letter:
        print(f"You have already guessed {letter}")
        
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
          
    if guess not in chosen_word:
        lives -= 1
        print(f"The letter {guess} is not in the word. Loose a life, lives left= {lives}")
        if lives == 0:
            end_of_game = True
            print("You lose.")
    print(f"{' '.join(display)}")

    if "_" not in display:
        end_of_game = True
        print("You win.")
    print(stages[lives])