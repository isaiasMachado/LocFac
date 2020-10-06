import time
import sys
from Entrada.leitura import le_instancia as le
from Construtiva import modeloMat, aleatorio

t_inicio = time.time()      # Marca hora de inicio

nroFac = 0
nroCli = 0
capFac = []
custoFac = []
demaCli = []
dist_a_fac = []

def main(inst):
    path = 'c:/Trabalho/LocFac/Instancias/' + inst
    nroFac, nroCli, capFac, custoFac, demaCli, dist_a_fac = le(path)     # Extrai os dados da instancia

    #modeloMat.funcaoObjetivo(nroFac, nroCli, capFac, custoFac, demaCli, dist_a_fac)

    aleatorio.funcaoAleatorio(nroFac, nroCli, capFac, custoFac, demaCli, dist_a_fac)

if __name__ == '__main__':
    main(str(sys.argv[1]))

t_total = time.time() - t_inicio

print('{:.4f}s'.format(t_total))
