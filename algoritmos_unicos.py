tot = tot_valido = 0

arq = open('arquivo.txt', "w")

for numero in range(1000, 10000):
    num_str = str(numero)
    num_lista = list(num_str)
    tot += 1

    # print(numero)

    num_valido = True
    for algo in num_str:
        qtd = num_lista.count(algo)
        if qtd > 1:
            num_valido = False
            break
    if num_valido:
        arq.write(f'Número {numero} é válido\n')
        tot_valido += 1
        arq.write("-=" * 30)
        arq.write('\n' * 2)
    '''
    else:
        print(f'Número {numero} INVÁLIDO')
    '''

# print(f'Total = {tot}')
# print(f'Válidos = {tot_valido}')
# print(f'Diferença = {tot - tot_valido}')
arq.write(f'Total = {tot}\n')
arq.write(f'Válidos = {tot_valido}\n')
arq.write(f'Diferença = {tot - tot_valido}')

arq.close()
