# lista1 = [1,2,3,4]
# lista2 = [5,6,7,8]
# lista3 = [9,10,11,12]
# lista4 = [13,14,15,16]
# matriz = [lista1,lista2, lista3,lista4]
# matriz1 = [('pt','carro'),('english','car'),('fr','auto')]
# for i in range(len(matriz)):
#     for j in range(len(matriz[i])):
#         print(matriz[i][j], end='\t')
#     print('\n')

# lista_zero = [0]*5
# matriz = [lista_zero] * 5

# for i in range(len(matriz)):
#     for j in range(len(matriz[i])):
#         print(matriz[i][j], end='\t')
#     print('\n')
# a = []
# for i in range(5):
#     a.append([0]*3)
# a[1][1] = 100
# for i in range(len(a)):
#     for j in range(len(a[i])):
#         print(a[i][j], end='\t')
#     print('\n')

def cria_matriz(n_linhas, n_colunas):
    matriz = []
    for i in range(int(n_linhas)):
        linha = []
        for j in range(n_colunas):
            n = int(input('Número: '))
            linha.append(n)
        matriz.append(linha)
    return matriz

def soma_numeros_matriz(matriz):
    soma = 0
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            soma += matriz[i][j]
    return soma

def imprimir(soma):
    print(f'Soma: {soma}')

def main():
    matriz = cria_matriz(3,3)
    soma = soma_numeros_matriz(matriz)
    imprimir(soma)
main()