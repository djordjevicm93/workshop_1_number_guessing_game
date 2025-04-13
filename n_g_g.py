from random import randint

draw_number = randint(1, 101)
#print(draw_number)
guess_number = False

"""
    Number guessing game
    
    Computer chose random number between 1 and 100, you guess that number.
    Too big. Too small. You win.
    """

while guess_number != draw_number:
    guess_number = input("Guess the number: ")
    try:
        check_number = int(guess_number)
    except ValueError or TypeError:
        print("Its not a number!")
        continue
    if check_number < draw_number:
        print("Too small!")
    elif check_number > draw_number:
        print("Too big!")
    else:
        print("You win!")
        break
