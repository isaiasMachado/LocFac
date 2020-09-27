from pulp import *
import numpy as np


def functionObjetive(dados):

    CLIENTES = []
    FACILIDADES = []
    DEMANDA_CLIENTE = []
    CUSTO_LOCACAO_FACILIDADES = []
    CAPACIDADE_MAXIMA_FACILIDADES = []
    CUSTO_TRANSPORTE_CLIENTE = []


    # Array com name facilidades
    cont = 0
    while cont < dados[5]:
        CLIENTES.append(cont+1)
        cont += 1

    #Array com name facilidades
    cont = 0
    while cont < dados[4]:
        FACILIDADES.append('FAC '+str(cont+1))
        cont +=1

    #Atribuindo as demanda
    cont = 0
    for d in dados[3]:
        cont +=1
        DEMANDA_CLIENTE.append({cont,d})

    #Atribuindo custo para cada facilidade
    cont = 0
    for cust in dados[0]:
        cont += 1;
        CUSTO_LOCACAO_FACILIDADES.append({'FAC '+str(cont),int(cust)})

    #   print(dict(CUSTO_LOCACAO_FACILIDADES))

    #Atribuindo capacidades para as facilidades
    cont = 0
    for cap in dados[1]:
        cont +=1
        CAPACIDADE_MAXIMA_FACILIDADES.append('FAC '+str(cont))
        CAPACIDADE_MAXIMA_FACILIDADES.append(int(cap))

    #print(maxam)
    #print(dict(CAPACIDADE_MAXIMA_FACILIDADES))

    # Inicializando os custo de tranporte pra cada cliente
    cont = 0
    for i in dados[2]:
        cont+=1
        cli = 0
        #CUSTO_TRANSPORTE_CLIENTE.append({'FAC '+str(cont)})
        for j in i:
            cli +=1
            CUSTO_TRANSPORTE_CLIENTE.append({cli, j})



    print(dict.fromkeys(CAPACIDADE_MAXIMA_FACILIDADES))


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

            # # set problem variable
            # prob = LpProblem("FACILIDADESLocation", LpMinimize)
            #
            # # decision variables
            # serv_vars = LpVariable.dict.fromkeyss("Service",
            #                                       [(i, j) for i in CLIENTES
            #                                        for j in FACILIDADES], 0)
            #
            # use_vars = LpVariable.dict.fromkeyss("UseLocatin", FACILIDADES, 0, 1, LpBinary)
            #
            # # Função Objetiva
            # prob += lpSum(dict.fromkeys(CUSTO_LOCACAO_FACILIDADES)[j] * use_vars[j] for j in FACILIDADES) + lpSum(
            #     dict.fromkeys(CUSTO_TRANSPORTE_CLIENTE)[j][i] * serv_vars[(i, j)] for j in FACILIDADES for i in
            #     CLIENTES)
            #
            # # Restrições
            # for i in CLIENTES:
            #     prob += lpSum(serv_vars[(i, j)] for j in FACILIDADES) == dict.fromkeys(DEMANDA_CLIENTE)[
            #         i]  # 1º Restrição
            #
            # for j in FACILIDADES:
            #     prob += lpSum(serv_vars[(i, j)] for i in CLIENTES) <= dict.fromkeys(CAPACIDADE_MAXIMA_FACILIDADES)[j] * \
            #             use_vars[j]
            #
            # for i in CLIENTES:
            #     for j in FACILIDADES:
            #         prob += serv_vars[(i, j)] <= dict.fromkeys(DEMANDA_CLIENTE)[i] * use_vars[j]
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