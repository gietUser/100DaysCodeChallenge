"""
 Dictionary:
    Dictionary in Python is an unordered collection of data values, used to store data values like a map, 
    which unlike other Data Types that hold only single value as an element, 
    Dictionary holds key:value pair. Key value is provided in the dictionary to make it more optimized.
"""

# Creating an Empty Dictionary
dict={}
print("Empty Dictionay:",format(dict))

# Sample Dictionary
dict1 = {
    1: "Ashif",
    2: "Eqbal",
    3: "is",
    4: "DevOps Engineer"
}
print(dict1)

# Nested Dictionary
dict2 = {1: "Python" , 2: "Programming", 3: {"A": "Django", "B": "Flask"} }
print(dict2)

# Accessing element from Dictionary

# From Normal Dictionary
print(dict1[1])
print(dict1[3])

print(dict1.get(4))

# From Nested Dictionary
print(dict2[3]["B"])

# Deleting a Dictionary items

# From Normal Dictionary

sample1 = {1: "Pune", 2: "Mumbai", 3:"Nagpur"}
print("Original Dictionary:{}".format(sample1))

del sample1[2] 
print("After Dictionary:{}".format(sample1))


# From Nested Dictionary
sample1 = {1: "Pune", 2: {1: "Bandra", 2: "Worli", 3: "Dombivali" }, 3:"Nagpur"}
print("Original Dictionary:{}".format(sample1))

del sample1[2][3] 
print("After Dictionary:{}".format(sample1))
