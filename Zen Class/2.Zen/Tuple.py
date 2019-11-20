## Tuples

## Creating a tuple
tuple=("iphone","windowsphone","android")
print(tuple)

##Access tuple items

##Printing the second item in the tuple
tuple=("iphone","windowsphone","android")
print(tuple[1])

##Negative indexing - begining from the end 
tuple=("iphone","windowsphone","android")
print(tuple[-2])

##Range of indexes - by specifying where to start and where to end 
tuple=("iphone","windowsphone","android","redmi","realme","oppo","vivo","samsung")
print(tuple[2:6])

##Range of Negative indexes - start the search by end of the tuple
tuple=("iphone","windowsphone","android","redmi","realme","oppo","vivo","samsung")
print(tuple[-2:-5])

##Change tuple values

tuple=("iphone","windowsphone","android")
y=list(tuple)
y[1]="Mi"
print(y)


##Loop through tuple
tuple=("iphone","windowsphone","android")
for x in tuple:
    print(x)
    
##If item exists
tuple=("iPhone","windowsphone","android")
if "iphone" in tuple:
    print("Yes,iPhone is available")
else:
    print("No,iPhone is not available")


##If not exists
tuple=("Mi","windowsphone","android")
if "iphone" in tuple:
    print("Yes,iPhone is available")
else:
    print("No,iPhone is not available")
    
##Tuple length
tuple=("iphone","windowsphone","android")
print(len(tuple))

##Adding items

##tuple=("iphone","windowsphone","android")
##tuple[3]="realme"
##print(tuple)

##Creating tuples with one item

tuple=("iphone","windowsphone","android")
print(type(tuple))

##Deleting Tuple  ##Removing/Adding is not possible
tuple=("iphone","windowsphone","android")
del tuple
print(tuple) 

##Joining two tuples
tuple1=("iphone","Windowsphone","Android")
tuple2=("realme","Mi","Samsung")
tuple3=tuple1+tuple2
print(tuple3)

##tuple constructor
tuple=tuple(("iphone","windowsphone","android"))
print(tuple)