import time
import sys


from Calculo.format import format
from Calculo.functionObjetive import functionObjetive
from In_Out.read import read_inst as le
from In_Out.write import write_file as escreve

t_inicio = time.time()

def main(inst):
    path = 'c:/Trabalho/LocFac/Instancias/' + inst
    #le(path)  # Extrai os dados da instancia

    functionObjetive(le(path))
#Teste

if __name__ == '__main__':
    main(str(sys.argv[1]))

t_total = time.time() - t_inicio
print('{:.4f}s'.format(t_total))
