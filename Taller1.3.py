import os

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
        print("╔═══════════════════════════════╗")
        print(f"║    El numero {num}, es perfecto   ║")
        print("╚═══════════════════════════════╝")

    else: 
        print("╔═══════════════════════════════╗")
        print(f"║     El numero {num}, no es perfecto    ║")
        print("╚═══════════════════════════════╝")


def main():
    print("╔═══════════════════════════════╗")
    num = int(input("║     ingrese un numero ==> "))
    print("╚═══════════════════════════════╝")
    os.system("clear")
    
    perfecto(num)
    
if __name__ == '__main__':
    main()