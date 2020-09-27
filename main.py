import time
import sys

from Calculo.format import format
from Calculo.functionObjetive import functionObjetive
from In_Out.read import readFile as le
from In_Out.write import write_file as escreve

t_inicio = time.time()

def main(inst):
    path = 'c:/Trabalho/LocFac/Instancias/' + inst
    dados = le(path)
    # print(dados)

    retorno = format(dados)
    functionObjetive(retorno)
#Teste

if __name__ == '__main__':
    main(str(sys.argv[1]))

t_total = time.time() - t_inicio
print('{:.4f}s'.format(t_total))
