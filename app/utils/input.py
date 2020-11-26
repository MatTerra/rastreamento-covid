from utils.colors import bcolors


def read_simple_string(prop_name: str):
    result = ""
    while result == "":
        result = input(f" {prop_name}: ")
        if result == "":
            print(bcolors.WARNING + f"Você deve informar o(a) "
                                    f"{prop_name.lower()}!"
                  + bcolors.ENDC)
    return result