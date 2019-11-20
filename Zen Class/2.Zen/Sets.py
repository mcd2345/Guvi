## Sets

##Unordered and unindexed

##Creating a set   ##No index
set={"Chinna","Mahesh","Arun","Kevin","Sahul"}
print(set)

##To Access Items
set={"Chinna","Mahesh","Arun","Kevin","Sahul"}
for x in set:
    print(x)
    
##To check whether the name is present or not
set={"Chinna","Mahesh","Arun","Kevin","Sahul"}
if "Chinna" in set:
    print("Yes, Chinna is present in the set")
    
##If Not present in the set
set={"Chinna","Mahesh","Arun","Kevin","Sahul"}
if "Sudheer" in set:
    print("Yes, Sudheer is present in the Set")
else:
    print("No, Sudheer is not present in the Set")

##Adding Values to the set
set={"Chinna","Mahesh","Arun","Kevin","Sahul"}
set.add("Sudheer")
print(set)

##Adding Multiple Values to the set
set={"Chinna","Mahesh","Arun","Kevin","Sahul"}
set.update(["Sudheer","Bawa","KaakaaMuttai"])
print(set)

##Getting length of the set

set={"Chinna","Mahesh","Arun","Kevin","Sahul"}
print(len(set))

##Removing Items   ##By using remove() command

set={"Chinna","Mahesh","Arun","Kevin","Sahul"}
set.remove("Sahul")
print(set)

##Removing Items  ##By using discard() command
set={"Chinna","Mahesh","Arun","Kevin","Sahul"}
set.discard("Kevin")
print(set)


##Removing Item   ##By using POP 
set={"Chinna","Mahesh","Arun","Kevin","Sahul"}
x=set.pop()
print(x)
print(set)

##To Clear the set

set={"Chinna","Mahesh","Arun","Kevin","Sahul"}
set.clear()
print(set)

##To Delete the set Completely 

set={"Chinna","Mahesh","Arun","Kevin","Sahul"}
del set
print(set)

##Joining two sets
set1={"Chinna","Mahesh","Arun","Kevin","Sahul"}
set2={"Sudheer","Akshay","Ramnath"}
set3=set1.union(set2)
print(set3)

##Update  ##inserts the items in set2 into set1
set1={"Chinna","Mahesh","Arun","Kevin","Sahul"}
set2={"Sudheer","Akshay","Ramnath"}
set1.update(set2)
print(set1)

##Set Constructor

set=set(("Chinna","Mahesh","Arun","Kevin","Sahul"))
print(set)
