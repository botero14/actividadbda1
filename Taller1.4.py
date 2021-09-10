import math
import os 

def exp(x):
    suma=0

    for n in range(0,50):
        suma+=math.pow(x,n)/math.factorial(n)

    return suma

def main():
    print("╔═══════════════════════════════╗")
    x = int(input("║     ingrese un numero ==> "))
    print("╚═══════════════════════════════╝")
    os.system("clear")

    exp(x)

    print("╔════════════════════════════════════════════════════")
    print("║  Resultado de la funcion exponencial ==> ", exp(x))
    print("╚════════════════════════════════════════════════════")

if __name__ == '__main__':
    main()
