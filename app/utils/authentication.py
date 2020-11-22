import os
from getpass import getpass
from typing import List

from utils.entity.email import Email
from utils.entity.usuario import Usuario, hash_password
from utils.database.usuarioDAO import UsuarioDAO
from utils.colors import bcolors


def login(email: str, password: str) -> Usuario:
    usuario_dao = None
    try:
        usuario_dao = UsuarioDAO()
        usuario = usuario_dao.select_from_email(email=email)
        password_hash = hash_password(password, usuario.salt)
        if password_hash == usuario.password:
            return usuario
        return None
    except Exception as e:
        print(f"{bcolors.FAIL}Ops.. Algo deu errado no login... "
              f"Tente novamente.{bcolors.ENDC}")
    finally:
        if usuario_dao:
            usuario_dao.close()


def signup(name: str, last_name: str, password: str, consent: bool,
           emails: List[str]):
    usuario = Usuario(primeiro_nome=name, ultimo_nome=last_name,
                      password=password, consentimento=consent,
                      emails=[])
    for index, email in enumerate(emails):
        usuario.emails.append(Email(email=email,
                                    usuario_id_=usuario.id_,
                                    primario=(index == 0)))
    # Validate email already registered
    usuario_dao = None
    try:
        usuario_dao = UsuarioDAO()
        usuario_dao.create(usuario)
    except Exception as e:
        print(bcolors.FAIL + "Não foi possível criar o usuário...\n"
              + str(e) + bcolors.ENDC)
        return None
    finally:
        if usuario_dao:
            usuario_dao.close()
    return usuario
