"""list syntax practice"""

# Initialize an empty list
grocery_list: list[str] = list() # <- list constructor
grocery_list: list[str] = [] # <-literal

print (grocery_list)

# Add item to a list 
grocery_list.append("bananas")
grocery_list.append("milk")
grocery_list.append("bread")


print("after appending")
print(grocery_list)

#create an already populated list
grocery_list2: list[str] = ["bananas, milk, bread"]
print ("populated list:")
grocery_list2.append("eggs")
print(grocery_list2)

#Indexing
print("Print first element of string")
print(grocery_list[0])

# Modifying by index
print(grocery_list)
grocery_list[1] = "almond milk"
print("After change")
print(grocery_list)


#You can have duplicates 
grocery_list.append("almond milk")
print("add almond milk again: ")
print(grocery_list)

# Measuring length 
print(len(grocery_list))

#Removing an item 
grocery_list.pop(1)
print("After removing almond milk:")
print(grocery_list)

# Function name: display 
# Parameter: list [str]
# Return Nothing!
# Print out the list!
print("~*~ Functions! ~*~")

def display(word: lsit[str]) -> None:
    print(word)

display(grocery_list)

x = display([ "Alyssa", "Erin", "AK"])
print (x)

# Create a list!
# Name: create
# parameters: str, str
# return: list of str
#Put both paramters into a list


  


