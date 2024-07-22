"""
Client for testing generation and export.
"""

import VariationGen
from Intents import *

def main():
    vargen = VariationGen.VariationGen(Hello.Hello())
    path = "C:/Users/Aspen/PycharmProjects/ValSoundDesign/generated"
    vargen.generate(3,path)

if __name__ == "__main__":
    main()