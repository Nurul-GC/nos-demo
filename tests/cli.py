# from pprint import pprint
# from sys import argv
# from re import sub, compile
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


def verifica_cmd(_noscode: str):
    if 'intervalo' in _noscode:
        return _noscode.replace('intervalo', RESERVED['intervalo'])
    elif 'mostre' in _noscode:
        return _noscode.replace('mostre', RESERVED['mostre'])
    elif 'leia' in _noscode:
        return _noscode.replace('leia', RESERVED['leia'])
    elif 'paraInteiro' in _noscode:
        return _noscode.replace('paraInteiro', RESERVED['paraInteiro'])
    elif 'paraTexto' in _noscode:
        return _noscode.replace('paraTexto', RESERVED['paraTexto'])
    elif 'importa' in _noscode:
        return _noscode.replace('importa', RESERVED['importa'])
    elif 'descreva' in _noscode:
        return _noscode.replace('descreva', RESERVED['descreva'])
    elif 'para' in _noscode:
        return _noscode.replace('para', RESERVED['para'])
    elif 'retorna' in _noscode:
        return _noscode.replace('retorna', RESERVED['retorna'])
    elif 'em' in _noscode:
        return _noscode.replace('em', RESERVED['em'])
    elif 'se' in _noscode:
        return _noscode.replace('se', RESERVED['se'])
    elif 'senao' in _noscode:
        return _noscode.replace('senao', RESERVED['senao'])
    elif 'enquanto' in _noscode:
        return _noscode.replace('enquanto', RESERVED['enquanto'])
    elif 'tamanho' in _noscode:
        return _noscode.replace('tamanho', RESERVED['tamanho'])
    elif 'capitaliza' in _noscode:
        return _noscode.replace('capitaliza', RESERVED['capitaliza'])
    return _noscode


def teste():
    code_nos = open('test.nos').readlines()
    code_py = []
    for linha in code_nos:
        code_py.append(verifica_cmd(linha))
    return code_py


if __name__ == '__main__':
    try:
        print("".join(teste()))
    except Exception as erro:
        print(erro)
