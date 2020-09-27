from pulp import *
def functionObjetive(retorno):

    CLIENTES = retorno[0]
    FACILIDADES = retorno[1]
    DEMANDA_CLIENTE = retorno[2]
    CUSTO_LOCACAO_FACILIDADES = retorno[3]
    CAPACIDADE_MAXIMA_FACILIDADES = retorno[4]
    CUSTO_TRANSPORTE_CLIENTE = retorno[5]


    #CLIENTES,FACILIDADES, DEMANDA_CLIENTE, CUSTO_LOCACAO_FACILIDADES, CAPACIDADE_MAXIMA_FACILIDADES, CUSTO_TRANSPORTE_CLIENTE

    # set problem variable
    prob = LpProblem("FacilityLocation", LpMinimize)

    # decision variables
    serv_vars = LpVariable.dicts("Service",
                                 [(i, j) for i in CLIENTES
                                  for j in FACILIDADES], 0)

    use_vars = LpVariable.dicts("UseLocatin", FACILIDADES, 0, 1, LpBinary)
    # # Função Objetiva
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