age = 0

print("Time to Vote")
print("Lets check out your Age")

while age == 0:
    age = int(input("Enter your Age"))
    if(age < 18) : 
        print("You are not a Adult")
        print("You are not Eligible to Vote")

    else : 
        print("You are a Adult")
        print("You are Eligible to Vote")