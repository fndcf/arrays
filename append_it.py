#!/usr/bin/env python3

### chmod +x 'arquivo.py' (chmod é um comando para alterar a permissão de arquivos)

"""
Este script mostra "none" caso a quantidade de parametros seja igual a zero 
e mostra as palavras que estão no parametro adicionando "ism" no final, caso uma das palavras já tenha o "ism" no final não mostra.

Funcionamento do código:

1. Cria uma variavel para os parametros passados
2. Pega a quantidade de parametros, excluindo o nome do script
3. Imprime none caso a quantidade de parametros seja igual a zero
4. Imprime os parametros passados adicionando "ism" no final quando a palavra não tenha "ism" no final não mostra
"""

import sys

parameters = len(sys.argv) - 1  # Pega a quantidade de parametros, excluindo o nome do script
array_parameters = sys.argv[1:]   # Cria um array para os parametros passados

if parameters == 0:
    print("none")  # Imprime "none" caso a quantidade de parametros seja igual a zero
else:
    for word in array_parameters:
        match word:
            case _ if not word.endswith("ism"):  # Verifica se a palavra nao termina com "ism"
                print(word + "ism")              # Adiciona "ism" no final da palavra
            case _:
                continue  # Nao faz nada se a palavra termina com "ism"
