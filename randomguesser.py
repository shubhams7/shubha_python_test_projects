import random
# takes the random  range that the user would want to guess in
random_number = input("Enter a number ")
if random_number.isdigit():
    random_int = int(random_number)
else:
    print("Please enter a number value and  not a string")
    exit()
# this code sets a random  number to the output_random_it which the users will have to guess
output_random_int=random.randint(0,random_int)
counter=0
while True:
    guess = input("Guess the random number :")
    if not guess.isdigit():
        print("Please enter a digit ")
        continue
    counter+=1
    if int(guess) == output_random_int:
        print("This is the corrrect number")
        break
    else :
        print("This is the inccorrect guess")
        continue
    
print("you got  the  correct guess in", counter , "times")


    
