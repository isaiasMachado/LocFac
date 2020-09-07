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

        for c in range(0, cliQtd):
            demaInfo = fp.readline().split()
            for i in range(0, len(demaInfo)):
                cliDema.append(float(demaInfo[i]))
    inst_lidas = {'nroFac': facQtd, 'nroCli': cliQtd, 'demanda': cliDema}
    return inst_lidas
