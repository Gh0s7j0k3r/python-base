#!/usr/bin/env python3

"""Hello world multi linguas.

Dependendo da lingua configurada no ambiente, o programa exibe a mensagem 
correspondente.

Como usar:

Tenha a variável LANG devidamente configurada ex:

    export LANG=pt_BR

Execução:

    python3 hello.py
    ou
    ./hello.py
"""
__version__ = "0.0.1"
__author__ = "Miguel Moises"
__license__ = "Unlicense"

import os

current_language = os.getenv("LANG", "en_US")[:5]

msg = "hello,World!"

if current_language == "pt_BR":
    msg = "Olá, Mundo!"
elif current_language == "it_IT":
    msg = "Ciao, Mondo!"
elif current_language == "es_ES":
    msg = "Hola, Mundo!"
elif current_language == "de_DE":
    msg = "Hallo, Welt!"
elif current_language == "fr_FR":
    msg = "Bonjour, Monde!"

print(msg)