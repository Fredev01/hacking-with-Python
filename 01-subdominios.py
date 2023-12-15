import requests
from os import path
import argparse
import sys

parser = argparse.ArgumentParser()
parser.add_argument('-t', '--target', help="Indicar el dominio de la victima")
argument = parser.parse_args().target


def main():
    if argument:
        if path.exists("subdominios.txt"):
            with open("subdominios.txt", "r", encoding="utf-8") as diccionario:
                content = diccionario.read().split("\n")
                print(content)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()
