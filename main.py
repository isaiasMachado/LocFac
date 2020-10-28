import time
import os
import sys
from Entrada.leitura import le_instancia as le, le_instancia_csv
from Construtiva import modeloMat, estratAleatoria, estratGulosa
from Refinamento import estraAleatoriaRef
from Saida.escrita import saveResultsCSV, saveResultsTXT, exibeResultado, comparaResultados
from MetaHeuristicas import SA

nroFac = 0
nroCli = 0
capFac = []
custoFac = []
demaCli = []
dist_a_fac = []
num_inst = 1

def main(inst):
    instancia = input('Digite a instancia desejada:')
    path = 'c:/Trabalho/LocFac/Instancias/' + instancia + '/' + inst
    nroFac, nroCli, capFac, custoFac, demaCli, dist_a_cli = le(path)     # Extrai os dados da instancia
    # dist_a_cli significa custo de distribuição até o cliente i
    # print(modeloMat.funcaoObjetivo(nroFac, nroCli, capFac, custoFac, demaCli, dist_a_cli))
    # saveResultsCSV(inst, listaFacAbertas, alocacaoCli, custoTotal)
    # ================================================================================================================
    # tipo = 'Construtiva'
    # estrategia = 'Aleatoria'
    # listaFacAbertas, alocacaoCli, custoTotal, tempo = estratAleatoria.funcaoAleatorio(nroFac, nroCli, capFac, custoFac, demaCli, dist_a_cli)
    # saveResultsTXT(inst, listaFacAbertas, alocacaoCli, custoTotal, tempo, tipo, estrategia)
    # ================================================================================================================
    # tipo = 'Construtiva'
    # estrategia = 'Gulosa'
    # listaFacAbertas, alocacaoCli, custoTotal, tempo = estratGulosa.gulosa(nroFac, nroCli, capFac, custoFac, demaCli, dist_a_cli)
    # saveResultsTXT(inst, listaFacAbertas, alocacaoCli, custoTotal, tempo, tipo, estrategia)
    # ================================================================================================================
    # tipo = 'Refinamento'
    # estrategia = 'Aleatoria'
    # listaFacAbertas, alocacaoCli, custoTotal, tempo = estraAleatoriaRef.funcaoRefinamentoAleatorio(nroFac, nroCli, custoFac, demaCli, dist_a_cli, inst)
    # saveResultsTXT(inst, listaFacAbertas, alocacaoCli, custoTotal, tempo, tipo, estrategia)
    # # saveResultsCSV(inst, listaFacAbertas, alocacaoCli, custoTotal, tempo, tipo, estrategia)
    # ==================================================================================================================
    escolha = ''
    while escolha != '9':
        print('1 - estratégia aleatória')
        print('2 - Estratégia gulosa')
        print('3 - Refinamento')
        print('4 - Exibe resultado busca aleatória')
        print('5 - Exibe resultado busca gulosa')
        print('6 - Exibe resultado refinamento')
        print('7 - Simulated Annealing')
        print('8 - spare')
        print('9 - Compara resultados')
        print('-1 - Sair')
        escolha = input('Escolha uma opção: ')

        if escolha == '1':
            tipo = 'Construtiva'
            estrategia = 'Aleatoria'
            listaFacAbertas, alocacaoCli, custoTotal, tempo = estratAleatoria.funcaoAleatorio(nroFac, nroCli, capFac, custoFac, demaCli, dist_a_cli)
            # saveResultsCSV(inst, listaFacAbertas, alocacaoCli, custoTotal, tempo, tipo, estrategia)
            saveResultsTXT(inst, listaFacAbertas, alocacaoCli, custoTotal, tempo, tipo, estrategia)
        elif escolha == '2':
            tipo = 'Construtiva'
            estrategia = 'Gulosa'
            listaFacAbertas, alocacaoCli, custoTotal, tempo = estratGulosa.gulosa(nroFac, nroCli, capFac, custoFac, demaCli, dist_a_cli)
            # saveResultsCSV(inst, listaFacAbertas, alocacaoCli, custoTotal, tempo, tipo, estrategia)
            saveResultsTXT(inst, listaFacAbertas, alocacaoCli, custoTotal, tempo, tipo, estrategia)
        elif escolha == '3':
            tipo = 'Refinamento'
            estrategia = 'Aleatoria'
            listaFacAbertas, alocacaoCli, custoTotal, tempo = estraAleatoriaRef.funcaoRefinamentoAleatorio(nroFac, nroCli, custoFac, demaCli, dist_a_cli, inst)
            saveResultsCSV(inst, listaFacAbertas, alocacaoCli, custoTotal, tempo, tipo, estrategia)
        elif escolha == '4':
            exibeResultado('Resultados/Construtiva/Aleatoria/')
        elif escolha == '5':
            exibeResultado('Resultados/Construtiva/Gulosa/')
        elif escolha == '6':
            exibeResultado('Resultados/Refinamento/Aleatoria/')
        elif escolha == '7':
            nome_arq_saida = 'Tabela resultados SA'

            with open(nome_arq_saida, mode='a') as fp:
                if os.stat(nome_arq_saida).st_size == 0:
                    fp.write(''.ljust(10) + 'Resultado'.ljust(20) + 'Tempo(s)\n')

                for i in range(1, num_inst+1):
                    nome_instancia = 'Instancias/' + instancia + 'p' + str(i)
                    res = 0
                    tempo_inicio = time.time()
                    listaFacAbertas, alocacaoCli, custoTotal, tempo = estratGulosa.gulosa(nroFac, nroCli, capFac, custoFac, demaCli, dist_a_cli)
                    SA.generate_neighbor_by_change_facility(nroCli, nroFac, alocacaoCli, capFac, demaCli, dist_a_cli, listaFacAbertas, custoFac, custoTotal)
                    print('$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$')
                    print(custoTotal)
                    print('$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$')




        elif escolha == '8':
            pass
        elif escolha == '9':
            comparaResultados('Resultados/')
        elif escolha == '-1':
            break
        else:
            print('Você deve escolher uma opção válida!')

if __name__ == '__main__':
    main(str(sys.argv[1]))
