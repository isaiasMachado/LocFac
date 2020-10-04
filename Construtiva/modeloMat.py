import random

def funcaoObjetivo(nroFac, nroCli, capFac, custoFac, demaCli, dist_a_cli):
    listaFacAbertas = [0]*nroFac
    alocacao_do_cliente = []
    custoTotal = 0

    print(dist_a_cli)
    for i in range(0, nroCli):
        for j in range(0, nroFac):
            if capFac[j] >= demaCli[i]:
                if listaFacAbertas[j] == 0:
                    custoTotal += custoFac[j]
                    listaFacAbertas[j] += 1
                capFac[j] -= demaCli[i]
                custoTotal += dist_a_cli[i][j]
                alocacao_do_cliente.append(j)

    print(listaFacAbertas)
    print(alocacao_do_cliente)
    print(custoTotal)