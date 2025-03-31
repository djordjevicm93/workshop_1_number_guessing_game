from random import randint

draw_number = randint(1, 101)
print(draw_number)
guess_number = input("Guess the number: ")

def ngg_1 (guess_number):
    try:
        guess_number = int(guess_number)
    except TypeError:
        print("Its not a number!")
        return guess_number

if guess_number < draw_number:
    print("Too small!")
if guess_number > draw_number:
    print("Too big!")
if guess_number == draw_number:
    print("You win!")
        
