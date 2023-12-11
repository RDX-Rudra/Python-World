with open('myfile3.txt', 'r') as f:
    print(type(f))
    f.seek(5)
    data = f.read(5)
    print(data)
    print(f.tell())