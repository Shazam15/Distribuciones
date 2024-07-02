import DistHipergeo
import EsperanzaMat
import DistBino
import DistMulti
import DistPoisson
import DistNorm

opcion = 0
cont = 's'
while cont =='s':
    print("--------------MENU PRINCIPAL--------------")
    opcion = int(input("Ingrese el tipo de calculo que desea hacer\n1.Binomial\n2.Poisson\n3.Multinomial\n4.Hipergeometrica\n5.Valor esperado/Esperanza matematica\n6.Distribucion Normal\n:"))
    if(opcion == 1):
        DistBino.principal()
    elif(opcion == 2):
        DistPoisson.principal()
    elif(opcion == 3):
        DistMulti.principal()
    elif(opcion == 4):
        DistHipergeo.principal()
    elif(opcion == 5):
        EsperanzaMat.principal()
    elif(opcion == 6):
        DistNorm.principal()
    else:
        print("\nOpcion invalida")
    print("\n-------Menu Principal-------")
    cont = input("Desea realizar otro calculo? s/n: ")