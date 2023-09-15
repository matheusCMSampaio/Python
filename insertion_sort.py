#Insertion Sort
import random as rd
def insertion_sort(lista):
    for i in range (1, len(lista)):
        pivo = lista[i]
        j = i - 1
        while j >=0 and pivo < lista [j]:
            lista[j+1] = lista[j]
            j-=1
        lista[j+1] = pivo
    return(lista)    

lista = [rd.randint(0, 1000) for i in range(50)]


print("Lista original: ", lista,"\n")
insertion_sort(lista) #Ordena a lista com o algoritmo de inserção.
print("\nLista ordenada:", lista," \n")