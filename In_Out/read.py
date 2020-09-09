import numpy as np

def read_inst(nome):

    facCapac = []
    facCust = []
    cliDema = []
    with open(nome, mode='r') as fp:

        tamInst = fp.readline().split()
        facQtd = int(tamInst[0])
        cliQtd = int(tamInst[1])

        for f in range(0, facQtd):
            facInfo = fp.readline().split()
            facCapac.append(int(facInfo[0]))
            facCust.append(int(facInfo[1]))

        matCt = np.genfromtxt(fp, dtype="float", max_rows=cliQtd)
        inst_lidas = {'nroFac': facQtd, 'nroCli': cliQtd, 'demanda': matCt}
    return inst_lidas

