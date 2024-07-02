import math
import matplotlib.pyplot as plt
import numpy
import scipy.stats as stats


def buscarZ(x, media, desviacion):
    z = (x-media) / desviacion
    return z

def buscarX(z, media, desviacion):
    x = (z * desviacion) + media
    return x

def buscarDesviacion(x, media, z):
    desviacion = (x-media) / z
    return desviacion

def buscarZMuestra(x, media, desviacion, muestra):
    z = (x-media) / (desviacion/math.sqrt(muestra))
    return z

def buscarXMuestra(z, media, desviacion, muestra):
    x = (z * desviacion/math.sqrt(muestra)) + media
    return x

def buscarDesviacionMuestra(x, media, z, muestra):
    desviacion = (x-media) / (z/math.sqrt(muestra))
    return desviacion

def principal():  
    print("----DISTRIBUCION NORMAL-----")
    opc = 0
    cont = 's'
    while cont =='s':
        cont ='s'
        opc = 0
        print("-----------------------------")
        opc = int(input("Ingrese la opcion deseada: \n1.Buscar z\n2.Buscar x\n3.Buscar Desviacion\n4.Buscar Z con muestra\n5.Buscar X con muestra\n6.Buscar desviacion con muestra\n:"))
        if(opc == 1):
            print("----------BUSCAR Z-------------")

            xi = float(input("Ingresar valor de x: "))
            media = float(input("Ingresar valor de media: "))
            desviacion = float(input("Ingresar valor de desviacion estandar: "))
            print(f"\nValor de z = {buscarZ(xi, media, desviacion)}")
            z = buscarZ(xi, media, desviacion)
        elif(opc == 2):
            print("----------BUSCAR X-------------")
            z = float(input("Ingresar valor de z: "))
            media = float(input("Ingresar valor de media: "))
            desviacion = float(input("Ingresar valor de desviacion estandar: "))
            print(f"\nValor de x = {buscarX(z, media, desviacion)}")
        elif(opc == 3):
            print("----------BUSCAR DESVIACION-------------")
            x = float(input("Ingresar valor de x: "))
            media = float(input("Ingresar valor de media: "))
            z = float(input("Ingresar valor de z: "))
            print(f"\nValor de desviacion = {buscarDesviacion(x, media, z)}")
        elif(opc == 4):
            print("----------BUSCAR  Z CON MUESTRA---------")
            xi = float(input("Ingresar valor de x: "))
            media = float(input("Ingresar valor de media: "))
            desviacion = float(input("Ingresar valor de desviacion estandar: "))
            muestra = int(input("Ingresar valor de muestra: "))
            print(f"\nValor de z = {buscarZMuestra(xi, media, desviacion, muestra)}")
            z = buscarZMuestra(xi, media, desviacion, muestra)
        elif(opc == 5):
            print("----------BUSCAR X CON MUESTRA---------")
            z = float(input("Ingresar valor de z: "))
            media = float(input("Ingresar valor de media: "))
            desviacion = float(input("Ingresar valor de desviacion estandar: "))
            muestra = int(input("Ingresar valor de muestra: "))
            print(f"\nValor de x = {buscarXMuestra(z, media, desviacion, muestra)}")
        elif(opc == 6):
            print("----------BUSCAR DESVIACION CON MUESTRA---------")
            x = float(input("Ingresar valor de x: "))
            media = float(input("Ingresar valor de media: "))
            z = float(input("Ingresar valor de z: "))
            muestra = int(input("Ingresar valor de muestra: "))
            print(f"\nValor de desviacion = {buscarDesviacionMuestra(x, media, z, muestra)}")
        else:
            print("\nOpcion invalida")
        # Plot between -3.9 and 3.9 with .001 steps.
        x_axis = numpy.arange(-3.9, 3.9, 0.001)

        # Mean = 0, SD = 2.
        plt.plot(x_axis, stats.norm.pdf(x_axis, 0, 2))

        # Add a vertical line at x = z
        plt.axvline(x=z, color='r', linestyle='--', linewidth=2)

        # Display the plot
        plt.show()

        cont = input("Desea realizar otro calculo? s/n: ")