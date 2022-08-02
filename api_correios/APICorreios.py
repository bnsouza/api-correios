import json

import requests
from schema.correios import (
    Ambiente,
    ListarPrepostagensRequest,
    Prepostagem,
    Prepostagens,
    Rastreamento,
)
from utils.token import token_is_expired


class Correios:

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
        self.base_url = "https://api.correios.com.br" if self.ambiente=='producao' else "https://apihom.correios.com.br"
        self.token = None

    def autentica(self) -> bool:
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

    def listar_prepostagens(self, **kwargs: dict) -> dict:
        self.autentica()

        params = ListarPrepostagensRequest(**kwargs)
        headers = {'Authorization': 'Bearer ' + self.token}

        response = requests.get(
            url=self.base_url + '/prepostagem/v2/prepostagens', 
            params=params, 
            headers=headers
        )  
        response = Prepostagens(**response.json())
        response = response.dict(exclude_none=True)
        
        return response

    def criar_prepostagem(self, prepostagem: dict) -> dict:
        self.autentica()

        payload = Prepostagem(**prepostagem)
        headers = {
            'Authorization': 'Bearer ' + self.token,
            "Content-Type": "application/json"
        }

        response = requests.post(
            url=self.base_url + '/prepostagem/v1/prepostagens', 
            data=payload.json(exclude_none=True), 
            headers=headers
        )  
        response = Prepostagem(**response.json())
        response = response.dict(exclude_none=True)
        
        return response

    def rastrear_objeto(self, objetos: list, resultado: str = "U") -> dict:
        self.autentica()

        params = {'codigosObjetos': objetos, 'resultado': resultado}
        headers = {
            'Authorization': 'Bearer ' + self.token,
            "Content-Type": "application/json"
        }

        response = requests.get(
            url=self.base_url + '/srorastro/v1/objetos', 
            params=params, 
            headers=headers
        )  

        response = Rastreamento(**response.json())
        response = response.dict(exclude_none=True)
    
        return response
