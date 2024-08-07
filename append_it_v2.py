#!/usr/bin/env python3

### chmod +x 'arquivo.py' (chmod é um comando para alterar a permissão de arquivos)

"""
Este script mostra "none" caso a quantidade de parâmetros seja igual a zero 
e mostra as palavras que estão no parâmetro adicionando "ism" no final, caso uma das palavras já tenha o "ism" no final não mostra.

Funcionamento do código:

1. Cria uma variável para os parâmetros passados.
2. Pega a quantidade de parâmetros, excluindo o nome do script.
3. Imprime "none" caso a quantidade de parâmetros seja igual a zero.
4. Imprime os parâmetros passados adicionando "ism" no final quando a palavra não tenha "ism" no final.
"""

import sys
import re

parameters = len(sys.argv) - 1  # Pega a quantidade de parâmetros, excluindo o nome do script
array_parameters = sys.argv[1:]   # Cria um array para os parâmetros passados

if parameters == 0:
    print("none")  # Imprime "none" caso a quantidade de parâmetros seja igual a zero
else:
    for word in array_parameters:
        # Verifica se a palavra não termina com "ism" usando uma expressão regular
        if not re.search(r'ism$', word):  # $ indica que "ism" deve estar no final da string
        #if not word.endswith("ism"):   # Verifica se a palavra nao termina com "ism"
            print(word + "ism")            # Adiciona "ism" no final da palavra





