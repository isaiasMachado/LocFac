import sys
import time
custoMax = 10000000

def gulosa(nroFac, nroCli, capFac, custoFac, demaCli, dist_a_cli):
    t_inicio = time.time()

    custoTotal = 0
    listaFacAbertas = [0] * nroFac
    alocacao_do_cliente = []
    capacidadeRestante = capFac

    for i in range(nroCli):

        custoMin = custoMax
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

    t_total = time.time() - t_inicio
    tempo_formatado = '{:.5f}s'.format(t_total)
    return listaFacAbertas, alocacao_do_cliente, custoTotal, tempo_formatado