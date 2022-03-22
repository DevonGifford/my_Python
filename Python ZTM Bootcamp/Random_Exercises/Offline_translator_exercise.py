from translate import Translator


#my sentence to be translated 
sentence = "Hello Lisa.  Have a nice evening!"
# print(sentence)

# translator1 = Translator(to_lang = 'es')
# translation1 = translator1.translate(sentence)
# print (translation1)

# translator2 = Translator(to_lang = 'zh')
# translation2 = translator2.translate(sentence)
# print (translation2)



#my file to be translated

translator = Translator(to_lang = 'es')

try:
    with open("./test_file.txt", mode = 'r') as my_file:
        text = my_file.read()
        print(text)
        translation = translator.translate(text)
        with open("./test_file.txt", mode = 'w') as my_file2:
            my_file2.write(translation)


except FileNotFoundError as err:
    print("Bro I couldn't find the file you are looking for")

except FileExistsError as nerr:
    print("Bro I alreaddy created this file for you, what are you doing?")