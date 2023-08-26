# 인덱스 대입 대신 언패킹 사용

# 언패킹 -> 튜플만 아니라 리스트도 된다.
def func1():
    a = [1, 2, 3] 
    b1, b2, b3 = a
    print(b1, b2, b3)

def func2():
    # starred expression
    a, b, *c = [1, 2, 3, 4, 5, 6, 7]
    print("a", a)
    print("b", b)
    print("c", c)

def func3():
    a, *b, c = [1, 2, 3, 4, 5, 6, 7]
    print("a", a)
    print("b", b)
    print("c", c)

if __name__ == "__main__":
    # func1()
    # func2()
    func3()