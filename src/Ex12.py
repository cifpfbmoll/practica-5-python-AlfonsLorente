#!/usr/bin/env python3
#encoding: windows-1252
import sys
#Escribe un programa que pida un número y escriba si es primo o no

if __name__ == "__main__":
       #ask for the number and set variables
        num = int(input("Insert an integer: "))
        #the number must be greater than 0
        counter = 0
        if num < 1:
            sys.exit("The number must be more than 0") 
        #make greater the counter if there is a number divisible by num that is not himself and 1
        for i in range(2, num):
            if num % i == 0:
                counter+=1
        
        #print if its a prime number or not
        if counter == 0:
            print("The number %d IS a prime number" % num)
        else:
            print("The number %d is NOT a prime number" % num)
