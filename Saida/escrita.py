import csv
import sys

def saveResultsTXT(instName, listaFacAbertas, alocacao_do_cliente, custoTotal, tempo, tipo, estrategia):
    aux = ''
    with open('Resultados/' + tipo + '/' + estrategia + '/' + instName, mode='w') as fp:
        fp.write(tempo + '\n')
        fp.write(str(custoTotal) + '\n')
        fp.write(str(listaFacAbertas) + '\n')
        for i in alocacao_do_cliente:
            aux += str(i)+ ', ';
        aux = aux[:-2]
        fp.write('['+aux+']')



def saveResultsCSV(instName, listaFacAbertas, alocacao_do_cliente, custoTotal, tempo, tipo, estrategia):
    caminho = 'Resultados/' + tipo + '/' + estrategia + '/' + instName + '.csv';
    # row_list = [[" Custo", " Tempo", " Qtd Facilidades Abertas", " Sequencia das facilidades abertas"],
    #             [custoTotal, tempo, str(listaFacAbertas), str(alocacao_do_cliente)]]
    row_list = [[instName, custoTotal, tempo, str(listaFacAbertas), str(alocacao_do_cliente)]]
    with open(caminho, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(row_list)

def exibeResultado(caminho):
    result = open(caminho + 'Result.md', 'w')
    nameBase = caminho + '/p'
    result.write('|Inst.| Result | Times(s)|\n')
    result.write('|-----|--------|---------|\n')
    for index in range(1, 72):       # Alterar o range quando quiser fazer testes
        minCost = sys.maxsize
        minUsedTime = sys.maxsize
        for i in range(1, 4):
            with open(nameBase + str(index), 'r') as f:
                usedTimes = f.readline()
                cost = float(f.readline())
                if cost < minCost:
                    minCost = cost
                    minUsedTime = usedTimes
        result.write('|  p' + str(index) + ' |' + str(format(minCost, '.2f')) + '|' + str(minUsedTime))
    result.close()

def comparaResultados(caminho):
    resultComparacao = open('resultComparacao.md', 'w')
    fileNames = ['Resultados/Construtiva/Gulosa/Result.md', 'Resultados/Construtiva/Aleatoria/Result.md', 'Resultados/Refinamento/Aleatoria/Result.md']
    resultComparacao.write('| Gulosa | Tempo(s) \n| Aleatoria | Tempo(s)\n| Refinamento | Tempo(s)\n')
    resultComparacao.write('\n')

    files = [open(fileNames[i]) for i in range(3)]
    fileLines = [files[i].readlines() for i in range(3)]
    print(fileLines)

    for i in range(2, len(fileLines[0])):
        resultComparacao.write(fileLines[0][i])
        resultComparacao.write(fileLines[1][i])
        resultComparacao.write(fileLines[2][i])
        # resultComparacao.write(fileLines[3][i])
        resultComparacao.write('\n\n')

    for file in files:
        file.close()