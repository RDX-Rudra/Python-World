dict1 = {
    "Harry": "human being",
    "spoon": "object",
}
print(dict1["Harry"])

dict2 = {
    111: "RDX",
    121: "Ujjwal",
    131: "Subham"
}
print(dict2[121])
print(dict2)
for key in dict1.keys():
    print(f"The value corresponding to the key {key} is {dict1[key]}")
for key, value in dict1.items():
    print(f"The value corresponding to the key {key} is {value}")