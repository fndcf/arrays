#!/usr/bin/env python3

### chmod +x 'arquivo.py' (chmod é um comando para alterar a permissão de arquivos)

"""
Este script cria um array e faz uma somatoria de 2 em todos os numeros dentro do array.

Funcionamento do código:

1. Cria um array com 8 numeros selecionados
2. Cria um segundo array com os 8 numeros selecionados adicionados por 2
3. Printa os dois arrays
"""

orignal_array = [2, 8, 9, 48, 8, 22, -12, 2]  # Cria um array de 8 numeros selecionados
second_array = [(val_1 + 2) for val_1 in orignal_array] # Adiciona 2 em todos os numeros dentro do array
print(f"{orignal_array}") # Imprime o primeiro array
print(f"{second_array}") # Imprime o segundo array com os valores adicionados em 2

