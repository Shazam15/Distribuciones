import math

def xMenorQueX(media, x):
    suma = 0
    for i in range(x):
        suma = suma + (pow(math.e, -media) * pow(media, i) / math.factorial(i))
    return suma

def xMayorQueX(media, x):
    suma = 0
    for i in range(x+1):
        suma = suma + (pow(math.e, -media) * pow(media, i) / math.factorial(i))
    return 1 - suma

def xIgualAX(media, x):
    return pow(math.e, -media) * pow(media, x) / math.factorial(x)

def xMenorIgualQueX(media, x):
    suma = 0
    for i in range(x+1):
        suma = suma + (pow(math.e, -media) * pow(media, i) / math.factorial(i))
    return suma

def xMayorIgualQueX(media, x):
    suma = 0
    for i in range(x):
        suma = suma + (pow(math.e, -media) * pow(media, i) / math.factorial(i))
    return 1 - suma

def principal():
    print("-----------DISTRIBUCION DE POISSON-----------")
    opc = 0
    cont = 's'
    while cont == 's':
        cont = 's'
        opc = 0
        print("-----------------------------")
        opc = int(input("Ingrese la opcion deseada: \n1.X<x\n2.X>x\n3.X=x\n4.X<=x\n5.X>=x\n:"))
        if(opc == 1):
            print("--------------X < x--------------")
            x = int(input("\nIngrese valor de x: "))
            media = float(input("\nIngrese valor de media: "))
            print(f"\nLa probabilidad de que x < {x} es: {xMenorQueX(media, x)}")
        elif(opc == 2):
            print("--------------X > x--------------")
            x = int(input("\nIngrese valor de x: "))
            media = float(input("\nIngrese valor de media: "))
            print(f"\nLa probabilidad de que x > {x} es: {xMayorQueX(media, x)}")
        elif(opc == 3):
            print("--------------X = x--------------")
            x = int(input("\nIngrese valor de x: "))
            media = float(input("\nIngrese valor de media: "))
            print(f"\nLa probabilidad de que x = {x} es: {xIgualAX(media, x)}")
        elif(opc == 4):
            print("--------------X <= x--------------")
            x = int(input("\nIngrese valor de x: "))
            media = float(input("\nIngrese valor de media: "))
            print(f"\nLa probabilidad de que x <= {x} es: {xMenorIgualQueX(media, x)}")
        elif(opc == 5):
            print("--------------X >= x--------------")
            x = int(input("\nIngrese valor de x: "))
            media = float(input("\nIngrese valor de media: "))
            print(f"\nLa probabilidad de que x >= {x} es: {xMayorIgualQueX(media, x)}")
        else:
            print("\nOpcion invalida")
        cont = input("Desea continuar? [s/n]: ")

