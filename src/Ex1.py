#!/usr/bin/env python3
#encoding: windows-1252

# Escribe un programa que escriba a los siguientes n�mero (la separaci�n entre n�mero es para facilitar cu�ntos n�meros se deben escribir en cada bucle) 
#y en el que la funci�n range que utilices tenga un �NICO argumento y que el valor de este se corresponda con el n�mero de elementos que aparecen en la lista 
#( por Ejemplo, para la primera lista range (10)).


if __name__ == "__main__":
    #primero
    for i in range(10):
        print(i+1, end=" ")
    
    print("\n-------")
    
    #segundo
    for i in range(20):
        i+=1
        if i % 2 == 0:
            print(i, end=" ")
            
 
    print("\n-------")
    
    #tercero
    for i in range(38):
        i+=1
        if i > 19 and i % 2 == 0:
            print(i, end=" ")
 
    print("\n-------")
    
    #Cuarto
    for i in range(30):
        if i > 7 and i % 4 == 0:
            i+=2
            print(i, end=" ")

    
    print("\n-------")
    
    #Cinco
    for i in reversed(range(41)):
        if (i%5) == 0:
            print(i, end=" ")


    
        
