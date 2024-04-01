marks = [1,2,3,4,5,6,7,78,88]

for index, mark in enumerate(marks):
    print(mark)
    if(index == 5):
        print("dj")
        
fruits = ["apple", "banana", "dates", "guava", "mango"]
for index, fruit in enumerate(fruits, start=1):
    print(index, fruit)