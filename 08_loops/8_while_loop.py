import random  #import the module called random

#With function print() show to user about game
print("Welcome to Guess the Number!")
print("The rules are simple. I will think of a number, and you will try to guess it.")

#To generate a random number between 1 and 10 use function randint() from randon module
number = random.randint(1,10)
#track whether the user guessed the number, create a variable in False
isGuessRight = False 
#to start the loop using while indicate if is not true
while isGuessRight != True:
    #create variable guess to ask with input to the user
    guess = input("Guess a number between 1 and 10: ")
    #with if, compare the number introduce by the guess (is an integer: int) and the number created with random module and if is equal print the result.
    if int(guess) == number:
        print("You guessed {}. That is correct! You win!".format(guess))
        isGuessRight = True
    #otherwise with else print another result if is not equal and continue the loop until is guessed
    else:
        print("You guessed {}. Sorry, that isn't it. Try again.".format(guess))