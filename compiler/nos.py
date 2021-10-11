# from pprint import pprint
# from sys import argv
# from re import sub, compile
# from argparse import ArgumentParser
import os
from typing import List

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


def verify(_noscode: str) -> str:
    """funtion responsible to verify and recognise
    the .nos command and change them to .py command

    :return: the command replaced
    """
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


def translate() -> List:
    """funtion responsible by translating
    the code .nos into .py

    :return: list with the lines of the .nos script
    """
    content_nos = open('teste.nos').readlines()
    content_py = []

    for linha in content_nos:
        content_py.append(verify(linha))
    return content_py


def compiler(_exec: False):
    """funtion responsible to"""
    os.makedirs('temp', exist_ok=True)

    pycode = "".join(translate())
    pyscript = os.path.join('temp', 'script.py')

    with open(pyscript, 'w') as tmpscript:
        tmpscript.write(pycode)

    if _exec:
        if os.name == 'posix':
            raise SystemError('Unsupported Operative System...')
        elif os.name == 'nt':
            os.system(f'./python.exe {pyscript}')


if __name__ == '__main__':
    compiler()
