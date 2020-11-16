#!/usr/bin/env python3
#encoding: windows-1252

#Escribe un programa que pida la altura de un triángulo y lo dibuje de la siguiente manera:
#****
#***
#**
#*

if __name__ == "__main__":
    #ask for the height
    height = int(input("insert the height of the triangle: "))
    width = height+1
    for i in range(height):
        width-=1
        for j in range(width):
            print("*", end="")
        print("\n")
    
