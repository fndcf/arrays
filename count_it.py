#!/usr/bin/env python3

### chmod +x 'arquivo.py' (chmod é um comando para alterar a permissão de arquivos)

"""
Este script mostra  "none" caso a quantidade de parametros seja igual a zero e apresenta os parametros seguidos do length de cada parametro digitado.

Funcionamento do código:

1. Cria uma variavel para os parametros passados
2. Pega a quantidade de parametros, excluindo o nome do script
3. Imprime none caso a quantidade de parametros seja igual a zero
4. Imprime a quantidade de parametros passados
5. Imprime parametro e a length em nova linha
"""

import sys

array_parameters = sys.argv[1:] # Cria um array para os parametros passados
parameters = len(sys.argv) -1 # Pega a quantidade de parametros, excluindo o nome do script

if parameters == 0:
    print("none") # Imprime none caso a quantidade de parametros seja igual a zero
else:
    print(f"parameters: {parameters}") # Imprime a quantidade de parametros passados
    for parameters_len in array_parameters:
        print(f"{parameters_len} {len(parameters_len)}") # Imprime cada parametro em uma nova linha