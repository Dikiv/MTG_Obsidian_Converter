from pathlib import Path
from Card import Card

def make_cube_dir(cube_name, color, type, cmc):
    #Find/Make correct directory
        dir_name = cube_name +"/"+ color +"/"+ type +"/"+ cmc
        try:
          Path(dir_name).mkdir(parents=True,exist_ok=True)
        except PermissionError:
          print(f"permission to create directory was denied")
        except Exception as e:
          print(f"An error occurred: {e}")
        
        return dir_name


def md_writer(card0,img_uri):
        #Build the directory and return the name of the link
        dir_name = make_cube_dir("Cube", card0.color, card0.type, card0.cmc)
        #Write card data into .md file
        fileName = dir_name +"/"+ card0.name + ".md"
        try:
            with open(fileName, "x") as f:
                f.write("---")
                f.write("\n tags: ")
                for stype in card0.subtypes:
                    f.write("\n - " + stype)
                f.write("\n Type: " + card0.type)
                f.write("\n Color: " + card0.color)
                f.write("\n CMC: " + card0.cmc)
                f.write("\n Number of cards: 1" )
                f.write("\n Img_uri: " + img_uri )
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