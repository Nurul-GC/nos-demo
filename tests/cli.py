from pprint import pprint
from sys import argv
from re import sub, compile

# from argparse import ArgumentParser

RESERVED = {
    'intervalo': 'range',
    'mostre': 'print',
    'leia': 'input',
    'paraInteiro': 'int',
    'paraTexto': 'str',
    'importa': 'import',
    'descreva': 'class',
    'para': 'for',
    'retorna': 'return',
    'em': 'in',
    'se': 'if',
    'senao': 'else',
    'enquanto': 'while',
    'tamanho': 'len',
    'capitaliza': 'capitalize',
}

teste_nos = """n1 = leia("Informe o primeiro valor: ")
n2 = leia("Informe o segundo valor: ")

soma = n1+n2
multiplicado = n1*n2
dividido = n1/n2

mostre(f"A soma e {soma}")
mostre(f"A multiplicacao e {multiplicado}")
mostre(f"A divisao e {dividido}")"""


def teste():
    code_nos = ''
    for cmd in RESERVED:
        if cmd in teste_nos:
            code_nos = teste_nos.replace(cmd, RESERVED[cmd])
    return code_nos


if __name__ == '__main__':
    try:
        # nos_content = teste()
        print(teste())
    except Exception as erro:
        print(erro)
