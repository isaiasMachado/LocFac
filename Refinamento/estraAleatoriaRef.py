import random
import time

from Entrada.leitura import le_instancia_csv, capacidade


def funcaoRefinamentoAleatorio(nroFac, nroCli, custoFac, demaCli, dist_a_cli, instancia_name):
    t_inicio = time.time()
    flag = False;
    custo, sequenciaFacilidades = le_instancia_csv(instancia_name);
    cont = 0
    while flag == False:
        aux1 = sequenciaFacilidades[cont]
        sequenciaFacilidades[cont] = sequenciaFacilidades[nroCli - 1]
        sequenciaFacilidades[nroCli - 1] = aux1
        aux = sequenciaFacilidades[cont + 1]
        sequenciaFacilidades[cont + 1] = sequenciaFacilidades[nroCli - 2]
        sequenciaFacilidades[nroCli - 2] = aux
        listaFacAbertas, alocacao_do_cliente, custoRefinamento = calculaCusto(nroCli, nroFac, sequenciaFacilidades,
                                                                              demaCli, custoFac, dist_a_cli,
                                                                              instancia_name)
        if custoRefinamento < custo:
            flag = True
        else:
            cont += 1

    t_total = time.time() - t_inicio
    tempo_formatado = '{:.5f}s'.format(t_total)
    return listaFacAbertas, alocacao_do_cliente, custoRefinamento, tempo_formatado;


def calculaCusto(nroCli, nroFac, sequenciaFacilidades, demaCli, custoFac, dist_a_cli, instancia_name):
    cap = capacidade(instancia_name)
    listaFacAbertas = [0] * nroFac
    custoTotal = 0
    cont = 0
    alocacao_do_cliente = []
    vetAux = cap

    for i in range(0, nroCli):

        while True:
            fac_selecionada = sequenciaFacilidades[cont]
            cont += 1

            if vetAux[fac_selecionada] >= demaCli[i]:
                if listaFacAbertas[fac_selecionada] == 0:
                    custoTotal += custoFac[fac_selecionada]
                listaFacAbertas[fac_selecionada] += 1
                vetAux[fac_selecionada] -= demaCli[i]
                custoTotal += dist_a_cli[i][fac_selecionada]
                alocacao_do_cliente.append(fac_selecionada)
                break
            else:
                cont -= 1
                break

    return listaFacAbertas, alocacao_do_cliente, custoTotal;