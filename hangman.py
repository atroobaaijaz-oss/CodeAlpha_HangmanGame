import random
words = ["python", "apple", "school", "garden", "laptop"]
word = random.choice(words)
guessed_letters = []
incorrect_guesses = 0
max_attempts = 6

print("Welcome to Hangman!")
print("Guess the word one letter at a time.")
while incorrect_guesses < max_attempts:
    display_word = ""
    for letter in word:
        if letter in guessed_letters:
            display_word += letter
        else:
            display_word += "_ "
    print("\nword:" , " ".join(display_word))
    print("Incorrect guesses left:", max_attempts - incorrect_guesses)
    
    guess = input("Guess a letter: ").lower()
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter only one letter.") 
        continue
    if guess in guessed_letters:
        print("You already guessed that letter!")
        continue

    guessed_letters.append(guess)
    if guess in word:
        print("Correct guess!")
    else:
        incorrect_guesses += 1
        print("Wrong guess!")
    if all(letter in guessed_letters for letter in word):
        print("\nCongratulations! You've guessed the word:", word)
        break
if incorrect_guesses == max_attempts:
    print("\nGame over! The word was:", word)