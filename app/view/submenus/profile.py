from os import system

from utils.controller.profile import add_email, change_birthday, remove_email
from utils.entity.usuario import Usuario


def edit_profile(user: Usuario) -> Usuario:
    print("O que você gostaria de editar?")
    print("\t0 - Adicionar email secundário")
    print("\t1 - Remover email")
    print("\t2 - Data de nascimento")
    choice = ""
    while choice.lower() not in ["0", "1", "2"]:
        choice = input(">> ")
    if choice == '0':
        system("clear")
        add_email(user)
    elif choice == '1':
        system("clear")
        remove_email(user)
    elif choice == '2':
        change_birthday(user)
    return user


def view_profile(user: Usuario) -> Usuario:
    print("Perfil do Usuário\n")
    print(f"\tNome:\t\t\t{user.primeiro_nome} {user.ultimo_nome}")
    print(
        f"\tData de nascimento:\t{user.data_nascimento.strftime('%d/%m/%Y')}")
    print(f"\tEmails:")
    for email in user.emails:
        print(f"\t\t{'*' if email.primario else '-'} {email.email}")
    print("")
    print("\t(*) Email primário")
    print("")
    choice = ""
    while choice.lower() not in ["s", "n"]:
        choice = input("Gostaria de alterar algum dado? [s/N]\n>> ")
    if choice == 's':
        system("clear")
        return edit_profile(user)
    system("clear")
    return user