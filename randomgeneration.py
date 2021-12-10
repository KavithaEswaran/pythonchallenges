#!/usr/bin/env python3.9
import random
print("hello")
n=random.randint(1,99)
print("random number is :")
print(n)
guess=int(input("Guess the Number :"))
print("guessing number is")
print(guess)
while (guess != n):
    if(guess>n):
        print("Guessing number is big! ")
        guess=int(input("Enter smallest Number :"))
        continue
    elif(guess<n):
        print("Guessing number is small !")
        guess=int(input("Enter highest Number :"))
        continue
if(guess==n):
    print("You Guess the correct the number")

print("Random number is:\n" )
print(guess)
    

    





