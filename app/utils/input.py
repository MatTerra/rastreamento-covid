from datetime import date, datetime

from utils.colors import bcolors


def read_simple_string(prop_name: str):
    result = ""
    while result == "":
        result = input(f" {bcolors.BOLD}{prop_name}: {bcolors.ENDC}")
        if result == "":
            print(bcolors.WARNING + f"Você deve informar o(a) "
                                    f"{prop_name.lower()}!"
                  + bcolors.ENDC)
    return result


def read_simple_date(prop_name: str):
    result = ""
    while not isinstance(result, date):
        result = input(f" {bcolors.BOLD}"
                       f"{prop_name} (dd/mm/AAAA):"
                       f" {bcolors.ENDC}")
        try:
            result = datetime.strptime(result, "%d/%m/%Y")
            if result.timestamp() > datetime.now().timestamp():
                result = ""
                raise ValueError
        except ValueError:
            print(f"{bcolors.FAIL}Data inválida!{bcolors.ENDC}")
    return result


def read_nullable_date(prop_name: str):
    result = ""
    while not isinstance(result, date):
        result = input(f" {bcolors.BOLD}"
                       f"{prop_name} (dd/mm/AAAA;"
                       f" deixe em branco caso não saiba):"
                       f" {bcolors.ENDC}")
        try:
            result = datetime.strptime(result, "%d/%m/%Y")
            if result.timestamp() > datetime.now().timestamp():
                result = ""
                raise ValueError
        except ValueError:
            if result == "":
                return None
            print(f"{bcolors.FAIL}Data inválida!{bcolors.ENDC}")
    return result
