## Dictionary

#Collection ,unordered,Indexed,changable


##Creating and Printing a Dictionary
dict={"Brand":"Volkswagen","Model":"Polo","Variant":"Petrol"}
print(dict)

##Accessing Item
dict={"Brand":"Volkswagen","Model":"Polo","Variant":"Petrol"}
x=dict["Model"]
print(x)

##get Method
dict={"Brand":"Volkswagen","Model":"Polo","Variant":"Petrol"}
x=dict.get("Brand")
print(x)

##Changing Values
dict={"Brand":"Volkswagen","Model":"Polo","Variant":"Petrol"}
dict["Variant"]="Diesel"
print(dict)

##Loop  -print all keynames in the dictionary,one by one

dict={"Brand":"Volkswagen","Model":"Polo","Variant":"Petrol"}
for x in dict:
    print(x)
    
##Loop  -print all values in the dictionary,one by one

dict={"Brand":"Volkswagen","Model":"Polo","Variant":"Petrol"}
for x in dict:
    print(dict[x])
    
##Return the value by using values()

dict={"Brand":"Volkswagen","Model":"Polo","Variant":"Petrol"}
for x in dict.values():
    print(x)
    
##Return the value by using items() -both keys and values

dict={"Brand":"Volkswagen","Model":"Polo","Variant":"Petrol"}
for x,y in dict.items():
    print(x,y)
    
    
##To check whether the keys exist or not

dict={"Brand":"Volkswagen","Model":"Polo","Variant":"Petrol"}
if "Brand" in dict:
    print("Yes, Model is one of the keys in the dict dictionary")
    
    
##Length

dict={"Brand":"Volkswagen","Model":"Polo","Variant":"Petrol"}
print(len(dict))
print(dict)

##Adding Items

dict={"Brand":"Volkswagen","Model":"Polo","Variant":"Petrol"}
dict["Color"]="Red"
print(dict)

##Removing Items

dict={"Brand":"Volkswagen","Model":"Polo","Variant":"Petrol"}
dict.pop("Model")
print(dict)

##Deleting Dictionary

dict={"Brand":"Volkswagen","Model":"Polo","Variant":"Petrol"}
del dict
print(dict)

##Clearing Dictionary

dict={"Brand":"Volkswagen","Model":"Polo","Variant":"Petrol"}
dict.clear()
print(dict)


##Copy a Dictionary

dict={"Brand":"Volkswagen","Model":"Polo","Variant":"Petrol"}
Mydict=dict.copy()
print(Mydict)

##Copy with dict Method

##dict={"Brand":"Volkswagen","Model":"Polo","Variant":"Petrol"}
##mydict=dict(dict)
##print(mydict)

##Nested Dictionary   -Create a dictionary that contain three dictionary
mygarage={"Car1":{"name":"Volkswagen","Model":"Polo"},"Car2":{"name":"Hyundai","Model":"Verna"},"Car3":{"name":"Honda","Model":"City"}}
print(mygarage)

##creating three dictionaries than create one dictionary that will contain the other three dictionaries

Car1={"name":"Volkswagen","Model":"Polo"},Car2={"name":"Hyundai","Model":"Verna"},Car3={"name":"Honda","Model":"City"} mygarage={"Car1":Car1,"Car2":Car2,"Car3":Car3}
