import math

def calcularEx(xi, pi, n):
    n = len(xi)
    ex = 0
    for i in range(n):
        ex = xi[i] * pi[i] + ex
    return ex

def calcularDesviacion(xi, pi, n, ex):
    n = len(xi)
    desviacion = 0
    sumatoria = 0
    for i in range(n):
        sumatoria = sumatoria + (pow(xi[i], 2) * pi[i])
    desviacion = sumatoria - pow(ex, 2)
    return math.sqrt(desviacion)

def principal(): 
    x = list()
    p = list()
    valorEsp = 0

    n = 0
    print("-------------ESPERANZA MATEMATICA-------------")
    n = int(input("Ingrese la cantidad de datos que quiere ingresar: "))
    print("\n----------Ingreso de datos----------\n")
    for i in range(n):
        x.append(float(input(f"\nIngrese el valor de x{i+1}: ")))
        p.append(float(input(f"\nIngrese el valor de p{i+1}: ")))

    valorEsp = calcularEx(x, p, n)
    print(f"Valor esperado: {valorEsp}")

    desviacion = calcularDesviacion(x, p, n, valorEsp)
    print(f"Desviacion: {desviacion}")