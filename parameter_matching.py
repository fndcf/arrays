#!/usr/bin/env python3

### chmod +x 'arquivo.py' (chmod é um comando para alterar a permissão de arquivos)

"""
Este script mostra "none" caso a quantidade de parametros seja diferente de um e
mostra "nope, sorry..." enquanto a palavra digitada não for igual ao primeiro parametro.
Quando a palavra correta for digitada, sera exibido "good job"
"""

import sys

if len(sys.argv) - 1 != 1:  # Pega a quantidade de parametros, excluindo o nome do script e caso seja diferente de 1 imprime none
    print("none")
    sys.exit(1)  # Encerra o script
    
first_param = sys.argv[1]  # Cria uma variavel com o primeiro parametro
word = input("What was the parameter? ")
while word != first_param:
    print("Nope, sorry...")  # Mensagem quando a palavra nao esta igual ao parametro
    word = input("What was the parameter? ")
print("Good job!")  # Mensagem de sucesso
