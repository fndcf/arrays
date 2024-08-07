#!/usr/bin/env python3

### chmod +x 'arquivo.py' (chmod é um comando para alterar a permissão de arquivos)

"""
Este script mostra  "none" caso a quantidade de parametros seja diferente de um, caso tenha apenas um parametro mostrar em letra minuscula.

Funcionamento do código:

1. Pega a quantidade de parametros, excluindo o nome do script
2. Imprime none caso a quantidade de parametros seja diferente de um
3. Imprime o primeiro parametro em letra minuscula
"""

import sys

parameters = len(sys.argv) -1 # Pega a quantidade de parametros, excluindo o nome do script
if parameters != 1:
    print("none") # Imprime none caso a quantidade de parametros seja diferente de um
else:
    print(f"{sys.argv[1].lower()}") # Imprime o primeiro parametro em letra minuscula