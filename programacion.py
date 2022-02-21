import math
nombre_file = input("Ingrese el numero de nodos (5, 48 o 101): ")
nombre_file = nombre_file+"nodes"+".txt"
file  = open(nombre_file, "r")


def obteniendo_datos(file):
    lista = []
    for line in file:
        lista.append(line.split())
    
    #del lista[0:4]
    return lista


def imprimir_lista(lista):
    for cords in lista:
        print(cords)

costo_viaje = 0
lista_recorrido = []
#acuerdate que esta madre esta en string y cuando acceses para operaciones usa int(lista[x][y])
lista = obteniendo_datos(file) 
#ejemplo del comentario anterior:
      #Esto es X         Esto es Y
valor_ejemplo = int(lista[0][1]) + int(lista[0][2])#este es un ejemplo de como acceder a una posicion de una lista


nodo_inicial = int(input("Ingrese el numero del nodo para inicar el viaje: "))
print("El nodo inicial es: ",nodo_inicial)
nodo_inicial = nodo_inicial - 1 #se resta 1 por que el nodo 1 es el 0 en la lista
salida = nodo_inicial
lista_recorrido.append(nodo_inicial)

def buscando_siguiente(nodo_actual):
    menor_distancia = 100000
    nodo_menor_distancia = 0
    #se calculan las distancia de cada nodo a partir del nodo actual y se selecciona el mas cercano
    for i in range(len(lista)):
        if i != nodo_actual:
            x1 = int(lista[nodo_actual][1])
            y1 = int(lista[nodo_actual][2])
            x2 = int(lista[i][1])
            y2 = int(lista[i][2])
            distancia =math.sqrt(math.pow((x1 - x2),2) + math.pow((y1 - y2),2)) #calculo de la distancia
            if distancia < menor_distancia:
                if(i in lista_recorrido):  
                    continue
                else:
                    menor_distancia = distancia
                    nodo_menor_distancia = i

    return nodo_menor_distancia, menor_distancia

#se actualiza el costo y la lista de recorrido
for i in range(len(lista)-1):
    nodo_unevo,distancia_nuevo = buscando_siguiente(nodo_inicial)
    lista_recorrido.append(nodo_unevo)
    costo_viaje = costo_viaje + distancia_nuevo   
    nodo_inicial = nodo_unevo 

lista_recorrido.append(lista_recorrido[0])
x1 = int(lista[salida][1])
y1 = int(lista[salida][2])
x2 = int(lista[lista_recorrido[-2]][1])
y2 = int(lista[lista_recorrido[-2]][2])
distancia =math.sqrt(math.pow((x1 - x2),2) + math.pow((y1 - y2),2)) #se agrega la distancia del utlimo nodo al inicial
costo_viaje = costo_viaje + distancia #se agrega la distancia del utlimo nodo al inicial

#imprime el recorrido y el costo del viaje
for elemento in lista_recorrido:
    print(elemento + 1)
print("costo viaje: "+ str(costo_viaje) + " unidades")
        





