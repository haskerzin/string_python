import re

url = 'https://www.bytebank.com.br/cambio'
url_2 = 'www.bytebank.com.br/cambio'

padrao_url = re.compile("(http(s)?://)?(www.)?bytebank.com(.br)?/cambio")
match = padrao_url.match(url_2)

if not match:
    raise ValueError("A URL nao e valida")
else:
    print('A URL e valida')