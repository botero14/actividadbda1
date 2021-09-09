
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
        print(i)
    print(divisores)
    suma = 0
    for i in divisores:
        suma = suma + i
        print(i)
    print(suma)
    if suma == num:
        print("El numero es perfecto")
    else: 
        print("El numero no es perfecto")
def main():
    num = int(input("Ingrese numero: "))
    impar(num)
    perfecto(num)


if __name__ == "__main__":
    main()