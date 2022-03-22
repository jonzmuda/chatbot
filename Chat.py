loop = 1
age_value = "Not Specified"
name_value = "Not Specified"
while loop == 1:
    the_inp = input().lower()
    if the_inp == "hey":
        print(f"Hello There!")
    elif the_inp == "bye":
        print(f"See you later!")
    elif the_inp == "how are you":
        print(f"I am well, how are you?!")
        the_inp = input().lower()  
        if the_inp == "good":
            print(f"Great to hear!")
    elif the_inp == "whats your name":
        print(f"My name is Bill")
    elif the_inp == "repeat":
        repeat_value = input("Enter what I should repeat: ")
        print(repeat_value)
    elif the_inp == "age":
        age_value = input("Enter your age: ")
    elif the_inp == "how old am i":
        if age_value == "Not Specified":
            print("I dont know your age yet!")
        else:
            print(f"You are {age_value} years old")
    elif the_inp == "name":
        name_value = input("Enter your name: ")    
    elif the_inp == "whats my name":
        if name_value == "Not Specified":
            print("I dont know your name yet!")
        else:
            print(f"Your name is {name_value}")