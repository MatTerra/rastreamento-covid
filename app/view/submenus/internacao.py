from os import system

from utils.controller.internacao import view_relatorio_diagnostico_internacoes
from utils.entity.usuario import Usuario


def relatorio_diagnostico_internacoes(user: Usuario):
    pagina = 0
    while pagina != 'x':
        system("clear")
        pagina = view_relatorio_diagnostico_internacoes(pagina)