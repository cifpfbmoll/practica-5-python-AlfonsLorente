#!/usr/bin/env python3
#encoding: windows-1252

#Escribe un programa que pida la altura y ancho de un rectángulo y lo dibuje de la siguiente manera:
#*****
#*****
#*****

if __name__ == "__main__":
    #declare variables and ask for the input
    width = int(input("Insert the width: "))
    height = int(input("Insert the height: "))
    
    #make the triangle
    for i in range(height):
        for j in range(width):
            print("*", end="")
        print("\n")