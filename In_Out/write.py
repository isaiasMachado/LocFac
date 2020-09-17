
def write_file(dados, name_instancia):
   # print(dados)

    print(dados.get('nroFac'))
    print(dados.get('nroCli'))
    print(dados.get('demanda'))


    #print(name_instancia)
    with open('Results/' + name_instancia + '.txt', mode='w') as fp:
        cont = 0
        print('Qunatidade de Facilidades: '+ str( dados.get('nroFac')),
              'Quantidade de Cliente: '+ str(dados.get('nroCli')), file=fp)

        # for c in dados:
        #     print(c)
        #     print(cont, c, file=fp)
        #     cont += 1


