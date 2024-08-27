"""
Client for testing generation and export.
"""

from VariationGen import VariationGen
from Intent import Intent

def main():
    vargen = VariationGen(Intent("Hello"))
    path = "/Users/Aspen/PycharmProjects/ValSoundDesign/generated/"
    vargen.generate(1,path)

if __name__ == "__main__":
    main()