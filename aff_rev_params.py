#!/usr/bin/env python3

### chmod +x 'arquivo.py' (chmod é um comando para alterar a permissão de arquivos)

"""
Este script mostra  "none" caso a quantidade de parametros seja menor que dois e apresenta os parametros ao contrario.

Funcionamento do código:

1. Pega a quantidade de parametros, excluindo o nome do script
2. Imprime none caso a quantidade de parametros seja menor que dois
3. Imprime os parametros ao contrario
"""

import sys

parameters = len(sys.argv) -1 # Pega a quantidade de parametros, excluindo o nome do script
if parameters < 2:
    print("none") # Imprime none caso a quantidade de parametros seja menor que dois
else:
    array_parameters = sys.argv[1:]
    array_parameters.reverse()

    for reverse_parameters in array_parameters:
        print(f"{reverse_parameters}") # Imprime cada parametro em uma nova linha