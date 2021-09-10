import math
def exp(x):
    suma=0
    for n in range(0,50):
        suma+=math.pow(x,n)/math.factorial(n)
    return suma
def main():
    x = int(input("ingrese un numero: "))
    exp(x)
    print("funcion exponencial: ", exp(x))

if __name__ == '__main__':
    main()