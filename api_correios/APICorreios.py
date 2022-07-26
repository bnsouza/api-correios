from typing import Any, List, Optional, Union
import json
import requests
from schema.correios import Ambiente, ListarPrepostagensRequest, Prepostagens, Prepostagem
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

    def autentica(self):
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

        print(response)
        
        return response

    def criar_prepostagem(self, **kwargs: dict) -> Prepostagem:
        self.autentica()

        payload = Prepostagem(**kwargs)
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



if __name__ == '__main__':
    correios = APICorreios()
    # correios.listar_prepostagens(page=0, size=50, tipoObjeto= 'TODOS')
    # correios.criar_prepostagem(codigoServico= "03220",
    #     destinatario= {
    #         'nome': "commodo dolor veniam minim Lorem",
    #         'dddCelular': "11",
    #         'celular': "987875847",
    #         'email': "teste2312@gmail.com",
    #         'cpfCnpj': "38809594045",
    #         'obs': "consequat quis fugiat",
    #         'endereco': {
    #         'cep': "12234005",
    #         'logradouro': "dolore dolore",
    #         'numero': "132",
    #         'complemento': "in id",
    #         'bairro': "et culpa",
    #         'cidade': "incididunt laborum",
    #         'uf': "SP"
    #         }
    #     },
    #     remetente= {
    #         'nome': "et labore",
    #         'dddCelular': "12",
    #         'celular': "987478574",
    #         'email': "teste@gmail.com",
    #         'cpfCnpj': "64907455003",
    #         'obs': "esse in reprehenderit Ut",
    #         'endereco': {
    #         'cep': "12234005",
    #         'logradouro': "veniam mollit Ut dolor",
    #         'numero': "223",
    #         'complemento': "deserunt sed ipsum nisi",
    #         'bairro': "sit veniam",
    #         'cidade': "cupidatat ad non",
    #         'uf': "SP"
    #         }
    #     },
    #     codigoFormatoObjetoInformado= "1",
    #     pesoInformado= "10",
    #     cienteObjetoNaoProibido= 1
    # )

