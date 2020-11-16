#!/usr/bin/env python3
#encoding: windows-1252
import sys
#Escribe un programa que pida un número e imprima todos sus divisores.

if __name__ == "__main__":
        #ask for the number and set variables
        num = int(input("Insert an integer: "))
        #the number must be greater than 0
        if num < 1:
            sys.exit("The number must be more than 0") 
        print("The divisible numbers of %d are:" % num, end=" ")
        #print the divisible numbers of num
        for i in range(1, num+1):
            if num % i == 0:
                print(i, end=" ")
            