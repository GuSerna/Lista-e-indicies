print('===============================================================')
print('*CONDIÇÃO_01*')
print('===============================================================')
def verifica_soma(lista_numerica, valor_esperado):
    for i in range(len(lista_numerica)):
      for e in range(len(lista_numerica)):
        if(i != e):
          soma = lista_numerica[i] + lista_numerica[e]
          if(soma == valor_esperado):
           print('Numeros: ', lista_numerica[i], lista_numerica[e])
           print('Indices: ', i, e)
           print('Valor esperado: ', valor_esperado)
          if (soma == valor_esperado):
              l = True
    if not 'l' in locals():
        print('VALOR ALVO NÃO ENCONTRADO')
verifica_soma([1,2,3,4,5,6,7,8,9], 10)

print('===============================================================')
print('*CONDIÇÃO_02*')
print('===============================================================')
def verifica_soma(lista_numerica, valor_esperado):
    for i in range(len(lista_numerica)):
      for e in range(len(lista_numerica)):
        if(i != e):
          soma = lista_numerica[i] + lista_numerica[e]
          if(soma == valor_esperado):
           print('Numeros: ', lista_numerica[i], lista_numerica[e])
           print('Indices: ', i, e)
           print('Valor esperado: ', valor_esperado)
           if (soma == valor_esperado):
               l = True
    if not 'l' in locals():
            print('VALOR ALVO NÃO ENCONTRADO')
verifica_soma([3,8,9,6,8,5], 10)

print('===============================================================')
print('*CONDIÇÃO_03*')
print('===============================================================')
def verifica_soma(lista_numerica, valor_esperado):
    for i in range(len(lista_numerica)):
      for e in range(len(lista_numerica)):
        if(i != e):
          soma = lista_numerica[i] + lista_numerica[e]
          if(soma == valor_esperado):
           print('Numeros: ', lista_numerica[i], lista_numerica[e])
           print('Indices: ', i, e)
           print('Valor esperado: ', valor_esperado)
           print('Total: ', soma)
          if (soma == valor_esperado):
              l = True
    if not 'l' in locals():
        print('VALOR ALVO NÃO ENCONTRADO')

verifica_soma([4,8,6,1,3,7], 7)
