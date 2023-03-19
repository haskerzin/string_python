import re

class Extrator_url:

    def __init__(self, url):
        self.url = self.sanitiza_url(url)
        self.__valida_url()

    def sanitiza_url(self, url):
        if type(url) == str:
            return url.strip()
        else:
            return ''

    def __valida_url(self):
        if not self.url:
            raise ValueError("A URl esta vazia")
        
        padrao_url = re.compile("(http(s)?://)?(www.)?bytebank.com(.br)?/cambio")
        match = padrao_url.match(self.url)

        if not match:
            raise ValueError("A URL nao e valida")
        else:
            print('A URL e valida')


    def get_url_base(self):
        indice_interrogacao = self.url.find('?')
        return self.url[:indice_interrogacao]

    def get_url_parametros(self):
        indice_interrogacao = self.url.find('?')
        return self.url[indice_interrogacao + 1:]

    def get_valor_parametro(self, parametro_busca):
        indice_parametro = self.get_url_parametros().find(parametro_busca)
        indice_valor = indice_parametro + len(parametro_busca) + 1
        indice_e_comercial = self.get_url_parametros().find('&', indice_valor)

        if indice_e_comercial == -1:
            valor = self.get_url_parametros()[indice_valor:]

        else:
            valor = self.get_url_parametros()[indice_valor:indice_e_comercial]

        return valor
    

url = 'https://www.bytebank.com.br/cambio?quantidade=100&moedaOrigem=real&moedaDestino=dolar'
classe = Extrator_url(url)
valor_quantidade = classe.get_valor_parametro('quantidade')
print(valor_quantidade)