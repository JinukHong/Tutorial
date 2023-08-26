
# 1
def func1():
    a = 'hello'
    b = 'world'

    print(f"{a} {b}!")


# 2
def func2():
    a = 3
    b = 1.234567

    print(f"{a:04d} {b:.3f}!") # 04d: int 앞에 0 4개 붙인다. .3f: 소숫점 3자리까지
    
# 3
def func3():
    a = '\thello'
    print(a)
    print(f"{a!r}") # !r(representation) -> escape sequence 없애줌

#def func4():
    #string = f"{"{"{"hi"}}"}" # python 3.12 부터는 에러 안뜸
    #print(f"{string}")

if __name__ == "__main__":
    func1()
    func2()
    func3()
    #func4()