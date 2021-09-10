
import os
def proceso():
    print("╔═══════════════════════════════╗")
    numero = int(input("║     ingrese un numero ==> "))
    print("╚═══════════════════════════════╝")
    os.system("clear")
    return numero


def main():
    num = proceso()

    if num%2 == 0:
        print("╔═══════════════════════════════╗")
        print(f"║      El número {num} es par.      ║")
        print("╚═══════════════════════════════╝")
    
    else:
        print("╔═══════════════════════════════╗")
        print(f"║     El número {num} es impar.     ║")
        print("╚═══════════════════════════════╝")


if __name__ == "__main__":
    main()
