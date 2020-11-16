#!/usr/bin/env python3
#encoding: windows-1252

#Escribe un programa que pida un número y calcule su factorial.

if __name__ == "__main__":
    #declare variables and ask for inputs
    num1 = int(input("insert a number: "))
    factorial = 1

    #make a "for" to factor the number
    for i in range(1, num1+1):
        factorial *= i
    
    #print the result
    print("the factorial of %d is: %d" % (num1, factorial))
        


