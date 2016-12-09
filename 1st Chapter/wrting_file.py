text = " Smaple Text to save \n New line!"

# save file with name 
saveFile = open('examplefile.txt', 'w')

#writes the information 
saveFile.write(text)

#It is important to remember to actually close the file, otherwise it will hage
# for a while and could cause problem in your script
saveFile.close()
