import random
import math
from math import inf
import datetime
import os
import numpy as np
from Construtiva import estratGulosa
from Entrada.leitura import le_instancia as le


tam_loop = 1000     # Condição de parada
temp_max = 100      # Parâmetro da temperatura: usado no SA
temp_min = 0.5      # Parâmetro da temperatura: usado no SA
coeficient_atenuacao = 0.99     # Parâmetro da temperatura: usado no SA

limite = 10
tam_populacao = 5

random.seed(7)

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

        self.lista_fac_abertas = [0]*self.num_fac    # [0 for _ in range(self.num_fac)]
        self.aloc_cli = []   # Aqui é inserido o número da facilidade que vai atender o cliente da posição do array
        self.custo_total = 0

        self.temperatura = temp_max

    def aloc_inicial_cliente(self):
        for i in range(0, self.num_cli):
            while True:
                fac_escolhida = random.randint(0, self.num_fac - 1)
                if self.cap_fac[fac_escolhida] >= self.deman_cli[i]:    # Caso a fabrica não atenda sorteia-se outra até que seja encontrada uma que sirva
                    if self.lista_fac_abertas[fac_escolhida] == 0:
                        self.custo_total += self.custo_abert_fac[fac_escolhida]
                    self.lista_fac_abertas[fac_escolhida] += 1
                    self.cap_fac[fac_escolhida] -= self.deman_cli[i]
                    self.custo_total += self.dist_a_fac[i][fac_escolhida]
                    self.aloc_cli.append(fac_escolhida)
                    break   # Caso a fabrica atenda o cliente em questão, vai para o próximo cliente.

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
                for i in range(0, len(temp)):   # Transfere cada linha lida do arquivo para um vetor
                    info_dist.append(float(temp[i]))
            informs_distancia.append(info_dist)     # Idêntica à instancia
        self.dist_a_fac = np.array(informs_distancia).transpose()

    def write_file(self):
        fp = open('Solução do Simulated Annealing/Resultado para ' + self.nomeInstancia.split('/')[2], 'w')
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
                continue  # É a própria fabrica em vez da vizinha.
            if self.cap_fac[fac_escolhida] < self.deman_cli[cli_escolhido]:
                continue  # A troca foi rejeitada porque a facilidade alvo tinha capacidade insuficiente
            # A operação de troca pode ser realizada se o custo total for reduzido, aceita-se a solução vizinha. O custo total inclui o custo da distância até o cliente + o custo de abertura da fábrica
            fac_alocada_antes = self.aloc_cli[cli_escolhido]
            custo_antes = self.dist_a_fac[cli_escolhido][fac_alocada_antes]
            if self.lista_fac_abertas[fac_alocada_antes] == 1:
                custo_antes += self.custo_abert_fac[fac_alocada_antes]
            custo_apos = self.dist_a_fac[cli_escolhido][fac_escolhida]
            if self.lista_fac_abertas[fac_escolhida] == 0:
                custo_apos += self.custo_abert_fac[fac_escolhida]

            if custo_antes <= custo_apos and \
                    random.random() > math.exp((custo_antes - custo_apos)/self.temperatura):
                return False

            self.cap_fac[fac_alocada_antes] += self.deman_cli[cli_escolhido]
            self.cap_fac[fac_escolhida] -= self.deman_cli[cli_escolhido]

            self.lista_fac_abertas[fac_alocada_antes] -= 1
            self.lista_fac_abertas[fac_escolhida] += 1

            self.aloc_cli[cli_escolhido] = fac_escolhida
            self.custo_total = self.custo_total - custo_antes + custo_apos

            return True


    def solve(self):
        self.aloc_inicial_cliente()
        print('Usando recozimento simulado, custo do plano de alocação inicial：', self.custo_total)
        while self.temperatura > temp_min:
            for i in range(0, tam_loop):
               if self.gera_vizinho_pela_troca_facilidade():
                    print('Usando recozimento simulado, temperatura atual：', self.temperatura, '，Ciclo', i, 'Aceite a nova solução vizinha e atualize o custo para：', self.custo_total)
            self.temperatura *= coeficient_atenuacao
        self.write_file()
        return self.custo_total

# =====================================================================================================================
# GA - Genetic algorithm

class GA:

    def __init__(self, nomeInstancia,pastaInstDesejada):
        self.nomeInstancia = nomeInstancia
        self.pastaInstDesejada = pastaInstDesejada
        self.num_fac = 0
        self.num_cli = 0
        self.cap_fac = []
        self.custo_abert_fac = []
        self.deman_cli = []
        self.dist_a_fac = []
        self.read_file()

        self.lista_fac_abertas = [0]*self.num_fac    # [0 for _ in range(self.num_fac)]
        # print(self.lista_fac_abertas)
        self.aloc_cli = []   # Aqui é inserido o número da facilidade que vai atender o cliente da posição do array
        self.custo_total = 0

        self.geracao = 0
        self.populacao = []

    def aloc_inicial_cliente(self):
            for i in range(0, self.num_cli):
                while True:
                    fac_escolhida = random.randint(0, self.num_fac - 1)
                    if self.cap_fac[fac_escolhida] >= self.deman_cli[i]:    # Caso a fabrica não atenda sorteia-se outra até que seja encontrada uma que sirva
                        if self.lista_fac_abertas[fac_escolhida] == 0:
                            self.custo_total += self.custo_abert_fac[fac_escolhida]
                            self.lista_fac_abertas[fac_escolhida] += 1
                        self.cap_fac[fac_escolhida] -= self.deman_cli[i]
                        self.custo_total += self.dist_a_fac[i][fac_escolhida]
                        self.aloc_cli.append(fac_escolhida)
                        break   # Caso a fabrica atenda o cliente em questão, vai para o próximo cliente.

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
                for i in range(0, len(temp)):   # Transfere cada linha lida do arquivo para um vetor
                    info_dist.append(float(temp[i]))
            informs_distancia.append(info_dist)     # Idêntica à instancia
        self.dist_a_fac = np.array(informs_distancia).transpose()

    def write_file(self):
        fp = open('Solução do Genetic algorithm/Resultado para ' + self.nomeInstancia.split('/')[2], 'w')
        fp.write(str(self.custo_total) + '\n')
        for i in range(0, self.num_fac):
            if self.lista_fac_abertas[i] != 0:
                fp.write('1 ')
            else:
                fp.write('0 ')
        fp.write('\n')
        for i in range(0, self.num_cli):
            fp.write(str(self.aloc_cli[i]) + ' ')

    def gera_populacao(self):
        while len(self.populacao) < tam_populacao:
            cromossomo_aux = []
            for i in range(0, self.num_cli):
                gene_aleat = random.randint(0, self.num_fac-1)
                cromossomo_aux.append(gene_aleat)
            self.populacao.append(cromossomo_aux)
        #print(self.populacao)

    def capacidade_cada_facilidade(self):
        caminho = 'c:/Trabalho/LocFac/'+ self.nomeInstancia

        capFac = []
        # print(caminho)
        with open(caminho, mode='r') as fp:
            problem_size = fp.readline().split()
            nroFac = int(problem_size[0])
            for i in range(0, nroFac):
                facility_info = fp.readline().split()
                capFac.append(int(facility_info[0]))

        return capFac

    # def calcula_custo(self):
    #     cont = 0
    #     custoTotal = 0
    #     listaFacAbertas = [0] * self.num_fac
    #     nroCli = self.num_cli
    #     sequenciaFacilidades =[0, 12, 0, 0, 12, 12, 12, 12, 12, 12, 0, 12, 12, 12, 13, 13, 0, 0, 13, 9, 13, 13, 0, 13, 9, 13, 0, 1, 1, 1, 13, 1, 1, 1, 1, 9, 1, 13, 19, 19, 9, 5, 5, 5, 9, 5, 5, 9, 19, 9]
    #     demaCli = self.deman_cli
    #     dist_a_cli = self.dist_a_fac
    #     custoFac = self.custo_abert_fac
    #     vetAux = self.capacidade_cada_facilidade()
    #
    #     for i in range(0, nroCli):
    #         while True:
    #             fac_selecionada = sequenciaFacilidades[cont]
    #             cont += 1
    #             if vetAux[fac_selecionada] >= demaCli[i]:
    #                 if listaFacAbertas[fac_selecionada] == 0:
    #                     custoTotal += custoFac[fac_selecionada]
    #                 listaFacAbertas[fac_selecionada] += 1
    #                 vetAux[fac_selecionada] -= demaCli[i]
    #                 custoTotal += dist_a_cli[i][fac_selecionada]
    #                 break
    #             else:
    #                 cont -= 1
    #                 break
    #
    #     return custoTotal

    def calcula_custo(self, seq):

        cont = 0
        custoTotal = 0
        listaFacAbertas = [0] * self.num_fac
        nroCli = self.num_cli
        sequenciaFacilidades = seq
        demaCli = self.deman_cli
        dist_a_cli = self.dist_a_fac
        custoFac = self.custo_abert_fac
        vetAux = self.capacidade_cada_facilidade()

        for i in range(0, nroCli):
            while True:
                fac_selecionada = sequenciaFacilidades[cont]
                cont += 1
                if vetAux[fac_selecionada] >= demaCli[i]:
                    if listaFacAbertas[fac_selecionada] == 0:
                        custoTotal += custoFac[fac_selecionada]
                    listaFacAbertas[fac_selecionada] += 1
                    vetAux[fac_selecionada] -= demaCli[i]
                    custoTotal += dist_a_cli[i][fac_selecionada]
                    break
                else:
                    cont -= 1
                    break

        return custoTotal

    def avaliacao(self):
        vetAux = self.populacao
        avaliacoes = []
        for i in range(0,len(vetAux)) :
            avaliacoes.append(self.calcula_custo( vetAux[i]))

        print(avaliacoes)
        print(sorted(avaliacoes))
        print(avaliacoes.index(sorted(avaliacoes)[0]))
        print(vetAux[avaliacoes.index(sorted(avaliacoes)[0])])
        # dicionario = []
        # for i in range(0,len(avaliacoes)):
        #     dicionario.append(vetAux[i])
        #     dicionario.append(avaliacoes[i])

        #print(dicionario)

    def solve(self):
        notasIndividuos = []
        self.aloc_inicial_cliente()
        self.gera_populacao()   # Gera população inicial aleatoriamente
        #self.calcula_custo()
        self.avaliacao()
        # while self.geracao < limite:
        #     self.geracao += 1
        #     for i in range(0, len(self.populacao)):
        #         notasIndividuos.append(self.avaliacao(self.populacao[i]))
            # print(notasIndividuos)

        self.write_file()
        return self.custo_total

# =====================================================================================================================

def main():
    pastaInstDesejada = input('Digite o nome da instancia que deseja rodar: ')
    numero_instancia = int(input('Digite o tamanho da instancia: '))

    print('S-METAHEURISTICA')
    print('Fornece as seguintes soluções ')
    print('1 Reserva 1')
    print('2 Recozimento simulado')
    print('3 Algoritmo genético')
    command = input('Digite o algoritmo que deseja usar: ')

    write_file_name = ''
    if command == '1':
        pass
    elif command == '2':
        write_file_name = 'Tabela dos resultados do Simulated Annealing'
    elif command == '3':
        write_file_name = 'Tabela dos resultados do GA'
    fp = open(write_file_name, 'a')
    if os.stat(write_file_name).st_size == 0:
        fp.write(''.ljust(10) + 'Resultado'.ljust(20) + 'Tempo(s)\n')

    for i in range(1, numero_instancia+1):
        nomeInstancia = 'Instancias/' + pastaInstDesejada + '/p' + str(i)
        res = 0
        start_time = datetime.datetime.now()
        if command == '1':
            pass
        elif command == '2':
            solution2 = SA(nomeInstancia)
            res = solution2.solve()
        elif command == '3':
            # pass
            solution3 = GA(nomeInstancia,pastaInstDesejada )
            res = solution3.solve()
        end_time = datetime.datetime.now()
        fp.write(('p' + str(i)).ljust(10) + str(res).ljust(20) + str((end_time - start_time).seconds) + '\n')


if __name__ == '__main__':
    main()
