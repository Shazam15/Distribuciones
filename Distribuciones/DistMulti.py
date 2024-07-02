import math

def xIgual(x, p, n, cant):
    calculo = 1
    for i in range(cant):
        calculo = pow(p[i], x[i]) * (1/math.factorial(x[i])) * calculo
    resultado = math.factorial(n) * calculo
    return resultado

def principal():
    print("-----------DISTRIBUCION MULTINOMIAL-----------")
    x = list()
    p = list()
    n = int(input("\nIngrese la n: "))
    cant = int(input("\nIngrese cantidad de variables: "))
    for i in range(cant):
        x.append(int(input(f"\nIngrese el valor de x{i+1}: ")))
        p.append(float(input(f"\nIngrese el valor de p{i+1}: ")))
    print(f"\nLa probabilidad es: {xIgual(x, p, n, cant)}")
