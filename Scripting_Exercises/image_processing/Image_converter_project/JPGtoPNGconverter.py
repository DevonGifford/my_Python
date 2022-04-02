import sys
import os
from pathlib import Path
from PIL import Image, ImageFilter

#grab first and second arguement (using sys module)
#argument 1 = folder you want to use
#argument 2 = create new folder for output 
#------------------------------------------------------------------------------------------------------------

chosen_folder = (sys.argv[1])
new_folder = (sys.argv[2])


#check is new/exists, if not create-using OS module (or pathlib)
#------------------------------------------------------------------------------------------------------------

if not os.path.exists(new_folder):
    os.makedirs(new_folder)


#loop throuhg Pokedex folder       
#Convert images to png format
#Save to the new folder 
#------------------------------------------------------------------------------------------------------------

for images in os.listdir(chosen_folder):
    img = Image.open(f'{chosen_folder}//{images}')
    print(img)
    just_file_name = os.path.splitext(images)[0]
    print(just_file_name)
    img.save(f'{new_folder}//{just_file_name}.png', 'png')
    print("completed the task sir")
