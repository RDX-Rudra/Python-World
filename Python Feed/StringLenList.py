def string_len(str_list):
    list = []
    for i in str_list:
        list.append(len(i))
    return list

mylist = ['rdx', 'rudra', 'mx@023']
print(string_len(mylist))