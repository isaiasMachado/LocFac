# Função que calcula o custo para se abrir facilidades mediante o número de clientes e sua demanda,
# número de facilidades, capacidade das facilidades e seu custo de abertura.

def funcaoObjetivo(nroFac, nroCli, capFac, custoFac, demaCli, dist_a_cli):
    listaFacAbertas = [0]*nroFac
    custoTotal = 0

    for i in range(0, nroCli):
        for j in range(0, nroFac):
            if capFac[j] >= demaCli[i]:     # Checa se a facilidade j é capaz de atender o cliente i
                if listaFacAbertas[j] == 0:
                    custoTotal += custoFac[j]
                    listaFacAbertas[j] += 1
                capFac[j] -= demaCli[i]     # Se atendeu o cliente subtrai de sua capacidade inicial
                custoTotal += dist_a_cli[i][j]

    return listaFacAbertas, custoTotal

