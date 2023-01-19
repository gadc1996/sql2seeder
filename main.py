from DirectoryReader import DirectoryReader
from SqlParser import SqlParser
from SeederWriter import SeederWriter

BASE_DIR = 'sql/'

def main():
    dr = DirectoryReader(BASE_DIR)
    for file in dr.files:
        sp = SqlParser(BASE_DIR+file)
        SeederWriter(sp.model, sp.attributes, sp.values).write()


if __name__ == "__main__":
    main()