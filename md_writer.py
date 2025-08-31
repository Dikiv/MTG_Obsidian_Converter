from pathlib import Path
from Card import Cardc

def make_cube_dir(cube_name, color, type, cmc, dest):
    #Find/Make correct directory
        if color:
            dir_name = dest + "/" + cube_name +"/"+ color +"/"+ type +"/"+ cmc
        else:
            dir_name = dest + "/" + cube_name +"/C/"+ type +"/"+ cmc
        try:
          Path(dir_name).mkdir(parents=True,exist_ok=True)
        except PermissionError:
          print(f"permission to create directory was denied")
        except Exception as e:
          print(f"An error occurred: {e}")
        
        return dir_name


def md_writer(cards: list[Cardc],dest):
        for card in cards:   
            #Build the directory and return the name of the dir
            dir_name = make_cube_dir("Cube", card.color, card.type, card.cmc, dest)
            #Write card data into .md file
            fileName = dir_name +"/"+ card.name + ".md"
            try:
                with open(fileName, "x") as f:
                    f.write("---")
                    f.write("\n tags: ")
                    for stype in card.subtypes:
                        f.write("\n - " + stype)
                    f.write("\n Type: " + card.type)
                    f.write("\n Color: " + card.color)
                    f.write("\n CMC: " + card.cmc)
                    f.write("\n Number of cards: 1" )
                    f.write("\n Img_uri: " + card.imgUrl )
                    f.write("\n In my cube: False" )
                    f.write("\n set: " + card.set )
                    f.write("\n---")
            except FileExistsError:
                fileName = dir_name +"/"+ card.name + ".md"
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