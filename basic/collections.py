#list
iamlist = [1,"2","five",4,3,2]

# if "2" in iamlist:
#     print("index is " + str(iamlist.index("2")))

# print(len(iamlist))
# print(iamlist.count(2))

#tuple
iamtuple = (1,2,"3",">")
# print(iamtuple)

#set
iamset = {"5",4,3,"two"}
iamset.add(1)
# print(iamset)

iamset.remove("5")
iamset.discard("5") # will not throw exception if no this value
#iamset.remove("5") # will throw exception if no this value
# print(iamset)

iamset2 = {3,"two",4}

# print(iamset.difference(iamset2))
# print(iamset.intersection(iamset2))

#dictionary
iamdict = {"e":1, "r":"2", "s":3, 4:"test"}
# print(iamdict)
# print(iamdict["e"])
# print(iamdict[4])
# print(iamdict["no"]) # will throw exception if no this key
# print(iamdict.get("r"))
# print(iamdict.get("no")) # return none if no this key

# print(iamdict.values())
## add item
iamdict["new item"] = "nit"
# loop keys
# for k in iamdict.keys():
#     print(k)
## add item
iamdict["pi"] = 3.14159

# loop values
# for v in iamdict.values():
#     print(v)

# remove item
iamdict.pop("e")
print(iamdict)
# remove random item
iamdict.popitem()
print(iamdict)

# loop key/value pair
# for k,v in iamdict.items():
#     print(str(k)+ ":" + str(v))

# in will find key, not value
# print("s" in iamdict)
# print("test" in iamdict)