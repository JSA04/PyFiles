from validate_docbr import CPF, CNPJ
from excepts import (InvalidDocument,
                     InvalidCpf,
                     InvalidCnpj)
from typing import Union


def rep(string):
    # Ele procura as strings ".", "/" e "-" no parâmetro "string".
    # E retorna a "string" sem elas para validar um CPF/CNPJ.

    return str(string).replace("/", "").replace(".", "").replace("-", "")


class Document:
    @staticmethod
    def create_document(document: Union[int, str]):
        document = rep(document)
        if len(document) == 11:
            return DocCpf(document)
        elif len(document) == 14:
            return DocCnpj(document)
        else:
            raise InvalidDocument


class DocCpf:
    def __init__(self, document):
        document = str(document)
        if self.validate(document):
            self.cpf = rep(document)
        else:
            raise InvalidCpf("O CPF não é valido")

    @staticmethod
    def validate(cpf):
        validator = CPF()
        return validator.validate(cpf)

    def format(self):
        mask = CPF()
        return mask.mask(self.cpf)

    def __str__(self):
        return self.format()


class DocCnpj:
    def __init__(self, document):
        document = str(document)
        if self.validate(document):
            self.cnpj = rep(document)
        else:
            raise InvalidCnpj("The CNPJ is not valid")

    @staticmethod
    def validate(cnpj):
        validator = CNPJ()
        return validator.validate(cnpj)

    def format(self):
        mask = CNPJ()
        return mask.mask(self.cnpj)

    def __str__(self):
        return self.format()
