#Reader for CSV files
from pathlib import Path
import csv, os

class Card:
  def __init__(self, name, cmc, type, subtypes, color, set):
    self.name = name 
    self.cmc = cmc
    self.type = type
    if subtypes:
       self.subtypes = subtypes
    self.color = color
    self.set = set


with open('testcsv.csv', mode='r') as csvfile:
    reader = csv.reader(csvfile)
    
    #read categories of cards 
    row_0 = reader.__next__()
    for card_info in reader:

        #splitting up types
        types = card_info[2].split("-")
        mType = types[0].strip()
        sTypes = []
        for styp in types[-1:]:
            sTypes.append(styp.strip())
    

        #Assign data to object
        card0 = Card(card_info[0],card_info[1],mType,sTypes,card_info[3],card_info[4])
    
        #Find/Make correct directory
        dir_name = "Cube/" + card0.color +"/"+ card0.type +"/"+ card0.cmc
        try:
          Path(dir_name).mkdir(parents=True,exist_ok=True)
        except PermissionError:
          print(f"permission to create directory was denied")
        except Exception as e:
          print(f"An error occurred: {e}")
      
        #Write card data into .md file
        fileName = dir_name +"/"+ card0.name + ".md"
        try:
            with open(fileName, "x") as f:
                f.write("---")
                f.write("\n tags: ")
                for stype in card0.subtypes:
                    f.write("\n --" + stype)
                f.write("\n Type: " + card0.type)
                f.write("\n Color: " + card0.color)
                f.write("\n CMC: " + card0.cmc)
                f.write("\n Number of cards: 1" )
                f.write("\n In my cube: " )
                f.write("\n---")
        except FileExistsError:
            fileName = dir_name +"/"+ card0.name + ".md"
            lineTowrite = ""
            with open(fileName, "r") as f:
               lines = f.readlines() 
            for line in lines:
                if line.__contains__("Number of cards:"):
                    lineTowrite = line
                    number = int(lineTowrite.split(" ")[-1:][0].split('\\')[0]) + 1
                    lines[lines.index(line)] = " Number of cards: " + str(number) + "\n"
                    

            with open(fileName, "w") as f:
                  f.writelines(lines)

       




