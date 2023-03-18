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
        else:
            if not self.url.startswith('https'):
                raise ValueError("A URL nao comeca com 'https'")
            if not self.get_url_base().endswith('/cambio'):
                raise ValueError("A URL nao e da pagina de cambio do Bytebank")


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