
def write_file(dados, name_instancia):

    with open('Results/' + name_instancia + '.txt', mode='w') as fp:
        cont = 0
        for c in dados:
            print(cont, c, file=fp)
            cont += 1


