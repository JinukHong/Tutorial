def func1():
    a = [1, 2, 3, 4, 5]
    b = [x**2 for x in a] # 변수 노출이 안됨. list comprehension 하면 변수가 내포되어있어서 밖에서 가져다써도 반영이 안됨.
    c = {x: x+10 for x in a}
    print(a)
    print(b)
    print(c)


if __name__ == "__main__":
    func1()