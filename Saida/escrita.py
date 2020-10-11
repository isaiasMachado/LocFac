import csv


def saveResultsTXT(instName, listaFacAbertas, alocacao_do_cliente, custoTotal,tipo):
    with open('Resultados/'+tipo +'/' + instName + '.txt', mode='w') as fp:
        fp.write("Custo Total: " + str(custoTotal) + " | ");
        fp.write('Qtd Facilidades abertas: ' + str(listaFacAbertas) + ' | ');
        fp.write('Sequencias de facilidades abertas: ' + str(alocacao_do_cliente) + ' | ');


def saveResultsCSV(instName, listaFacAbertas, alocacao_do_cliente, custoTotal,tipo,estrategia):
    caminho = 'Resultados/'+tipo +'/' +estrategia + '/'  + instName + '.csv';

    row_list = [["Custo", "Qtd Facilidades Abertas", "Sequencia das facilidades abertas"],
                [custoTotal, str(listaFacAbertas), str(alocacao_do_cliente)]]
    with open(caminho, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(row_list)
