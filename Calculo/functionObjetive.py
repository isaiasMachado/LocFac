from pulp import *
def functionObjetive(retorno):
    facCust, facCapac, custoCli, cliDema = retorno  # Extrai os dados da instancia

    clientes = []
    for index, c in enumerate(cliDema):  # Atribui um ID aos clientes i
        clientes.append(index + 1)
    # print(clientes)

    facilidades = []
    for index, f in enumerate(facCust):  # Atribui um ID a facilidade j
        facilidades.append('FAC ' + str(index + 1))
    # print(facilidades)

    demanda = {}
    for index, d in enumerate(cliDema):  # Cria o dicionario demanda do cliente i
        demanda[index + 1] = d
    # print(demanda)

    custoFixoFac = {}
    for index, c in enumerate(facCust):  # Cria o dicionario custo fixo associado à localidade j
        custoFixoFac[facilidades[index]] = c
    # print(custoFixoFac)

    capacFacilidade = {}
    for index, c in enumerate(facCapac):  # Cria o dicionario capacidade da facilidade j
        capacFacilidade[facilidades[index]] = c
    # print(capacFacilidade)

    custoTransCli = {}
    for index, a in enumerate(custoCli):
        custoTransCli[facilidades[index]] = a
    # print(custoTransCli)

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
    prob += lpSum(custoFixoFac[j] * use_vars[j] for j in facilidades) + lpSum(
        custoTransCli[j][i] * serv_vars[(i, j)] for j in facilidades for i in clientes)

    # Restrições
    for i in clientes:
        prob += lpSum(serv_vars[(i, j)] for j in facilidades) == demanda[i]  # RESTRIÇÃO 1

    for j in facilidades:
        prob += lpSum(serv_vars[(i, j)] for i in clientes) <= capacFacilidade[j] * use_vars[j]

    for i in clientes:
        for j in facilidades:
            prob += serv_vars[(i, j)] <= demanda[i] * use_vars[j]

    # Solução
    prob.solve()
   # print('Status:', LpStatus[prob.status])

    TOL = .00001
    # for i in facilidades:
    #     if use_vars[i].varValue > TOL:
    #         print('Abrir a facilidade', i)
    #
    # for v in prob.variables():
    #     print(v.name, '=', v.varValue)

    # Imprimir a solução ótima
    print(value(prob.status))
    #print('O custo da produção total sera = ', value(prob.objective))

    # CLIENTES = retorno[0]
    # FACILIDADES = retorno[1]
    # DEMANDA_CLIENTE = retorno[2]
    # CUSTO_LOCACAO_FACILIDADES = retorno[3]
    # CAPACIDADE_MAXIMA_FACILIDADES = retorno[4]
    # CUSTO_TRANSPORTE_CLIENTE = retorno[5]
    #
    #
    # #CLIENTES,FACILIDADES, DEMANDA_CLIENTE, CUSTO_LOCACAO_FACILIDADES, CAPACIDADE_MAXIMA_FACILIDADES, CUSTO_TRANSPORTE_CLIENTE
    #
    # # set problem variable
    # prob = LpProblem("FacilityLocation", LpMinimize)
    #
    # # decision variables
    # serv_vars = LpVariable.dicts("Service",
    #                              [(i, j) for i in CLIENTES
    #                               for j in FACILIDADES], 0)
    #
    # use_vars = LpVariable.dicts("UseLocatin", FACILIDADES, 0, 1, LpBinary)
    # # # Função Objetiva
   # prob += lpSum(CUSTO_LOCACAO_FACILIDADES[j] * use_vars[j] for j in FACILIDADES)
    #prob+= lpSum(CUSTO_TRANSPORTE_CLIENTE[j][i] * serv_vars[(i, j)] for j in FACILIDADES for i in CLIENTES)

   # print(CUSTO_TRANSPORTE_CLIENTE[0][0])
    #
    # # Restrições
    # for i in CLIENTES:
    #     prob += lpSum(serv_vars[(i, j)] for j in FACILIDADES) == DEMANDA_CLIENTE[i]  # 1º Restrição
    #
    # for j in FACILIDADES:
    #     prob += lpSum(serv_vars[(i, j)] for i in CLIENTES) <= CAPACIDADE_MAXIMA_FACILIDADES[j] * use_vars[j]
    #
    # for i in CLIENTES:
    #     for j in FACILIDADES:
    #         prob += serv_vars[(i, j)] <= DEMANDA_CLIENTE[i] * use_vars[j]
    #
    # # Solução
    # prob.solve()
    # print("Status", LpStatus[prob.status])
    #
    # TOL = .0001
    # for i in FACILIDADES:
    #     if use_vars[i].varValue > TOL:
    #         print("Estabelecer instalações", i)
    #
    # for v in prob.variables():
    #     print(v.name, " = ", v.varValue)
    #
    # # Print optinal Solutoion
    # print("O custo de producao em MOEDA NATIVA por um ano ", value(prob.objective))