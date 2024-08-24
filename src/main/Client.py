"""
Client for testing generation and export.
"""

from VariationGen import VariationGen
from Controllers.DBConnection import DBConnection
from Intents import *

def main():
    vargen = VariationGen(Hello.Hello())
    path = "/Users/Aspen/PycharmProjects/ValSoundDesign/generated/"
    vargen.generate(1,path)

if __name__ == "__main__":
    main()