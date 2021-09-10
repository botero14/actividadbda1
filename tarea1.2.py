def perfecto(num):
    divisores = []
    for i in range(1,num-1):
        if num % i == 0:
            divisores.append(i)
    print(divisores)
    suma = 0
    for i in divisores:
        suma = suma + i  
    if suma == num:
        print("El numero es perfecto")
    else: 
        print("El numero no es perfecto")
def main():
    num = int(input("Ingrese numero: "))
    perfecto(num)

if __name__ == "__main__":
    main()
