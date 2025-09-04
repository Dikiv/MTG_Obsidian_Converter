
from csv_reader import csv_reader
from md_writer import md_writer
from gui import gui
from consoleLoading import ConsoleLoading
import threading

import sys

#arg_mode differs between launching gui or console mode
def main(args):
    if(len(args)<2):
        gui()
    arg_mode = args[1]
    if(arg_mode == 'c'):
        loading = ConsoleLoading()
        #t = threading.Thread(target=loading.runLoading)
        try:     
         #   t.start()
            src = args[2]
            cards = csv_reader(src)
            dest = args[3]
            md_writer(cards,dest)
        except Exception as e:
            print(e)
        loading.stopLoading()  
        #t.join()    

if __name__=="__main__":
    main(sys.argv)
    
    