file=open("sample_data.txt","a")
file.write("\ngo through my next codes as well...")
file.close()
print("Data appended")

with open("sample_data.txt","r")as file:   #with  automatically opens & closes file 
  data=file.read()
  print(data)


