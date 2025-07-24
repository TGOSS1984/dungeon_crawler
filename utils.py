from colorama import Fore, Style, init

init(autoreset=True)


def bold(text):
    return Style.BRIGHT + text + Style.RESET_ALL


def red(text):
    return Fore.RED + text + Fore.RESET


def green(text):
    return Fore.GREEN + text + Fore.RESET


def yellow(text):
    return Fore.YELLOW + text + Fore.RESET


def blue(text):
    return Fore.CYAN + text + Fore.RESET


def magenta(text):
    return Fore.MAGENTA + text + Fore.RESET


def cyan(text):
    return Fore.CYAN + text + Fore.RESET
