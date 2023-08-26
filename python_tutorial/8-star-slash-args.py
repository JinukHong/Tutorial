def func1():
    # 가변인자 사용
    def args(a, b, /, *, c, d): # 이게 모냐? / 앞에는 무조건 위치인자, * 뒤에는 키워드 인자.
        print("a", a)
        print("b", b)
        print("c", c)
        print("d", d)
    
    # args(1, 2, 3, 4)
    # args(a=1, b=2, c=3, d=4)
    args(1, 2, c=3, d=4)
    


if __name__ == "__main__":
    func1()