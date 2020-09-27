# def read_inst(nome):
#
#     facCapac = []
#     facCust = []
#     cliDema = []
#     with open(nome, mode='r') as fp:
#
#         tamInst = fp.readline().split()
#         facQtd = int(tamInst[0])
#         cliQtd = int(tamInst[1])
#
#         for f in range(0, facQtd):
#             facInfo = fp.readline().split()
#             facCapac.append(int(facInfo[0]))
#             facCust.append(int(facInfo[1]))
#
#         for c in range(0, cliQtd):
#             demaInfo = fp.readline().split()
#             for i in range(0, len(demaInfo)):
#                 cliDema.append(float(demaInfo[i]))
#     inst_lidas = {'nroFac': facQtd, 'nroCli': cliQtd, 'demanda': cliDema}
#     return inst_lidas
import math
import numpy as np

def readFile(fileName):
    f_fixed = []
    f_capacities = []
    c_costs = []
    c_demand = []
    with open(fileName, "r") as f:
        nLocations, nClients = f.readline().strip().split()
        nLocations = int(nLocations)
        nClients = int(nClients)

        for _ in range(nLocations):
            b_i, f_i = f.readline().strip().split()
            f_fixed.append(float(f_i))
            f_capacities.append(float(b_i))
        for _ in range(nClients):
            demand = int(f.readline().strip())
            c_demand.append(demand)
            lines = math.ceil(nLocations / 7)
            clientsCost = []
            for _ in range(lines):
                line = f.readline().strip().split()
                clientsCost += line
            clientsCost = np.array([float(x) for x in clientsCost])
            c_costs.append(clientsCost)

    f_fixed = np.array(f_fixed)
    f_capacities = np.array(f_capacities)
    c_costs = np.array(c_costs).transpose()
    c_demand = np.array(c_demand)

    return f_fixed, f_capacities, c_costs, c_demand,nLocations,nClients