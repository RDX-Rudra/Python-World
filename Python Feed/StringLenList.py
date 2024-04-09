def string_len(str_list):
    list = []
    for i in str_list:
        list.append(len(i))
    return list

mylist = ['rdx', 'rudra', 'mx@023']
print(string_len(mylist))

assert string_len(mylist) == [3, 4, 6], "should return true"
print("Assertion passed!")  # This will only print if the assertion passes
