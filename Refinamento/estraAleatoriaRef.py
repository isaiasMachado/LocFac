import random
import time

def funcaoRefinamentoAleatorio(nroFac, nroCli, capFac, custoFac, demaCli, dist_a_cli, instancia_name):
    t_inicio = time.time()

    flag = False;
    custo = 0
    sequenciaFacilidades = []

    # Resultado da estrategia construtiva aleatorio
    if instancia_name == 'p1':
        custo = 25217.0
        sequenciaFacilidades = [3, 9, 8, 2, 5, 9, 7, 9, 1, 9, 0, 7, 4, 8, 3, 3, 7, 8, 7, 6, 2, 3, 2, 6, 0, 1, 2, 9, 0,
                                4, 0, 4, 7, 9, 6, 6, 6, 9, 2, 5, 1, 0, 2, 3, 4, 6, 4, 6, 6, 9]

    elif instancia_name == 'p13':
        custo = 28032.0
        sequenciaFacilidades = [7, 18, 17, 4, 11, 19, 15, 18, 2, 19, 0, 15, 8, 17, 7, 6, 15, 17, 17, 15, 12,
                                4, 7, 4, 16, 12, 0, 2, 5, 18, 1, 9, 0, 8, 15, 19, 12, 13, 12, 18, 14, 4, 11, 3, 1, 4, 15, 6, 8, 13]

    elif instancia_name == 'p25':
        custo = 113476.0
        sequenciaFacilidades = [7, 18, 17, 4, 11, 29, 19, 15, 20, 18, 2, 19, 0, 29, 26, 15, 8, 17, 7, 6, 22, 15, 17, 26, 17, 15, 12,
                                20, 27, 4, 7, 20, 4, 27, 29, 16, 12, 23, 0, 21, 24, 2, 5, 24, 18, 1, 9, 24, 0, 26, 27, 8, 15, 19, 23,
                                29, 28, 12, 22, 25, 29, 13, 12, 23, 25, 18, 14, 29, 4, 28, 11, 3, 1, 4, 15, 6, 8, 21, 13, 24, 20, 27,
                                9, 13, 16, 26, 12, 18, 11, 17, 18, 13, 18, 7, 28, 10, 21, 29, 29, 0, 27, 8, 19, 21, 22, 5, 22, 27, 10,
                                17, 28, 18, 18, 3, 22, 20, 6, 20, 26, 18, 8, 9, 3, 2, 15, 27, 20, 15, 2, 11, 25, 2, 13, 28, 4, 0, 9, 13,
                                24, 13, 27, 3, 1, 19, 19, 24, 1, 12, 22, 18]


    cont = 0

    while flag == False:
        aux = sequenciaFacilidades[cont]
        sequenciaFacilidades[cont] = sequenciaFacilidades[nroCli - 1]
        sequenciaFacilidades[nroCli - 1] = aux
        aux = sequenciaFacilidades[cont + 1]
        sequenciaFacilidades[cont + 1] = sequenciaFacilidades[nroCli - 2]
        sequenciaFacilidades[nroCli - 2] = aux

        listaFacAbertas, alocacao_do_cliente, custoRefinamento = calculaCusto(nroCli, nroFac, sequenciaFacilidades, capFac,
                                                                              demaCli, custoFac, dist_a_cli)
        if(custoRefinamento < custo):
            flag = True
        else:
            cont +=1
    t_total = time.time() - t_inicio
    tempo_formatado = '{:.5f}s'.format(t_total)
    return listaFacAbertas, alocacao_do_cliente, custoRefinamento, tempo_formatado;


def calculaCusto(nroCli, nroFac, sequenciaFacilidades, capFac, demaCli, custoFac, dist_a_cli):
    listaFacAbertas = [0] * nroFac
    custoTotal = 0
    cont = 0
    alocacao_do_cliente = []
    for i in range(0, nroCli):

        while True:
          cont += 1
          fac_selecionada = sequenciaFacilidades[cont-1]

          if capFac[fac_selecionada] >= demaCli[i]:
                if listaFacAbertas[fac_selecionada] == 0:
                    custoTotal += custoFac[fac_selecionada]
                listaFacAbertas[fac_selecionada] += 1
                capFac[fac_selecionada] -= demaCli[i]
                custoTotal += dist_a_cli[i][fac_selecionada]

                alocacao_do_cliente.append(fac_selecionada)
                break

    return listaFacAbertas, alocacao_do_cliente, custoTotal;