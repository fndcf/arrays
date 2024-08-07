#!/usr/bin/env python3

### chmod +x 'arquivo.py' (chmod é um comando para alterar a permissão de arquivos)

"""
Este script mostra "none" caso a quantidade de parametros seja diferente de dois
e cria um array entre o primeiro e o segundo parametro.

Funcionamento do código:

1. Cria um array com os parametros passados
2. Pega a quantidade de parametros, excluindo o nome do script
3. Imprime none caso a quantidade de parametros seja diferente de dois
4. Imprime um array entre o primeiro e o segundo parametro
"""

import sys

array_parameters = sys.argv[1:]   # Cria um array para os parametros passado
parameters = len(sys.argv) - 1  # Pega a quantidade de parametros, excluindo o nome do script
if parameters != 2:
    print("none")
else:
    try:
        first_param = int(sys.argv[1])  # Converte o primeiro parametro para inteiro
        second_param = int(sys.argv[2]) # Converte o segundo parametro para inteiro
        
        
        array_completo = list(range(first_param, second_param + 1))  # Cria um array de numeros entre first_param e second_param
        
        print(array_completo) # Imprime o array
    except ValueError:
        print("none")  # Se a conversao falhar, imprime none