# reading
f = open('myfile.txt', 'r')

text = f.read()
print(text)
f.close()

# writting
f = open('myfile1.txt', 'w')
f.write('Hello World!')
f.truncate(5)
f.close()

# append
with open('myfile.txt', 'a') as f:
    f.write('\nwelcome')
    
# readline
with open('myfile2.txt', 'r') as f:
    i = 0
    while True:
        i=i+1
        line = f.readline()
        if not line:
            break
        m1 = line.split(",")[0]
        m2 = line.split(",")[1]
        m3 = line.split(",")[2]
        print(f"Marks os student {i} in math is: {m1}")
        print(f"Marks os student {i} in chem is: {m2}")
        print(f"Marks os student {i} in phy is: {m3}")
        
# writelines