import time
import sys
from Entrada.leitura import le_instancia as le
from Construtiva import modeloMat, estratAleatoria, estratGulosa
from Saida.escrita import saveResultsCSV, saveResultsTXT


nroFac = 0
nroCli = 0
capFac = []
custoFac = []
demaCli = []
dist_a_fac = []

def main(inst):
    path = 'c:/Trabalho/LocFac/Instancias/' + inst
    nroFac, nroCli, capFac, custoFac, demaCli, dist_a_cli = le(path)     # Extrai os dados da instancia
    # dist_a_cli significa custo de distribuição até o cliente i
    # print(modeloMat.funcaoObjetivo(nroFac, nroCli, capFac, custoFac, demaCli, dist_a_cli))
    # listaFacAbertas, alocacaoCli, custoTotal = estratAleatoria.funcaoAleatorio(nroFac, nroCli, capFac, custoFac, demaCli, dist_a_cli)
    # saveResultsCSV(inst, listaFacAbertas, alocacaoCli, custoTotal)
    # saveResultsTXT(inst, listaFacAbertas, alocacaoCli, custoTotal)
    # print(custoTotal)
    # listaFacAbertas, alocacaoCli, custoTotal = estratGulosa.gulosa(nroFac, nroCli, capFac, custoFac, demaCli, dist_a_cli)
    # print(listaFacAbertas)
    # print(alocacaoCli)
    # print(custoTotal)
    escolha = ''
    while escolha != '9':
        print('1 estratégia aleatória')
        print('2 Estratégia gulosa')
        print('3 Refinamento')
        print('9 Sair')
        escolha = input('Escolha uma opção: ')

        if escolha == '1':
            tipo = 'Construtiva'
            estrategia = 'Aleatoria'
            listaFacAbertas, alocacaoCli, custoTotal, tempo = estratAleatoria.funcaoAleatorio(nroFac, nroCli, capFac, custoFac, demaCli, dist_a_cli)
            saveResultsCSV(inst, listaFacAbertas, alocacaoCli, custoTotal, tempo, tipo, estrategia)
        elif escolha == '2':
            tipo = 'Construtiva'
            estrategia = 'Gulosa'
            listaFacAbertas, alocacaoCli, custoTotal, tempo = estratGulosa.gulosa(nroFac, nroCli, capFac,
                                                                                              custoFac, demaCli, dist_a_cli)
            saveResultsCSV(inst, listaFacAbertas, alocacaoCli, custoTotal, tempo, tipo, estrategia)
        elif escolha == '3':
            tipo = 'Refinamento'
            estrategia = 'Aleatoria'
            listaFacAbertas, alocacaoCli, custoTotal, tempo = estratGulosa.gulosa(nroFac, nroCli, capFac,
                                                                                  custoFac, demaCli, dist_a_cli)
            saveResultsCSV(inst, listaFacAbertas, alocacaoCli, custoTotal, tempo, tipo, estrategia)
        elif escolha == '9':
            break
        else:
            print('Você deve escolher uma opção válida!')

if __name__ == '__main__':
    main(str(sys.argv[1]))
