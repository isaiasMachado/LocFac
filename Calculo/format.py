from  pulp import *
def format(dados):

    # CLIENTES = []
    # FACILIDADES = []
    # DEMANDA_CLIENTE = {}
    # CUSTO_LOCACAO_FACILIDADES = {}
    # CAPACIDADE_MAXIMA_FACILIDADES = {}
    # CUSTO_TRANSPORTE_CLIENTE = {}
    #
    # print(dados)
    # # Array TODOS ID CLIENTES
    # cont = 0
    # while cont < dados[5]:
    #     CLIENTES.append(cont+1)
    #     cont += 1
    #
    # #Array com name facilidades
    # cont = 0
    # while cont < dados[4]:
    #     FACILIDADES.append('FAC '+str(cont+1))
    #     cont +=1
    #
    # #Atribuindo as demanda
    # for index,d in enumerate(dados[3]):
    #     DEMANDA_CLIENTE[index+1] = dados[3][index]
    #
    # #Atribuindo custo para cada facilidade
    # for index,cust in enumerate(dados[0]):
    #     CUSTO_LOCACAO_FACILIDADES['FAC '+str(index+1)] = int(dados[0][index])
    #
    # #Atribuindo capacidades para as facilidades
    # for index,cap in enumerate(dados[1]):
    #     CAPACIDADE_MAXIMA_FACILIDADES['FAC '+str(index+1)] = int(dados[1][index])
    #
    # # Inicializando os custo de tranporte pra cada cliente
    # aux = {}
    # aux2 = []
    # for ind,custos in enumerate(dados[2]):
    #     if len(aux) == 50:
    #         CUSTO_TRANSPORTE_CLIENTE['FAC ' + str(ind)] = aux;
    #         aux2.append(CUSTO_TRANSPORTE_CLIENTE)
    #
    #     for index,itens in enumerate(custos):
    #         aux[index+1] = itens
    #
    # m = []
    # m1 = []
    # for i in dados[2]:
    #     for j in i:
    #         m1.append(float(input(j)))
    #     m.append(m1)
    #     m1 = []
    #
    # print(m)
    # #print(CUSTO_TRANSPORTE_CLIENTE[0])
    # #FACILIDADES, DEMANDA_CLIENTE, CUSTO_LOCACAO_FACILIDADES, CAPACIDADE_MAXIMA_FACILIDADES, CUSTO_TRANSPORTE_CLIENTE)
    #
    # return CLIENTES,FACILIDADES, DEMANDA_CLIENTE, CUSTO_LOCACAO_FACILIDADES, CAPACIDADE_MAXIMA_FACILIDADES, CUSTO_TRANSPORTE_CLIENTE
    #
    #

    facCust, facCapac, custoCli, cliDema = dados  # Extrai os dados da instancia

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
    print('Status:', LpStatus[prob.status])

    TOL = .00001
    for i in facilidades:
        if use_vars[i].varValue > TOL:
            print('Abrir a facilidade', i)

    for v in prob.variables():
        print(v.name, '=', v.varValue)

    # Imprimir a solução ótima
    print('O custo da produção total sera = ', value(prob.objective))

# escreve(dados, inst)
    # CUSTOMERS = [1,2,3,4,5]
    # FACILITY = ['FAC 1', 'FAC 2', 'FAC 3']
    #
    # demanda = {1 : 80,
    #            2 : 270,
    #            3 : 250,
    #            4 : 160,
    #            5 : 180}
    #
    # actcost = {'FAC 1':1000,
    #            'FAC 2':1000,
    #            'FAC 3':1000}
    #
    # maxam = {'FAC 1':500,
    #          'FAC 2':500,
    #          'FAC 3':500}
    #
    # transp ={'FAC 1':{1 : 4, 2 : 5, 3 : 6, 4 : 8, 5 : 10},
    #          'FAC 2':{1 : 6, 2 : 4, 3 : 3, 4 : 5, 5 : 8},
    #          'FAC 3':{1 : 9, 2 : 7, 3 : 4, 4 : 3, 5 : 4}}
    #
    # #set problem variable
    # prob = LpProblem("FacilityLocation",LpMinimize)
    #
    # #decision variables
    # serv_vars = LpVariable.dicts("Service",
    #                              [(i,j) for i in CUSTOMERS
    #                                     for j in  FACILITY],0)
    #
    # use_vars = LpVariable.dicts("UseLocatin",FACILITY,0,1,LpBinary)
    #
    # #Função Objetiva
    # prob += lpSum(actcost[j]*use_vars[j] for j in FACILITY) + lpSum(transp[j][i]*serv_vars[(i,j)] for j in FACILITY for i in CUSTOMERS)
    #
    # #Restrições
    # for i in CUSTOMERS:
    #     prob += lpSum(serv_vars[(i,j)] for j in FACILITY) == demanda[i] #1º Restrição
    #
    # for j in FACILITY:
    #     prob += lpSum(serv_vars[(i,j)] for i in CUSTOMERS) <= maxam[j]*use_vars[j]
    #
    # for i in CUSTOMERS:
    #     for j in FACILITY:
    #         prob += serv_vars[(i,j)] <= demanda[i]*use_vars[j]
    #
    # #Solução
    # prob.solve()
    # print("Status", LpStatus[prob.status])
    #
    # TOL = .0001
    # for i in FACILITY:
    #     if use_vars[i].varValue > TOL:
    #         print("Estabelecer instalações",i)
    #
    #
    # for v in prob.variables():
    #     print(v.name, " = ", v.varValue)
    #
    #
    # #Print optinal Solutoion
    # print("O custo de producao em MOEDA NATIVA por um ano ",value(prob.objective))

