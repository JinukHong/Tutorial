def wrapper(func): # func -> @ 밑에있는 function
    def inner_func(*args, **kwargs): # name 이 *args, **kwargs 로 들어감.
        func(*args, **kwargs)
        #print(*args)
    return inner_func # return 돼야 실행됨.

def wrapper2(func): # func -> @ 밑에있는 function
    def inner_func2(*args, **kwargs): # name 이 *args, **kwargs 로 들어감.
        func(*args, **kwargs)
        #print(*args, *args)
    return inner_func2 # return 돼야 실행됨.

@wrapper # decorator. decorator 여러개면??
@wrapper2 # decorator. decorator 여러개면??
def func1(name):
    print(f"{name}")

if __name__ == "__main__":
    func1("Tom")
    # func2()