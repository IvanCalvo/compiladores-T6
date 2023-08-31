from pymidiParser import pymidiParser

class pymidiUtils:
    def __init__(self):
        self.erros = []

    def adicionarErro(self, mensagem):
        self.erros.append(f"{mensagem}")

utils = pymidiUtils()