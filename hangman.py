import random
words = ["Computer","Boss","Happy","Sad"]
lives = 6
correct = 0

word = random.choice(words).lower()


print("The word is {} characters long".format(len(word)))
print('_' * len(word))
while (lives > 0):
    user_letter = input("Guess a letter in the word:  ")
    if user_letter in word:
        correct = correct+1
        print("You got it {} is the {} character in the word".format(user_letter,word.find(user_letter)+1))
        if(correct == len(word)):
            print("You win! The word was {}".format(word))
            lives = 0
    else:
        lives = lives -1
        if(lives == 0):
            print("Game over! You ran out of lives the word was {}".format(word))
        else:
            print("Try again you have {} lives left".format(lives))
