5import random
print("Let me help you with your Password Creation")
num_amount = input("Howmany Numbers would you like it to be ? ")
char_amount = input("How many Charictors would you like to include ? ")
letters = ("A","B","C","D","E","F","G","H","I","J","K","L","M","O","P","Q","R","S","T""U","V","W","X","Y","Z","a","b","#")
num_amount = int(num_amount)
char_amount = int(char_amount)
pw_letters = (random.choices(letters, k = char_amount))
print (char_amount, "letters will be used and",num_amount, "numbers will be used.")
print(pw_letters)
pw_numbers = random.sample([1, 2, 3, 4, 5,6,7,8,9],  num_amount)
pw= pw_letters+ pw_numbers
random.shuffle(pw) #shuffle method
print (pw_numbers)
print(*pw_numbers, sep="")
print(*pw_letters, sep="")
print("This is your password. ",*pw, sep= "")