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
    id: Optional[str] = None
    remetente: RemetenteDestinatario = None
    destinatario: RemetenteDestinatario = None
    codigoObjeto: Optional[str] = None
    codigoServico: str = None
    servico: Optional[str] = None
    precoPrePostagem: Optional[int] = None
    listaServicoAdicional: Optional[List[ListaServicoAdicionalItem]] = None
    numeroNotaFiscal: Optional[str] = None
    itensDeclaracaoConteudo: Optional[List[ItensDeclaracaoConteudoItem]] = None
    pesoInformado: str = None
    pesoAferido: Optional[str] = None
    alturaInformada: Optional[str] = None
    alturaAferida: Optional[str] = None
    larguraInformada: Optional[str] = None
    larguraAferida: Optional[str] = None
    comprimentoInformado: Optional[str] = None
    comprimentoAferido: Optional[str] = None
    diametroInformado: Optional[str] = None
    diametroAferido: Optional[str] = None
    statusAtual: Optional[int] = None
    dataHoraStatusAtual: Optional[str] = None
    dataPrevistaPostagem: Optional[str] = None
    descStatusAtual: Optional[str] = None
    ncmObjeto: Optional[str] = None
    rfidObjeto: Optional[str] = None
    codigoFormatoObjetoInformado: str = None
    codigoFormatoObjetoAferido: Optional[str] = None
    numeroCartaoPostagem: Optional[str] = None
    dataHora: Optional[str] = None
    cienteObjetoNaoProibido: str = "1"
    tipoRotulo: Optional[str] = None
    modalidadePagamento: Optional[int] = None
    idCorreios: Optional[str] = None
    idAtendimento: Optional[str] = None
    chaveNFe: Optional[str] = None
    nuColeta: Optional[str] = None
    solicitarColeta: Optional[str] = None
    sistemaOrigem: Optional[str] = None
    valorTotalBens: Optional[int] = None
    precoServico: Optional[int] = None
    isCredencialInterna: Optional[bool] = None
    isCredencialExterna: Optional[bool] = None
    quantidade: Optional[int] = None
    reciboSolicitacaoAssincrona: Optional[str] = None
    codigoFormatoObjetoPreAfericao: Optional[str] = None
    alturaPreAfericao: Optional[str] = None
    larguraPreAfericao: Optional[str] = None
    comprimentoPreAfericao: Optional[str] = None
    diametroPreAfericao: Optional[str] = None
    pesoPreAfericao: Optional[str] = None
    dataHoraPreAfericao: Optional[str] = None
    mcuUnidadePreAfericao: Optional[str] = None
    idBalancaCubagem: Optional[str] = None
    cepDestinoPreAfericao: Optional[str] = None
    eticket: Optional[str] = None
    dataEticket: Optional[str] = None
    controleCliente: Optional[str] = None
    observacao: Optional[str] = None
    checkList: Optional[str] = None
    embalagem: Optional[str] = None
    tipoObjeto: Optional[str] = None
    erroAssincrono: Optional[str] = None
    codigoEstampa2D: Optional[str] = None
    enviadoSigep: Optional[str] = None
    historicoStatus: Optional[List[HistoricoStatus]] = None


class ListarPrepostagensRequest(BaseModel):
    id: Optional[str] = None
    codigoObjeto: Optional[str] = None
    codigoEstampa2D: Optional[str] = None
    numeroCartaoPostagem: Optional[str] = None
    idCorreios: Optional[str] = None
    idAtendimento: Optional[str] = None
    status: Optional[str] = None
    mcuUnidadePreAfericao: Optional[str] = None
    eTicket: Optional[str] = None
    nomeDestinatario: Optional[str] = None
    data: Optional[str] = None
    tipoObjeto: Optional[str] = None
    modalidadePagamento: Optional[str] = None
    idRecibo: Optional[str] = None
    S: Optional[str] = None
    page: Optional[str] = None
    size: Optional[str] = None


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
    itens: Optional[List[Prepostagem]] = None
    page: Optional[Page] = None


# Rastreamento -------------------------------------------------------------------------------------
class TipoPostal(BaseModel):
    sigla: Optional[str] = None
    descricao: Optional[str] = None
    categoria: Optional[str] = None


class Recebedor(BaseModel):
    nome: Optional[str] = None
    documento: Optional[str] = None
    celular: Optional[str] = None
    email: Optional[str] = None
    comentario: Optional[str] = None

class Unidade(BaseModel):
    nome: Optional[str] = None
    codSro: Optional[str] = None
    codMcu: Optional[str] = None
    tipo: Optional[str] = None
    endereco: Optional[Endereco] = None


class EntregadorExterno(BaseModel):
    documento: Optional[str] = None
    nome: Optional[str] = None


class Telefone(BaseModel):
    tipo: Optional[str] = None
    ddd: Optional[str] = None
    numero: Optional[str] = None


class DestinatarioRastreamento(BaseModel):
    nome: Optional[str] = None
    documento: Optional[str] = None
    email: Optional[str] = None
    telefones: Optional[List[Telefone]] = None
    endereco: Optional[Endereco] = None


class UnidadeDestino(BaseModel):
    nome: Optional[str] = None
    codSro: Optional[str] = None
    codMcu: Optional[str] = None
    tipo: Optional[str] = None
    endereco: Optional[Endereco] = None


class Evento(BaseModel):
    codigo: Optional[str] = None
    tipo: Optional[str] = None
    dtHrCriado: Optional[str] = None
    descricao: Optional[str] = None
    detalhe: Optional[str] = None
    recebedor: Optional[Recebedor] = None
    unidade: Optional[Unidade] = None
    entregadorExterno: Optional[EntregadorExterno] = None
    destinatario: Optional[DestinatarioRastreamento] = None
    comentario: Optional[str] = None
    unidadeDestino: Optional[UnidadeDestino] = None


class Objeto(BaseModel):
    codObjeto: Optional[str] = None
    tipoPostal: Optional[TipoPostal] = None
    dtPrevista: Optional[str] = None
    mensagem: Optional[str] = None
    modalidade: Optional[str] = None
    largura: Optional[int] = None
    comprimento: Optional[int] = None
    altura: Optional[int] = None
    diametro: Optional[int] = None
    peso: Optional[int] = None
    formato: Optional[str] = None
    valorDeclarado: Optional[int] = None
    eventos: List[Evento] = None


class Rastreamento(BaseModel):
    versao: Optional[str] = None
    quantidade: Optional[int] = None
    resultado: Optional[str] = None
    objetos: List[Objeto] = None
