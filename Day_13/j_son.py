import json
data={
  "name":"pavan",
  "age":21,
  "skills":["Python","Html","CSS"]
}

with open("data.json","w")as file:
  json.dump(data,file)#Convert Python data into JSON format and write it into a file
print("JSON written")

with open("data.json","r")as file:
  data=json.load(file) #Read JSON data from file and convert it into Python data”
print(data)
print(data["name"])


