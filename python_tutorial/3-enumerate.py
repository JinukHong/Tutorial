def func1():
    a = ['a', 'b', 'c', 'd']
    for i in range(len(a)):
        print(i, a[i])

def func2():
    a = ['a', 'b', 'c', 'd']
    for i, a_ele in enumerate(a, start=0): # len으로 안묶어도 index, 원소 알 수 있다. start = 옵션은 원래 Index에 + 하는 개념.
        print(i, a_ele)
    
if __name__ == "__main__":
    #func1()
    func2()