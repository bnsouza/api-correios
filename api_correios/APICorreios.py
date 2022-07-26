from typing import Any, List, Optional, Union
import json
import requests
from schema.correios import Ambiente, PrepostagemConsulta, Prepostagens
from utils.token import token_is_expired

class APICorreios:

    ambiente: Ambiente = None
    usuario: str = None
    senha: str = None
    cartao_postagem: str = None

    def __init__(
        self, ambiente="homologacao", usuario="empresacws", senha="123456", cartao_postagem="0067599079"
    ):
        self.ambiente = ambiente
        self.usuario = usuario
        self.senha = senha
        self.cartao_postagem = cartao_postagem
        self.base_url = "https://apihom.correios.com.br" if self.ambiente=='homologacao' else "https://api.correios.com.br"
        self.token = None

    def autenticar(self):
        token_expired = False
        if self.token:
            token_expired = token_is_expired(self.token)

        if not self.token or token_expired:
            payload = {"numero": self.cartao_postagem}
            headers = {"Content-Type": "application/json"}

            response = requests.post(
                self.base_url + '/token/v1/autentica/cartaopostagem', 
                auth=(self.usuario, self.senha),
                data=json.dumps(payload),
                headers=headers
                )

            if response.status_code in (200, 201):
                token = response.json().get('token', None)
                if token:
                    self.token = token
                    return True
            return False
        return True

    def listar_prepostagens(self, **kwargs: dict) -> Prepostagens:
        self.autenticar()

        if not 'numeroCartaoPostagem' in kwargs:
            kwargs.update({'numeroCartaoPostagem': self.cartao_postagem})

        params = PrepostagemConsulta(**kwargs)

        headers = {'Authorization': 'Bearer ' + self.token}

        response = requests.get(
            url=self.base_url + '/prepostagem/v2/prepostagens', 
            params=params, 
            headers=headers
        )  

        print(response.json())

        response = Prepostagens(**response.json())
        
        return response

if __name__ == '__main__':
    correios = APICorreios()
    correios.listar_prepostagens(tipoObjeto='TODOS', page=0, size=50)

