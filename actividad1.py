import os
import math

def clear():
    os.system("cls")
 
def impar(num):
    if num % 2 == 0:
        print("El numero es par")
    else:
        print("El numero es impar")

def perfecto(num):
    divisores = []
    for i in range(1,num-1):
        if num % i == 0:
            divisores.append(i)
    suma = 0
    for i in divisores:
        suma = suma + i  
    if suma == num:
        print("El numero es perfecto")
    else: 
        print("El numero no es perfecto")

def primo(num):
    if num < 1:
        return False

    elif num == 2:
        return True

    else:
        for i in range(2, num):
            if num % i == 0:
                return False
        return True   
def exp(num):
    suma=0
    for n in range(0,50):
        suma+=math.pow(num,n)/math.factorial(n)
    print("Exponencial: ",suma)

def main():
    num = int(input("Ingrese numero: "))
    clear()
    impar(num)
    perfecto(num)
    if primo(num): 
        print("Es primo")
    else: 
        print("No es primo")
    exp(num)


if __name__ == "__main__":
    main()