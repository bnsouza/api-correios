import pydantic
from schema.correios import Ambiente


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
