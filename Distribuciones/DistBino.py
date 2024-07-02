import math

def xMenorIgualAX(x, n, p, q):
    suma = 0
    for i in range(x+1):
        suma = suma + (math.comb(n, i) * pow(p, i) * pow(q, n - i))
    return suma

def xMayorIgualAX(x, n, p, q):
    suma = 0
    for i in range(x):
        suma = suma + (math.comb(n, i) * pow(p, i) * pow(q, n - i))
    return 1 - suma

def xIgualAX(x, n, p, q):
    return (math.comb(n, x) * pow(p, x) * pow(q, n - x))

def xMenorQueX(x, n, p, q):
    suma = 0
    for i in range(x):
        suma = suma + (math.comb(n, i) * pow(p, i) * pow(q, n - i))
    return suma

def xMayorQueX(x, n, p, q):
    suma = 0
    for i in range(x+1):
        suma = suma + (math.comb(n, i) * pow(p, i) * pow(q, n - i))
    return 1 - suma

def principal():
    print("----------DISTRIBUCION BINOMIAL----------")
    n = 0.0
    q = 0.0
    x = 0
    cont = 's'
    opc = 0
    frac = 's'

    n = int(input("\nIngrese el valor de n: "))
    frac = input("\nEl exito y fracaso estan en fraccion? [s/n]: ")
    if(frac == 's'):
        numerador = int(input("\nIngrese el numerador de p: "))
        den = int(input("\nIngrese el denominador de p: "))
        p = numerador / den
        q = 1 - p
    else:
        p = float(input("\nIngrese el valor de p: "))
        q = float(input("\nIngrese el valor de q: "))

    while cont =='s':
        cont = 's'
        opc = 0
        x = 0
        opc = 0
        print("----------------------------------------------------------------")
        opc = int(input("Ingres eel tipo de calculo que desea hacer\n1.X=x\n2.X<=x\n3.X>=x\n4.X<x\n5.X>x: "))
        if(opc == 1):
            print("--------------X = x--------------")
            x = int(input("\nIngrese valor de x: "))
            print(f"\nLa probabilidad de que x = {x} es: {xIgualAX(x, n, p, q)}")
        elif(opc == 2):
            print("--------------X <= x--------------")
            x = int(input("\nIngrese valor de x: "))
            print(f"\nLa probabilidad de que x <= {x} es: {xMenorIgualAX(x, n, p, q)}")
        elif(opc == 3):
            print("--------------X >= x--------------")
            x = int(input("\nIngrese valor de x: "))
            print(f"\nLa probabilidad de que x >= {x} es: {xMayorIgualAX(x, n, p, q)}")
        elif(opc == 4):
            print("--------------X < x--------------")
            x = int(input("\nIngrese valor de x: "))
            print(f"\nLa probabilidad de que x < {x} es: {xMenorQueX(x, n, p, q)}")
        elif(opc == 5):
            print("--------------X > x--------------")
            x = int(input("\nIngrese valor de x: "))
            print(f"\nLa probabilidad de que x > {x} es: {xMayorQueX(x, n, p, q)}")
        else:
            print("\nOpcion invalida")
        cont = input("\nDesea continuar? [s/n]: ")

