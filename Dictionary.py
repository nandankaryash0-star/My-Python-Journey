# a dictionary = a collection of {key:values} pairs ordered and changable. no duplicate

capitals = {"INDIA":"New delhi",
            "USA":"WASHINGTON D.C",
            "CHINA":"Beijing",
            "RUSSIA":"Moscow"} 
#print(dir(capitals))
#print(help(capitals))

if capitals.get("Japan"):
    print("Capital Exist")
else:
    print("Capital does not exist")

capitals.update({"Germany":"Berlin","Japan":"Tokyo"})
#capitals.pop("Germany")
#capitals.popitem()
#capitals.clear()
#keys = capitals.keys()

#for key in capitals.keys():
#    print(key)

#values = capitals.values()

#for value in capitals.values():
#   print(value)

iteams = capitals.items()

for key , value in capitals.items():
    print(f"{key} : {value}")