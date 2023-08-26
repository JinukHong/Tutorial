import itertools

def func1():
    # 연결
    it = itertools.chain([1, 2, 3], [4, 5, 6])
    print(list(it))
    
def func2():
    # 하나의 원소 반복
    it = itertools.repeat("안녕", 3)
    print(list(it))
    
def func3():
    # 원소 전체 반복
    it = itertools.cycle([1, 2])
    result = [next(it) for _ in range(10)]
    print(result)
    
def func4():
    # 지정된 개수의 이터레이터 생성
    it1, it2, it3 = itertools.tee(["하나", "둘"], 3)
    print(list(it1))
    print(list(it2))
    print(list(it3))
    
# ...


if __name__ == "__main__":
    # func1()
    # func2()
    #func3()
    func4()