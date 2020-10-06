
def escreve_arquivo(dados, name_instancia):

    with open('Resultados/' + name_instancia + '.txt', mode='w') as fp:


            print(dados, file=fp)


