#!/usr/bin/env python3
#encoding: windows-1252

#Escribe un programa que pida la altura de un triángulo y lo dibuje de la siguiente manera:
#    *
#   ***
#  *****
# *******
#*********

if __name__ == "__main__":
    #declare variables and ask for the input
    height = int(input("Insert the height of the triangle: "))

    a = " "
    b = ""
    c = "*"
    #make the necessari spaces
    for i in range(height-1):
        b += a
    
    #make the triangle
    for i in range(height):
        print(b, c, b, end="")
        b = b[:-1]
        c += "**"
        print("\n", end="")



