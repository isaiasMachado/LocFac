import time
import sys
from Entrada.leitura import le_instancia as le
from Construtiva import modeloMat, estratAleatoria, estratGulosa
from Saida.escrita import saveResultsCSV, saveResultsTXT

t_inicio = time.time()      # Marca hora de inicio

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
    listaFacAbertas, alocacaoCli, custoTotal = estratGulosa.gulosa(nroFac, nroCli, capFac, custoFac, demaCli, dist_a_cli)

    print(listaFacAbertas)
    print(custoTotal)


if __name__ == '__main__':
    main(str(sys.argv[1]))

t_total = time.time() - t_inicio

print('{:.4f}s'.format(t_total))
