with open("notes.txt","w") as file:
  file.write("File Handling\n")
  file.write(" file.read()\n file.write()\n file.append()\n")
with open("notes.txt","r")as file:
  print(file.read())
