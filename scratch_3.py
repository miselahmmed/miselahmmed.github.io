print("Welcome to the Love Calculator!")
name1 = input("What is your name? ").lower()
name2 = input("What is their name? ").lower()
name = name1 + name2

true= 0
true_in_name = name.count("t")
true += true_in_name
true_in_name = name.count("r")
true += true_in_name
true_in_name = name.count("u")
true += true_in_name
true_in_name = name.count("e")
true += true_in_name


love = 0
love_in_name = name.count("l")
love += love_in_name
love_in_name = name.count("o")
love += love_in_name
love_in_name = name.count("v")
love += love_in_name
love_in_name = name.count("e")
love += love_in_name

true = str(true)
love = str(love)

value= int (true+ love)
if value < 10 or value> 90:
    print(f"Your score is {value}, you can go for mentos")
elif 40 < value and value >50:
    print(f"Your score is {value}, you are alright together")
else:
    print(f"Your score is {value}")
