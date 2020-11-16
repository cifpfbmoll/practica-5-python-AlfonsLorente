#!/usr/bin/env python3
#encoding: windows-1252

import sys

#Escribe un programa que pida dos números y escriba la suma de enteros desde el primero hasta el último.

if __name__ == "__main__":
    #Declare variables and ask for an input
    num1 = int(input("Insert a number: "))
    num2 = int(input("Insert a greater number:"))
    result = 0

    #thow an error if num2 is equal or lower than num 1:
    if (num2 <= num1):
        sys.exit("ERROR: the second number must be greater than the first one!")
    
    #make the for to sum all the numbers inside the range
    for i in range(num1, num2+1):
        result += i
    #print the answer
    print("the sum of %d to %d is: %d " % (num1, num2, result))