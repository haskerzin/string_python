# url = "bytebank.com/cambio?quantidade=100&moedaOrigem=real&moedaDestino=dolar"
url = ' '

# Sanitização da URL
url = url.replace(" ", "")


indice_interrogacao = url.find('?')
url_base = url[:indice_interrogacao]
url_parametros = url[indice_interrogacao+1:]
parametro_busca = 'moedaOrigem'
indice_parametro = url_parametros.find(parametro_busca)
indice_valor = indice_parametro + len(parametro_busca) + 1
indice_e_comercial = url_parametros.find('&', indice_valor)

if len(url) == 0:
    raise ValueError('A URL está vazia')
if indice_e_comercial == -1:
    valor = url_parametros[indice_valor:]
else:
    valor = url_parametros[indice_valor : indice_e_comercial]

print(valor)