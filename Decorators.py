def greet(fx):
    def mfx(*args, **kwargs):
        print("good morning")
        fx(*args, **kwargs)
        print("thanks for using this functions")
    return mfx

@greet
def hello():
    print("hello world")
    
hello()
# greeet(hello)()

def add(x, y):
    print(x+y)

greet(add)(1,2)  # *args, **kwargs for this argument