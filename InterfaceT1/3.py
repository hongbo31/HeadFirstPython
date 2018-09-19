import json

data = {
    "name" : "haha",
    "age" : 12
}
with open("abc.",'w') as f:
    json.dump(data, f)

with open("abc","r") as f:
    d = json.load(f)
    print(d)