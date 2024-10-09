"""
Client for testing generation and export.
"""

from VariationGen import VariationGen
from Intent import Intent

def main():
    vargen = VariationGen(Intent(name="Yes",test=True))
    path = "/Users/Aspen/PycharmProjects/ValSoundDesign/generated/Random/Yes/"
    vargen.generate(10,path,False)

if __name__ == "__main__":
    main()