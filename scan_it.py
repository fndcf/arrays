#!/usr/bin/env python3

### chmod +x 'arquivo.py' (chmod é um comando para alterar a permissão de arquivos)

"""
Este script mostra  "none" caso a quantidade de parametros seja diferente de dois, e imprime o quantidade que aparece a palavra do primeiro parametro.

Funcionamento do código:

1. Pega a quantidade de parametros, excluindo o nome do script
2. Imprime none caso a quantidade de parametros seja diferente de dois
3. Cria uma variavel com o primeiro parametro
4. Cria uma variavel com o segundo parametro
5. Imprime a quantidade de vezes que aparece a palavra do primeiro parametro
"""

import sys
import re

parameters = len(sys.argv) -1 # Pega a quantidade de parametros, excluindo o nome do script
if parameters != 2:
    print("none") # Imprime none caso a quantidade de parametros seja diferente de dois
else:
    first_params = sys.argv[1] # Cria uma variavel com o primeiro parametro
    second_params = sys.argv[2] # Cria uma variavel com o segundo parametro
    if first_params not in second_params:
        print("none") # Imprime none caso o primeiro parametro não esteja no segundo
    else:   
        result = re.findall(first_params, second_params) # Faz uma busca da palavra do primeiro parametro no segundo parametro
        print(len(result) + 1) # Imprime a quantidade que aparece a palavra do primeiro parametro
