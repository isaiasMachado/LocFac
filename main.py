import time
import sys
from pulp import *

from In_Out.read import read_inst as le
from In_Out.write import write_file as escreve

t_inicio = time.time()      # Marca hora de inicio

def main(inst):
    path = 'c:/Meta/LocFac/Instancias/' + inst
    facCust, facCapac, custoCli, cliDema = le(path)     # Extrai os dados da instancia

    clientes = []
    for index, c in enumerate(cliDema):     # Atribui um ID aos clientes i
        clientes.append(index+1)
    #print(clientes)

    facilidades = []
    for index, f in enumerate(facCust):     # Atribui um ID a facilidade j
        facilidades.append('FAC '+ str(index+1))
    #print(facilidades)

    demanda = {}
    for index, d in enumerate(cliDema):     # Cria o dicionario demanda do cliente i
        demanda[index+1] = d
    #print(demanda)

    custoFixoFac = {}
    for index, c in enumerate(facCust):     # Cria o dicionario custo fixo associado à localidade j
        custoFixoFac[facilidades[index]] = c
    #print(custoFixoFac)

    capacFacilidade = {}
    for index, c in enumerate(facCapac):    # Cria o dicionario capacidade da facilidade j
        capacFacilidade[facilidades[index]] = c
    #print(capacFacilidade)

    custoTransCli = {}
    for index, a in enumerate(custoCli):
        custoTransCli[facilidades[index]] = a
    #print(custoTransCli)

    # Define a variavel do problema
    prob = LpProblem("LocFac", LpMinimize)

    # Variáveis de decisão
    serv_vars = LpVariable.dicts(
        'Service',
        [(i, j) for i in clientes
                for j in facilidades],
        0
    )

    use_vars = LpVariable.dicts('UsarFacilidade', facilidades, 0, 1, LpBinary)

    # Função objetivo
    prob += lpSum(custoFixoFac[j]*use_vars[j] for j in facilidades) + lpSum(custoTransCli[j][i]*serv_vars[(i, j)] for j in facilidades for i in clientes)

    # Restrições
    for i in clientes:
        prob += lpSum(serv_vars[(i, j)] for j in facilidades) == demanda[i]     # RESTRIÇÃO 1

    for j in facilidades:
        prob += lpSum(serv_vars[(i, j)] for i in clientes) <= capacFacilidade[j]*use_vars[j]

    for i in clientes:
        for j in facilidades:
            prob += serv_vars[(i,j)] <= demanda[i]*use_vars[j]

    # Solução
    prob.solve()
    print('Status:', LpStatus[prob.status])

    TOL = .00001
    for i in facilidades:
        if use_vars[i].varValue > TOL:
            print('Abrir a facilidade', i)

    for v in prob.variables():
        print(v.name,'=', v.varValue)

    # Imprimir a solução ótima
    print('O custo da produção total sera = ', value(prob.objective))

   # escreve(dados, inst)

if __name__ == '__main__':
    main(str(sys.argv[1]))

t_total = time.time() - t_inicio
print('{:.4f}s'.format(t_total))
