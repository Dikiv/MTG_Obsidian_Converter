from csv_reader import csv_reader
from md_writer import md_writer
from Card import Cardc

def main():
     
    md_writer(csv_reader('faultyImg.csv'))


if __name__=="__main__":
    main()