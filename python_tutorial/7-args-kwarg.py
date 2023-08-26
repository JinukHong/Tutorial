def func1():
    # 가변인자 사용
    def star(a, b, *c):
        print("a", a)
        print("b", b)
        print("c", c)
    
    star(1, 2, 3, 4, 5, 6, 7)
    
def func2():
    # 가변인자 사용 -> 뭐가 들어올지 모를때. 
    def kwargs(num=10, **kwargs): # * 하나만 있으면 값이 하나만 들어감, **은 key, value pair 가 들어감.
        print("num", num)
        print("kwargs", kwargs)
        
    tmp = {
        "name": "john",
        "age": 20,
        "major" : 'cs'
    }
    kwargs(**tmp)


if __name__ == "__main__":
    func1()
    func2()