from collections import defaultdict

def func1():
    a = defaultdict(int)
    b = defaultdict(list)
    c = defaultdict(lambda: len(c))
    for i in range(10):
        a[i] = f'{i}'

    for i in range(10):
        b[i].append(f'{i}')
    
    for i in range(10):
        c[i] += 10
        
    print(a)
    print(b)
    print(c)
    


if __name__ == "__main__":
    func1()
    