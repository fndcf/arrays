#!/usr/bin/env python3

### chmod +x 'arquivo.py' (chmod é um comando para alterar a permissão de arquivos)

"""
Este script mostra  "none" caso não tenha nenhum parametro e caso tenha um ou mais parametros, mostra o primeiro.

Funcionamento do código:

1. Pega a quantidade de parametros, excluindo o nome do script
2. Imprime none caso não tenha nenhum parametro
3. Imprime o primeiro parametro caso tenha  um ou mais parametros 
"""

import sys

parameters = len(sys.argv) -1 # Pega a quantidade de parametros, excluindo o nome do script
if parameters == 0:
    print("none") # Imprime none caso não tenha nenhum parametro
else:
    print(f"{sys.argv[1]}") # Imprime o primeiro parametro caso tenha um ou mais parametros
