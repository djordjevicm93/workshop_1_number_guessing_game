from random import randint

draw_number = randint(1, 101)
print(draw_number)
guess_number_str = input("Guess the number: ")
guessed = False

while not guessed:
    try:
        guess_number_int = int(guess_number_str)
        if guess_number_int < draw_number:
            print("Too small!")
            #continue
        if guess_number_int > draw_number:
            print("Too big!")
        if guess_number_int == draw_number:
            print("You win!")
            guessed = True
            break
        #else:
            #pass
    except Exception:
        print("Its not a number!")
        print(guess_number_str)
        