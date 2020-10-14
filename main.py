import time
import sys
from Entrada.leitura import le_instancia as le
from Construtiva import modeloMat, estratAleatoria, estratGulosa
from Refinamento import estraAleatoriaRef
from Saida.escrita import saveResultsCSV, saveResultsTXT, exibeResultado, comparaResultados

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
    # saveResultsCSV(inst, listaFacAbertas, alocacaoCli, custoTotal)
    # ================================================================================================================
    # tipo = 'Construtiva'
    # estrategia = 'Aleatoria'
    # listaFacAbertas, alocacaoCli, custoTotal, tempo = estratAleatoria.funcaoAleatorio(nroFac, nroCli, capFac, custoFac, demaCli, dist_a_cli)
    # saveResultsTXT(inst, listaFacAbertas, alocacaoCli, custoTotal, tempo, tipo, estrategia)
    # print(custoTotal)
    # ================================================================================================================
    # tipo = 'Construtiva'
    # estrategia = 'Gulosa'
    # listaFacAbertas, alocacaoCli, custoTotal, tempo = estratGulosa.gulosa(nroFac, nroCli, capFac, custoFac, demaCli, dist_a_cli)
    # saveResultsTXT(inst, listaFacAbertas, alocacaoCli, custoTotal, tempo, tipo, estrategia)
    # ================================================================================================================
    tipo = 'Refinamento'
    estrategia = 'Aleatoria'
    listaFacAbertas, alocacaoCli, custoTotal, tempo = estraAleatoriaRef.funcaoRefinamentoAleatorio(nroFac, nroCli, capFac, custoFac, demaCli, dist_a_cli, inst)
    saveResultsTXT(inst, listaFacAbertas, alocacaoCli, custoTotal, tempo, tipo, estrategia)
    # print(listaFacAbertas)
    # print(alocacaoCli)
    # print(custoTotal)
    # ==================================================================================================================
    # escolha = ''
    # while escolha != '9':
    #     print('1 - estratégia aleatória')
    #     print('2 - Estratégia gulosa')
    #     print('3 - Refinamento')
    #     print('4 - Exibe resultado busca aleatória')
    #     print('5 - Exibe resultado busca gulosa')
    #     print('8 - Compara resultados')
    #     print('9 - Sair')
    #     escolha = input('Escolha uma opção: ')
    #
    #     if escolha == '1':
    #         tipo = 'Construtiva'
    #         estrategia = 'Aleatoria'
    #         listaFacAbertas, alocacaoCli, custoTotal, tempo = estratAleatoria.funcaoAleatorio(nroFac, nroCli, capFac, custoFac, demaCli, dist_a_cli)
    #         # saveResultsCSV(inst, listaFacAbertas, alocacaoCli, custoTotal, tempo, tipo, estrategia)
    #         saveResultsTXT(inst, listaFacAbertas, alocacaoCli, custoTotal, tempo, tipo, estrategia)
    #     elif escolha == '2':
    #         tipo = 'Construtiva'
    #         estrategia = 'Gulosa'
    #         listaFacAbertas, alocacaoCli, custoTotal, tempo = estratGulosa.gulosa(nroFac, nroCli, capFac, custoFac, demaCli, dist_a_cli)
    #         saveResultsCSV(inst, listaFacAbertas, alocacaoCli, custoTotal, tempo, tipo, estrategia)
    #     elif escolha == '3':
    #         tipo = 'Refinamento'
    #         estrategia = 'Aleatoria'
    #         listaFacAbertas, alocacaoCli, custoTotal, tempo = estraAleatoriaRef.funcaoRefinamentoAleatorio(nroFac, nroCli, capFac, custoFac, demaCli, dist_a_cli, inst)
    #         saveResultsCSV(inst, listaFacAbertas, alocacaoCli, custoTotal, tempo, tipo, estrategia)
    #     elif escolha == '4':
    #         exibeResultado('Resultados/Construtiva/Aleatoria/')
    #     elif escolha == '5':
    #         exibeResultado('Resultados/Construtiva/Gulosa/')
    #     elif escolha == '8':
    #         comparaResultados('Resultados/')
    #     elif escolha == '9':
    #         break
    #     else:
    #         print('Você deve escolher uma opção válida!')

if __name__ == '__main__':
    main(str(sys.argv[1]))
