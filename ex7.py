print("Mary had a little lamb.")
print("It's fleece was white as {}.".format('snow'))
print("And evrywhere that Mary went.")
print("." * 10) #what does this do?:  This will print ten fullstops in a row

end1 = "C"
end2 = "h"
end3 = "e"
end4 = "e"
end5 = "s"
end6 = "e"
end7 = "B"
end8 = "u"
end9 = "r"
end10 = "g"
end11 = "e"
end12 = "r"

#removing the comma and replacing with a + will not work as we are not concatinating a string, we are creating and assaigning a string to a new variable - therefore we must use a comma
print(end1 + end2 + end3 + end4 + end5 + end6, end=' ')
print(end7 + end8 + end9 + end10 + end11 + end12)