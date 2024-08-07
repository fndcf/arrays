#!/usr/bin/env python3

### chmod +x 'arquivo.py' (chmod é um comando para alterar a permissão de arquivos)

"""
Este script mostra a quantidade de parametros passados.

Funcionamento do código:

1. Pega a quantidade de parametros, excluindo o nome do script
2. Imprime a quantidade de parametros
"""

import sys

num_parameters = len(sys.argv) - 1 # Pega a quantidade de parametros, excluindo o nome do script
print(f"Number of parameters: {num_parameters}.") # Imprime a quantidade de parametros
