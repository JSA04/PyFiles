from cpf_cnpj import (Document,
                      DocCpf,
                      DocCnpj)
from excepts import (InvalidCpf,
                     InvalidCnpj,
                     InvalidDocument)
from pytest import raises

###############################################################################
# Testa CPF do tipo inteiro.


def test_cpf_int():
    doc = Document.create_document(14379930017)
    assert type(doc) == DocCpf


###############################################################################
# Testa CPF do tipo string.

def test_cpf_str():
    doc = Document.create_document("01802594078")
    assert type(doc) == DocCpf


###############################################################################
# Testa CNPJ do tipo inteiro.

def test_cnpj_int():
    doc = Document.create_document(46438342000199)
    assert type(doc) == DocCnpj


###############################################################################
# Testa CNPJ do tipo string.

def test_cnpj_str():
    doc = Document.create_document(46438342000199)
    assert type(doc) == DocCnpj


###############################################################################
# Testa CPF com pontuação.

def test_cpf_com_pontuacao():
    doc = Document.create_document("215.685.990-64")
    assert type(doc) == DocCpf


###############################################################################
# Testa CNPJ com pontuação.

def test_cnpj_com_pontuacao():
    doc = Document.create_document("38.999.396/0001-03")
    assert type(doc) == DocCnpj


###############################################################################
# Testa CPF invalido.

def test_cpf_invalido():
    with raises(InvalidCpf):
        doc = Document.create_document("12345678911")


###############################################################################
# Testa CNPJ invalido.

def test_cnpj_invalido():
    with raises(InvalidCnpj):
        doc = Document.create_document("12345678911234")


###############################################################################
# Testa Documento com Quantidade de Números Inválidos.

def test_documento_com_quantidade_de_numeros_invalidos():
    with raises(InvalidDocument):
        doc = Document.create_document("123456")
