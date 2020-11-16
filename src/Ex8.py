#!/usr/bin/env python3
#encoding: windows-1252

#Escribe un programa que pida la anchura de un triángulo y lo dibuje de la siguiente manera:
#*
#**
#***
#****
#***
#**
#*


if __name__ == "__main__":
    #ask for the height
    height = int(input("Insert the height of the trinagle: "))
    width = 0

    #make the triangle go forwards
    for i in range(height):
        width+=1
        for j in range(width):
            print("*", end="")
        print("\n")
    #make the triangle go backwards
    height
    for i in reversed(range(1, height)):
        width-=1
        for j in range(width):
            print("*", end="")
        print("\n")
    