#!/usr/bin/env python3
#encoding: windows-1252

#Escribe un programa que pida la anchura y la altura de un rectángulo y lo dibuje de la siguiente manera:
#*****
#*   *
#*   *
#*****

if __name__ == "__main__":
    #declare variables and ask for the input
    width = int(input("Insert the width: "))
    height = int(input("Insert the height: "))
    
    a = " "
    b = "" 
    #set a variable to use it ahead in time (amount of sapces inside of the triangle)
    for y in range(width - 2):
        b += a 
    
    #make the rectangle
    for i in range(height):
        if i > 0 and i < height-1:
            print("*", end="")
            print(b, end="")
            print("*", end="")
        for j in range(width):
            if i == 0 or i == (height-1):
                print("*", end="")
        print("\n", end="")
