import random
random_number = (random.randint (1,100))
user_guess = ""
guess_number_of = 0
while user_guess != random_number:
    user_guess = int(input("what is your guess?? "))
    if user_guess == random_number:
        print("you Win!!!!!")
        break
    guess_number_of = guess_number_of + 1
    print("the rabdome number is :" , random_number)
    print("that is guess number ", guess_number_of)
    print("wrong answer!!!")
    random_number = (random.randint(1, 100))
    if guess_number_of == 3:
        print("you losse !!")
        break
print("Thanks for pllayingggggggggggggg")