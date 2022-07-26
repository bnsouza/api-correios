"""
Pydantic Schema - Todos os schemas que serão usados na API
"""

from enum import Enum
from typing import List, Optional

from pydantic import BaseModel, Field

# Enums --------------------------------------------------------------------------------------------


class Ambiente(str, Enum):
    producao = "producao"
    homologacao = "homologacao"


# Pré-postagem -------------------------------------------------------------------------------------
class Endereco(BaseModel):
    id: Optional[int] = None
    cep: Optional[str] = None
    logradouro: Optional[str] = None
    numero: Optional[str] = None
    complemento: Optional[str] = None
    bairro: Optional[str] = None
    cidade: Optional[str] = None
    uf: Optional[str] = None


class RemetenteDestinatario(BaseModel):
    id: Optional[int] = None
    nome: Optional[str] = None
    dddTelefone: Optional[str] = None
    telefone: Optional[str] = None
    dddCelular: Optional[str] = None
    celular: Optional[str] = None
    email: Optional[str] = None
    cpfCnpj: Optional[str] = None
    obs: Optional[str] = None
    endereco: Optional[Endereco] = None


class ListaServicoAdicionalItem(BaseModel):
    codigoServicoAdicional: Optional[str] = None
    tipoServicoAdicional: Optional[str] = None
    nomeServicoAdicional: Optional[str] = None
    valorServicoAdicional: Optional[str] = None
    valorDeclarado: Optional[str] = None
    siglaServicoAdicional: Optional[str] = None
    orientacaoEntregaVizinho: Optional[str] = None


class ItensDeclaracaoConteudoItem(BaseModel):
    conteudo: Optional[str] = None
    quantidade: Optional[str] = None
    valor: Optional[str] = None


class HistoricoStatus(BaseModel):
    id: Optional[int] = None
    status: Optional[int] = None
    dataHora: Optional[str] = None
    prePostagem: Optional[str] = None


class Prepostagem(BaseModel):
    id: Optional[str] = Field(None)
    remetente: Optional[RemetenteDestinatario] = Field(None)
    destinatario: Optional[RemetenteDestinatario] = Field(None)
    codigoObjeto: Optional[str] = Field(None)
    codigoServico: Optional[str] = Field(None)
    servico: Optional[str] = Field(None)
    precoPrePostagem: Optional[int] = Field(None)
    listaServicoAdicional: Optional[List[ListaServicoAdicionalItem]] = Field(None)
    numeroNotaFiscal: Optional[str] = Field(None)
    itensDeclaracaoConteudo: Optional[List[ItensDeclaracaoConteudoItem]] = Field(None)
    pesoInformado: Optional[str] = Field(None)
    pesoAferido: Optional[str] = Field(None)
    alturaInformada: Optional[str] = Field(None)
    alturaAferida: Optional[str] = Field(None)
    larguraInformada: Optional[str] = Field(None)
    larguraAferida: Optional[str] = Field(None)
    comprimentoInformado: Optional[str] = Field(None)
    comprimentoAferido: Optional[str] = Field(None)
    diametroInformado: Optional[str] = Field(None)
    diametroAferido: Optional[str] = Field(None)
    statusAtual: Optional[int] = Field(None)
    dataHoraStatusAtual: Optional[str] = Field(None)
    dataPrevistaPostagem: Optional[str] = Field(None)
    descStatusAtual: Optional[str] = Field(None)
    ncmObjeto: Optional[str] = Field(None)
    rfidObjeto: Optional[str] = Field(None)
    codigoFormatoObjetoInformado: Optional[str] = Field(None)
    codigoFormatoObjetoAferido: Optional[str] = Field(None)
    numeroCartaoPostagem: Optional[str] = Field(None)
    dataHora: Optional[str] = Field(None)
    cienteObjetoNaoProibido: Optional[int] = Field(None)
    tipoRotulo: Optional[str] = Field(None)
    modalidadePagamento: Optional[int] = Field(None)
    idCorreios: Optional[str] = Field(None)
    idAtendimento: Optional[str] = Field(None)
    chaveNFe: Optional[str] = Field(None)
    nuColeta: Optional[str] = Field(None)
    solicitarColeta: Optional[str] = Field(None)
    sistemaOrigem: Optional[str] = Field(None)
    valorTotalBens: Optional[int] = Field(None)
    precoServico: Optional[int] = Field(None)
    isCredencialInterna: Optional[bool] = Field(None)
    isCredencialExterna: Optional[bool] = Field(None)
    quantidade: Optional[int] = Field(None)
    reciboSolicitacaoAssincrona: Optional[str] = Field(None)
    codigoFormatoObjetoPreAfericao: Optional[str] = Field(None)
    alturaPreAfericao: Optional[str] = Field(None)
    larguraPreAfericao: Optional[str] = Field(None)
    comprimentoPreAfericao: Optional[str] = Field(None)
    diametroPreAfericao: Optional[str] = Field(None)
    pesoPreAfericao: Optional[str] = Field(None)
    dataHoraPreAfericao: Optional[str] = Field(None)
    mcuUnidadePreAfericao: Optional[str] = Field(None)
    idBalancaCubagem: Optional[str] = Field(None)
    cepDestinoPreAfericao: Optional[str] = Field(None)
    eticket: Optional[str] = Field(None)
    dataEticket: Optional[str] = Field(None)
    controleCliente: Optional[str] = Field(None)
    observacao: Optional[str] = Field(None)
    checkList: Optional[str] = Field(None)
    embalagem: Optional[str] = Field(None)
    tipoObjeto: Optional[str] = Field(None)
    erroAssincrono: Optional[str] = Field(None)
    codigoEstampa2D: Optional[str] = Field(None)
    enviadoSigep: Optional[str] = Field(None)
    historicoStatus: Optional[List[HistoricoStatus]] = Field(None)


class PrepostagemConsulta(BaseModel):
    id: Optional[str] = Field(None)
    codigoObjeto: Optional[str] = Field(None)
    codigoEstampa2D: Optional[str] = Field(None)
    numeroCartaoPostagem: Optional[str] = Field(None)
    idCorreios: Optional[str] = Field(None)
    idAtendimento: Optional[str] = Field(None)
    status: Optional[str] = Field(None)
    mcuUnidadePreAfericao: Optional[str] = Field(None)
    eTicket: Optional[str] = Field(None)
    nomeDestinatario: Optional[str] = Field(None)
    data: Optional[str] = Field(None)
    tipoObjeto: Optional[str] = Field(None)
    modalidadePagamento: Optional[str] = Field(None)
    idRecibo: Optional[str] = Field(None)
    S: Optional[str] = Field(None)
    page: Optional[str] = Field(None)
    size: Optional[str] = Field(None)


class Page(BaseModel):
    size: int
    numberElements: int
    totalPages: int
    number: int
    count: int
    next: bool
    previous: bool
    first: bool
    last: bool


class Prepostagens(BaseModel):
    itens: Optional[List[Prepostagem]] = Field(None)
    page: Optional[Page] = Field(None)