from PIL import Image, ImageFilter

#---------------------------------------------------------------------------------------------------------------------------
#The Basic stuff
#---------------------------------------------------------------------------------------------------------------------------
# img = Image.open('.\image_processing\Pokedex\pikachu.jpg')  #Opening an image

# print(img)          #check the details about the image

# print(img.format)   #check format
# print(img.size)     #check image size
# print(img.mode)     #check the 'mode' 

# print(dir(img))     #check all the modules of the image


# #---------------------------------------------------------------------------------------------------------------------------
# # Creating a filter for an image
# #---------------------------------------------------------------------------------------------------------------------------
# filtered_img = img.filter(ImageFilter.BLUR)
# filtered_img.save('blur.JPEG', 'JPEG')
# print (filtered_img)
# print(filtered_img.format)


# #---------------------------------------------------------------------------------------------------------------------------
# #Showing an image, Rotating an Image, and Resizing an image - (commented out, don't want to do it over and over)
# #---------------------------------------------------------------------------------------------------------------------------
# # filtered_img.show()
# # filtered_img.rotate(90)
# # filtered_img.resize((250,250))


# #---------------------------------------------------------------------------------------------------------------------------
# #Cropping an image
# #---------------------------------------------------------------------------------------------------------------------------
#box = (100,100,400,400)
#comment out - region = filtered_img.crop(box)
#comment out - region.save("cropped_pikachu.png", 'png')


#---------------------------------------------------------------------------------------------------------------------------
#Downsizing an image 
#---------------------------------------------------------------------------------------------------------------------------

astro = Image.open('./image_processing/Pokedex/astro.jpg')

print('This is the size of the original')
print(astro.size)

#new_astro = astro.resize((400, 400))
#new_astro.save('thumbnail_astro.jpg')      #Doing this has compressed our image icorrectly (original size was odd)

astro.thumbnail((400, 400))                 #400x400 is the max for thumbnails, but keeps aspect ration - just FYI
astro.save('thumbnail_astro.jpg')



#---------------------------------------------------------------------------------------------------------------------------
#Other stuff - not to sure about yet
#---------------------------------------------------------------------------------------------------------------------------
#  for filename in os.listdir(image_folder):
#     img = Image.open(f'{image_folder}\\{filename}')
#     clean_name = os.path.splitext(filename)
#     img.save(f'{output_folder}\\{filename}','png')
#     print(f'Conversion completed: ',{filename})