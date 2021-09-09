import math
def exp(x):
    suma=0
    for n in range(0,50):
        suma+=math.pow(x,n)/math.factorial(n)
    return suma
print("funcion exponencial",exp(2))
def main():
    n=int (input("Escribe el numero: "))
    exp(n)
    main()