#!/usr/bin/env python3
#encoding: windows-1252

import sys

#Escribe un programa que pida dos números y escriba qué números entre ese par de números son pares y cuáles impares
if __name__ == "__main__":
    #Declare variables and ask for an input
    num1 = int(input("Insert a number: "))
    num2 = int(input("Insert a greater number:"))

    #thow an error if num2 is equal or lower than num 1:
    if (num2 <= num1):
        sys.exit("ERROR: the second number must be greater than the first one!")
    
    #make a for loop and tell id the numbers are even or odd.
    for i in range(num1, num2+1):
        #if the number is even
        if i % 2 == 0 or i == 0:
            print(i, "is even")
        #If the number is odd
        elif not(i % 2 == 0):
            print(i, "is odd")
        #if something happens (shoud not happen)
        else:
            sys.exit("ERROR: Something went wrong")

