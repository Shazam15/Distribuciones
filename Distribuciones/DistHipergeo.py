import math

def xIgualA(x, poblacion, muestra, k):
    numerador = math.comb(k, x) * (math.comb(poblacion - k, muestra - x))
    denominador = math.comb(poblacion, muestra)
    return numerador / denominador

def xMenorIgualQue(x, poblacion, muestra, k):
    suma = 0
    for i in range(x+1):
        numerador = math.comb(k, i) * (math.comb(poblacion - k, muestra - i))
        denominador = math.comb(poblacion, muestra)
        suma = suma + numerador / denominador
    return suma

def xMayorIgualQue(x, poblacion, muestra, k):
    suma = 0
    resultado = 0
    for i in range(x):
        numerador = math.comb(k, i) * (math.comb(poblacion - k, muestra - i))
        denominador = math.comb(poblacion, muestra)
        suma = suma + numerador / denominador
    resultado = 1 - suma
    return resultado

def xMenorQue(x, poblacion, muestra, k):
    suma = 0
    for i in range(x):
        numerador = math.comb(k, i) * (math.comb(poblacion - k, muestra - i))
        denominador = math.comb(poblacion, muestra)
        suma = suma + numerador / denominador
    return suma

def xMayorQue(x, poblacion, muestra, k):
    suma = 0
    resultado = 0
    for i in range(x+1):
        numerador = math.comb(k, i) * (math.comb(poblacion - k, muestra - i))
        denominador = math.comb(poblacion, muestra)
        suma = suma + numerador / denominador
    resultado = 1 - suma
    return resultado

def principal():
    print("----------DISTRIBUCION HIPERGEOMRTRICA----------")
    pob = int(input("Ingrese cant de poblacion: "))
    muestra = int(input("Ingrese cant de muestra: "))
    opc = 's'
    calc = 0
    while opc == 's':
        print("--------------------------------")
        opc = 's'
        x = 0
        k = 0
        calc = int(input("Ingrese el tipo de calculo que quiere hacer \n1. X=x\n2.X<=x\n3.X>=x\n4.X<x\n5.X>x\n: "))
        if(calc == 1):
                print("--------------X = x--------------")
                x = int(input("\nIngrese valor de x: "))
                k = int(input("\nIngrese valor de K: "))
                print(f"\nLa probabilidad de que x = {x} es: {xIgualA(x, pob, muestra, k)}")
        elif(calc == 2):
                print("--------------X <= x-------------")
                x = int(input("\nIngrese valor de x: "))
                k = int(input("\nIngrese valor de K: "))
                print(f"\nLa probabilidad de que x <= {x} es: {xMenorIgualQue(x, pob, muestra, k)}")
        elif(calc == 3):
                print("--------------X >= x-------------")
                x = int(input("\nIngrese valor de x: "))
                k = int(input("\nIngrese valor de K: "))
                print(f"\nLa probabilidad de que x >= {x} es: {xMayorIgualQue(x, pob, muestra, k)}")
        elif(calc == 4):
             print("--------------X < x--------------")
             x = int(input("\nIngrese valor de x: "))
             k = int(input("\nIngrese valor de K: "))
             print(f"\nLa probabilidad de que x < {x} es: {xMenorQue(x, pob, muestra, k)}")
        elif(calc == 5):
                print("--------------X > x--------------")
                x = int(input("\nIngrese valor de x: "))
                k = int(input("\nIngrese valor de K: "))
                print(f"\nLa probabilidad de que x > {x} es: {xMayorQue(x, pob, muestra, k)}")
        else:
            print("\nOpcion invalida")
        calc = 0
        opc = input("\nDesea continuar? (s/n): ")