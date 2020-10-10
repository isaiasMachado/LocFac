import sys

def gulosa(nroFac, nroCli, capFac, custoFac, demaCli, dist_a_cli):
    custoTotal = 0
    listaFacAbertas = [0] * nroFac
    alocacao_do_cliente = []
    capacidadeRestante = capFac

    for i in range(nroCli):
        print(capacidadeRestante) # Exibe o quanto ainda resta de capacidade para cada facilidade

        custoMin = 10000
        minIndex = -1
        for j in range(nroFac):
            custo = 0
            if listaFacAbertas[j] == 0:
                custo += custoFac[j] + dist_a_cli[i][j]
            else:
                custo = dist_a_cli[i][j]

            if (custo < custoMin) & (capacidadeRestante[j] > demaCli[i]):
                custoMin = custo
                minIndex = j

        custoTotal += custoMin


        if minIndex == -1:
            return listaFacAbertas, alocacao_do_cliente, custoTotal
        else:
            capacidadeRestante[minIndex] -= demaCli[i]
            listaFacAbertas[minIndex] = 1
            alocacao_do_cliente.append(minIndex)

    return listaFacAbertas, alocacao_do_cliente, custoTotal