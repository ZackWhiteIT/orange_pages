word = "python"
guessed = ["_"] * len(word)
tries = 6
while tries > 0 and "_" in guessed:
    guess = input("Guess a letter: ").lower()
    if guess in word:
        for i, letter in enumerate(word):
            if letter == guess:
                guessed[i] = guess
    else:
        tries -= 1
    print(" ".join(guessed))
if "_" not in guessed:
    print("You win!")
else:
    print("You lose!")