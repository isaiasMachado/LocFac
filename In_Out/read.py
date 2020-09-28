import numpy as np
import math


def read_inst(nome):
    facCust = []
    facCapac = []
    cusTransCli = []
    cliDema = []

    with open(nome, mode='r') as fp:

        tamInst = fp.readline().split()
        facQtd = int(tamInst[0])
        cliQtd = int(tamInst[1])

        for f in range(0, facQtd):
            facInfo = fp.readline().split()
            facCapac.append(int(facInfo[0]))
            facCust.append(float(facInfo[1]))

        for d in range(cliQtd):
            demanda = int(fp.readline().strip())
            cliDema.append(demanda)
            linhas = math.ceil(facQtd / 7)

            custoClientes = []

            for _ in range(linhas):
                linha = fp.readline().strip().split()
                custoClientes += linha

            custoClientes = list([float(x) for x in custoClientes])

            cusTransCli.append(custoClientes)

    cusTransCli = np.array(cusTransCli).transpose()
    print(cusTransCli)
    cusTransCliFinal = []

    for a in cusTransCli:
        dictAux = {}
        for index, l in enumerate(a):
            dictAux[index + 1] = l
        cusTransCliFinal.append(dictAux)

    return facCust, facCapac, cusTransCliFinal, cliDema

