file=open("sample_Data.txt","r")
data=file.read()
file.close()
print(data)

########################################
# Read line by line
file=open("sample_Data.txt","r")
for line in file:
  print(line.strip())   #strip is used for removing extra spaces and lines
file.close