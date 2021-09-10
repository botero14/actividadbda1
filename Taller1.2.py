import os

def proceso(num):
    if num < 1:
        return False

    elif num == 2:
        return True

    else:
        for i in range(2, num):
            if num % i == 0:
                return False
        return True            

def main():
    print("╔═══════════════════════════════╗")
    num = int(input("║     ingrese un numero ==> "))
    print("╚═══════════════════════════════╝")
    os.system("clear")
    resultado = proceso(num)

    if resultado is True:
        print("╔═══════════════════════════════╗")
        print(f"║     El numero {num}, es primo     ║")
        print("╚═══════════════════════════════╝")

    else:
        print("╔═══════════════════════════════╗")
        print(f"║   El numero {num}, no es primo    ║")
        print("╚═══════════════════════════════╝")

if __name__ == '__main__':
    main()

