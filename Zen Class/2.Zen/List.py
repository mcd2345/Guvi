## List

##Creating List
List=["Volkswagen","Hyundai","Honda"]
print(List)

##Access Items
List=["Volkswagen","Hyundai","Honda"]
print(List[1])

##Negative Indexing
List=["Volkswagen","Hyundai","Honda"]
print(List[-1])

##Range of Indexes
List=["Volkswagen","Hyundai","Honda","Tata","Maruti","Audi","BMW"]
print(List[2:5])

##Range of Negative Indexes
List=["Volkswagen","Hyundai","Honda","Tata","Maruti","Audi","BMW"]
print(List[-2:-5])

##Change Item values
List=["Volkswagen","Hyundai","Honda"]
List[2]="BMW"
print(List)

##Loop Through List
List=["Volkswagen","Hyundai","Honda"]
for x in List:
    print(x)
    
##Check if Item Exists
List=["Volkswagen","Hyundai","Honda"]
if "Volkswagen" in List:
    print("Yes,Volkswagen is in the cars List")

##list Length
List=["Volkswagen","Hyundai","Honda"]
print(len(List))

##Add items
List=["Volkswagen","Hyundai","Honda"]
List.append("BMW")
print(List)

##Adding item in the specified Location
List=["Volkswagen","Hyundai","Honda"]
List.insert(3,"Audi")
print(List)

##Removing Item 
List=["Volkswagen","Hyundai","Honda"]
List.remove("Honda")
print(List)

##POP Method of removing item
List=["Volkswagen","Hyundai","Honda"]
List.pop()
print(List)

##del Method of removing item
List=["Volkswagen","Hyundai","Honda"]
del List[1]
print(List)

##To delete the list completly
List=["Volkswagen","Hyundai","Honda"]
del(List)

##Clear Method -Empties the list
List=["Volkswagen","Hyundai","Honda"]
List.clear()

##Copy a List
List=["Volkswagen","Hyundai","Honda"]
MyList=List.copy()
print(MyList)

##Make a Copy with List() Method
List=["Volkswagen","Hyundai","Honda"]
MyList=list(List)
print(MyList)




##Join two Lists
List1=["Volkswagen","Hyundai","Honda"]
List2=["BMW","Audi","Tata"]
List3=List1+List2
print(List3)

####Appending all the items from list1 into list2,one by one ####
##Append List2 into List1
List1=["Volkswagen","Hyundai","Honda"]
List2=[1,2,3]
for x in List2:
    List1.append(x)
print(List1)

##Use the extend() method to add list2 at the end of list1
List1=["Volkswagen","Hyundai","Honda"]
List2=[1,2,3]
List1.extend(List2)
print(List1)

##The List() Constructor

##It is also possible to use the list() constructor to make a new list.
##Using a List() constructor to make a List
Listl=list(("Volkswagen","Hyundai","Honda"))   #double round brackets
print(List1)


#### Exercise

Cars=["Volkswagen","Hyundai","Honda","Tata","KIA","MG","BMW","Audi","Maruti","Jaquar"]
if "BMW" in Cars:
    print("Yes, BMW in the cars List")
else:
    print("No,BMW is not in the cars List")

####

Cars=["Volkswagen","Hyundai","Honda","Tata","KIA","MG","BMW","Audi","Maruti","Jaquar"]
for x in Cars:
    if x=="BMW":
        print(x)
        

####

Cars=["Volkswagen","Hyundai","Honda","Tata","KIA","MG","BMW","Audi","Maruti","Jaquar"]
for x in Cars:
    if x=="BMW":
        print(x)
