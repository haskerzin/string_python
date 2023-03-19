endereco = "Rua Jose Teodoro Bayeux, 248, Maua, Sao Paulo, 09360-280"
endereco_2 = "Rua Jose Teodoro Bayeux, 248, Maua, Sao Paulo, 09360280"

import re # Regular Expression

# Estrutura do CEP: 5 digitos + hifen + 3 digitos

padrao = re.compile("[0123456789][0123456789][0123456789][0123456789][0123456789][-]?[0123456789][0123456789][0123456789]")
padrao_2 = re.compile("[0-9]{5}[-]{0,1}[0-9]{3}")
# O caractere ? significa que o caractere anterior na regra do compile eh opcional
# Nesse caso o '-' seria opciopnal no cep
busca = padrao_2.search(endereco) # Match

if busca:
    cep = busca.group()
    print(cep)