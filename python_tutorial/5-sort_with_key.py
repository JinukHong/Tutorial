def func1():
    a = [("물리", 44), ("수학", 53), ("영어", 33), ("국어", 19)]
    a.sort()
    print(a)

def func2():
    def return_num(lst):
        return lst[1]

    a = [("물리", 44), ("수학", 53), ("영어", 33), ("국어", 19)]
    #a.sort(key=lambda x: x[1]) # 함수값 넣어도 된다.
    a.sort(key=return_num) #-> function으로 넣어보자.
    print(a)


if __name__ == "__main__":
    # func1()
    func2()
    