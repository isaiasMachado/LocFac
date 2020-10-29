import random
import math
import datetime
import os
import numpy as np
import time

numero_instancia = 4
tam_loop = 1000
temp_max = 100
temp_min = 0.5
coeficient_atenuacao = 0.99
num_max = 100000000


class SA:

    def __init__(self, nomeInstancia):
        self.nomeInstancia = nomeInstancia
        self.num_fac = 0
        self.num_cli = 0
        self.cap_fac = []
        self.custo_abert_fac = []
        self.deman_cli = []
        self.dist_a_fac = []
        self.read_file()

        self.lista_fac_abertas = [0]*self.num_fac
        self.aloc_cli = []
        self.custo_total = 0

        self.temperatura = temp_max

    def aloc_inicial_cliente(self):
        for i in range(0, self.num_cli):
            while True:
                fac_escolhida = random.randint(0, self.num_fac - 1)
                if self.cap_fac[fac_escolhida] >= self.deman_cli[i]:
                    if self.lista_fac_abertas[fac_escolhida] == 0:
                        self.custo_total += self.custo_abert_fac[fac_escolhida]
                    self.lista_fac_abertas[fac_escolhida] += 1
                    self.cap_fac[fac_escolhida] -= self.deman_cli[i]
                    self.custo_total += self.dist_a_fac[i][fac_escolhida]
                    self.aloc_cli.append(fac_escolhida)
                    break

    def read_file(self):
        fp = open(self.nomeInstancia)
        tam_problema = fp.readline().split()
        self.num_fac = int(tam_problema[0])
        self.num_cli = int(tam_problema[1])

        for i in range(0, self.num_fac):
            infor_fac = fp.readline().split()
            self.cap_fac.append(int(infor_fac[0]))
            self.custo_abert_fac.append(int(infor_fac[1]))

        while len(self.deman_cli) < self.num_cli:
            infor_demanda = fp.readline().split()
            for i in range(0, len(infor_demanda)):
                self.deman_cli.append(float(infor_demanda[i]))

        informs_distancia = []
        while len(informs_distancia) < self.num_fac:
            info_dist = []
            while len(info_dist) < self.num_cli:
                temp = fp.readline().split()
                for i in range(0, len(temp)):
                    info_dist.append(float(temp[i]))
            informs_distancia.append(info_dist)
        for i in range(0, self.num_cli):
            temp_dist = []
            for j in range(0, self.num_fac):
                temp_dist.append(informs_distancia[j][i])
            self.dist_a_fac.append(temp_dist)

    def write_file(self):
        fp = open('Solucao do Simulated Annealing/Resultado para ' + self.nomeInstancia.split('/')[2], 'w')
        fp.write(str(self.custo_total) + '\n')
        for i in range(0, self.num_fac):
            if self.lista_fac_abertas[i] != 0:
                fp.write('1 ')
            else:
                fp.write('0 ')
        fp.write('\n')
        for i in range(0, self.num_cli):
            fp.write(str(self.aloc_cli[i]) + ' ')

    def gera_vizinho_pela_troca_facilidade(self):
        while True:
            cli_escolhido = random.randint(0, self.num_cli - 1)
            fac_escolhida = random.randint(0, self.num_fac - 1)
            if self.aloc_cli[cli_escolhido] == fac_escolhida:
                continue  # 产生的是这个点本身而不是邻居，重来
            if self.cap_fac[fac_escolhida] < self.deman_cli[cli_escolhido]:
                continue  # 交换被拒绝，因为目标工厂容量不足
            # 交换操作可进行，计算总花费是否减少，如果减少则接受邻居解，总花费包括 到工厂距离+开工厂费用
            fac_alocada_antes = self.aloc_cli[cli_escolhido]
            # print('尝试操作：将顾客', choose_customer, '从工厂', allocated_facility_before, '转到工厂', choose_facility)
            custo_antes = self.dist_a_fac[cli_escolhido][fac_alocada_antes]
            if self.lista_fac_abertas[fac_alocada_antes] == 1:
                custo_antes += self.custo_abert_fac[fac_alocada_antes]
            custo_apos = self.dist_a_fac[cli_escolhido][fac_escolhida]
            if self.lista_fac_abertas[fac_escolhida] == 0:
                custo_apos += self.custo_abert_fac[fac_escolhida]

            if custo_antes <= custo_apos and \
                    random.random() > math.exp((custo_antes - custo_apos) / self.temperatura):
                return False

            self.cap_fac[fac_alocada_antes] += self.deman_cli[cli_escolhido]
            self.cap_fac[fac_escolhida] -= self.deman_cli[cli_escolhido]

            self.lista_fac_abertas[fac_alocada_antes] -= 1
            self.lista_fac_abertas[fac_escolhida] += 1

            self.aloc_cli[cli_escolhido] = fac_escolhida
            self.custo_total = self.custo_total - custo_antes + custo_apos

            return True

    def gera_vizinho_por_troca_cliente(self):
        while True:
            cliente_1 = random.randint(0, self.num_cli - 1)
            cliente_2 = random.randint(0, self.num_cli - 1)
            custo_fac_1 = self.aloc_cli[cliente_1]
            custo_fac_2 = self.aloc_cli[cliente_2]
            if cliente_1 == cliente_2 or custo_fac_1 == custo_fac_2:
                continue  # 产生的是这个点本身而不是邻居，重来
            if self.cap_fac[custo_fac_1] + self.deman_cli[cliente_1] - \
                    self.deman_cli[cliente_2] < 0 or self.cap_fac[custo_fac_2] + \
                    self.deman_cli[cliente_2] - self.deman_cli[cliente_1] < 0:
                continue  # 交换被拒绝，有一个工厂的容量不足
            # 交换操作可进行，计算总花费是否减少，如果减少则接受邻居解，总花费仅仅包括到工厂距离
            custo_antes = self.dist_a_fac[cliente_1][custo_fac_1] \
                          + self.dist_a_fac[cliente_2][custo_fac_2]
            custo_apos = self.dist_a_fac[cliente_1][custo_fac_2] \
                         + self.dist_a_fac[cliente_2][custo_fac_1]
            if custo_antes <= custo_apos and \
                    random.random() > math.exp((custo_antes - custo_apos) / custo_antes / self.temperature):
                return False

            self.cap_fac[custo_fac_1] = self.cap_fac[custo_fac_1] + \
                                                     self.deman_cli[cliente_1] - self.deman_cli[cliente_2]
            self.cap_fac[custo_fac_2] = self.cap_fac[custo_fac_2] + \
                                                     self.deman_cli[cliente_2] - self.deman_cli[cliente_1]
            self.aloc_cli[cliente_1] = custo_fac_2
            self.aloc_cli[cliente_2] = custo_fac_1
            self.custo_total = self.custo_total - custo_antes + custo_apos

            return True


    def solve(self):
        self.aloc_inicial_cliente()
        print('使用模拟退火，初始分配方案花费：', self.custo_total)
        while self.temperatura > temp_min:
            for i in range(0, tam_loop):
                # if i % 3 != 0:
                #     if self.generate_neighbor_by_swap_customer():
                #         print('使用模拟退火，当前温度：', self.temperatura, '，第', i, '循环 ', '接受新的邻居解,花费更新为：', self.custo_total)
                #     continue
                if self.gera_vizinho_pela_troca_facilidade():
                    print('使用模拟退火，当前温度：', self.temperatura, '，第', i, '循环 ', '接受新的邻居解,花费更新为：', self.custo_total)
            self.temperatura *= coeficient_atenuacao
        self.write_file()
        return self.custo_total

def main():
    pastaInstDesejada = input('Digite o nome da instancia que deseja rodar:')
    print('S-METAHEURISTICA')
    print('Fornece as seguintes soluções ')
    # print('1 Pesquisa local')
    print('2 Recozimento simulado')
    # print('3 Pesquisa tabu')
    command = input('Digite o algoritmo que deseja usar:')
    write_file_name = ''
    if command == '1':
        write_file_name = 'Result Table Of Local Search'
    elif command == '2':
        write_file_name = 'Tabela dos resultados do Simulated Annealing'
    elif command == '3':
        write_file_name = 'Result Table Of Tabu Search'
    fp = open(write_file_name, 'a')
    if os.stat(write_file_name).st_size == 0:
        fp.write(''.ljust(10) + 'Resultado'.ljust(20) + 'Tempo(s)\n')

    for i in range(1, numero_instancia+1):
        nomeInstancia = 'Instancias/' + pastaInstDesejada + '/p' + str(i)
        res = 0
        start_time = datetime.datetime.now()
        if command == '1':
            pass
            # solution1 = LocalSearchSol(filename)
            # res = solution1.solve()
        elif command == '2':
            solution2 = SA(nomeInstancia)
            res = solution2.solve()
        elif command == '3':
            pass
            # solution3 = TabuSearch(filename)
            # res = solution3.solve()
        end_time = datetime.datetime.now()
        fp.write(('p' + str(i)).ljust(10) + str(res).ljust(20) + str((end_time - start_time).seconds) + '\n')


if __name__ == '__main__':
    main()
