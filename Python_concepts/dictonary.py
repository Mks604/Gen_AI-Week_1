# Dictionary syntax example
test={"name":"mk", "native":"tn", "work":"IT"}
print(test)

# newly add to the key value in dictonary sample
test={"name":"mk", "native":"tn", "work":"IT"}
test["Country"]=("india")
print(test)

# remove the key value in dict
test={"name":"mk", "native":"tn", "work":"IT", "Country": "india"}
del test["Country"]
print(test)

