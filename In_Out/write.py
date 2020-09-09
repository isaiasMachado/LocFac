
def write_file(dados, name_instancia):

    with open('Results/' + name_instancia + '.txt', mode='w') as fp:


            print(dados, file=fp)


