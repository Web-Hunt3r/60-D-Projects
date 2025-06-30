import random


print("     --------Welcome to JustGuess IT--------")
print("            | Your Guess. My Number|        ")

lower_lim= int(input('Enter a lower limit= '))
upper_lim= int(input('Enter a upper limit= '))

num= random.randint(lower_lim,upper_lim)

guess_count=0
while True:
    guess=int(input(f"\nGuess a number between {lower_lim} and {upper_lim} : "))
    guess_count+=1
    if(guess>upper_lim or guess<lower_lim):
        print(f"C'mon man! You said between {lower_lim} and {upper_lim} ")
    elif(guess>num):
        print(f"The number is smaller than {guess} ")
    elif(guess<num):
        print(f"The number is greater than {guess} ")
    
    else:
        print(f"yeyyyy!!! There you go mate.\n You guessed it rightt!! [Attempts={guess_count}] ")
        break
