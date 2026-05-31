# My first Python program
name = input("Enter your name: ")

try:
    age = int(input("Enter your age: "))
except:
    print("Please enter a valid number for age!")
else:
    if age < 0:
        print("Age cannot be negative!")
    else:
        print(f"Hello {name.capitalize()}, you will be {age+1} years old next year!")
        if age < 18:
            print("You are still young — you cannot vote yet.")
        else:
            print("You are old enough to vote!")