dict = {
    "package": "A package is a module that can be added to any program",
    "random": "Any data or information that has no order",
    "unary operator": "An operator that takes only one value for its operation"
}
print(dict['package'])

# Adding new keys
dict["variable"] = "A memory or a location, that wouldn't change"

print(dict)


# Iterating over dictionaries

for k in dict:
    v = dict[k]
    print (k, " --- " , v)

print("package" in dict)

if "package" not in dict:
    print("the keyword package is not in this dictionary")
else:
    print("the keyword package was found")

print(dict.items())

for k, v in dict.items():   
    print (k, "=", v)


# Using dictionaries for configuration

autograder_conf = { 
    'url' : '121.52.146.108:8000', 
    'username' : 'p1111111', 
    'submission_pass' : 'abc-334'
}

print ('Connecting to', autograder_conf['url'], "with username", autograder_conf['username']) 



