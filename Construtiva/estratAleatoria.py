import random


def funcaoAleatorio(nroFac, nroCli, capFac, custoFac, demaCli, dist_a_cli):
    listaFacAbertas = [0] * nroFac
    alocacao_do_cliente = []
    custoTotal = 0

    random.seed(3)  # Para reprodução do experimento é necessário determinar a semente aleatória

    cont = 0

    for i in range(0, nroCli):

        while True:
            fac_selecionada = random.randint(0, nroFac - 1)

            if capFac[fac_selecionada] >= demaCli[i]:
                if listaFacAbertas[fac_selecionada] == 0:
                    custoTotal += custoFac[fac_selecionada]
                listaFacAbertas[fac_selecionada] += 1
                capFac[fac_selecionada] -= demaCli[i]
                custoTotal += dist_a_cli[i][fac_selecionada]

                alocacao_do_cliente.append(fac_selecionada)
                break

    return listaFacAbertas, alocacao_do_cliente, custoTotal


