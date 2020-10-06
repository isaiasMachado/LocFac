import numpy as np
import math


def le_instancia(nome):
    nroFac = 0
    nroCli = 0
    capFac = []
    custoFac = []
    demaCli = []
    dist_a_fac = []
    with open(nome, mode='r') as fp:

        problem_size = fp.readline().split()
        nroFac = int(problem_size[0])
        nroCli = int(problem_size[1])

        for i in range(0, nroFac):
            facility_info = fp.readline().split()
            capFac.append(int(facility_info[0]))
            custoFac.append(int(facility_info[1]))

        while len(demaCli) < nroCli:
            demand_info = fp.readline().split()
            for i in range(0, len(demand_info)):
                demaCli.append(float(demand_info[i]))

        distance_infos = []
        while len(distance_infos) < nroFac:
            distance_info = []
            while len(distance_info) < nroCli:
                temp = fp.readline().split()
                for i in range(0, len(temp)):
                    distance_info.append(float(temp[i]))
            distance_infos.append(distance_info)
        dist_a_fac = np.array(distance_infos).transpose()

    return nroFac, nroCli, capFac, custoFac, demaCli, dist_a_fac

