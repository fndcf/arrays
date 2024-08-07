#!/usr/bin/env python3

### chmod +x 'arquivo.py' (chmod é um comando para alterar a permissão de arquivos)

"""
Este script mostra  "none" caso a quantidade de parametros seja diferente de 1 ou a letra passada na variavel não conste no parametro, 
após essas validações o script procura a letra dentro do parametro e transforma em uma unica string.

Funcionamento do código:

1. Cria uma variavel para os parametros passados
2. Pega a quantidade de parametros, excluindo o nome do script
3. Imprime none caso a quantidade de parametros seja igual a zero
4. Imprime a quantidade de parametros passados
5. Imprime parametro e a length em nova linha
"""

import sys
import re

array_parameters = sys.argv[1:] #Cria um array dos parametros
list_parameters = ' '.join(array_parameters)
letter = "z"
parameters = len(sys.argv) -1 # Pega a quantidade de parametros, excluindo o nome do script
if list_parameters.find(letter) == -1 or parameters != 1 :
    print("none")
else:
    z_character = ''.join(re.findall(rf"{letter}", ''.join(list_parameters))) # Procura por todos os caracteres que está na variavel letter e faz transforma em uma unica string
    print(f"{z_character}")

    



    
    
    
 
