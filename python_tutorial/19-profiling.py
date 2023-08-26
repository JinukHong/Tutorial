import time
from cProfile import Profile
from pstats import Stats
from bisect import bisect_left
from random import randint

# 함수 얼마나 실행됐고 몇초 실행됐는지.

def insert_value1(array, value):
    for i, existing in enumerate(array):
        if existing > value:
            array.insert(i, value)
            return
    array.append(value)

def insertion_sort1(data):
    result = []
    for value in data:
        insert_value1(result, value)
    return result


def test1():
    max_size = 10**4
    data = [randint(0, max_size) for _ in range(max_size)]
    insertion_sort1(data)


def insert_value2(array, value):
    i = bisect_left(array, value)
    array.insert(i, value)

def insertion_sort2(data):
    result = []
    for value in data:
        insert_value2(result, value)
    return result

def test2():
    max_size = 10**4
    data = [randint(0, max_size) for _ in range(max_size)]
    insertion_sort2(data)



def func1():
    profiler = Profile()
    profiler.runcall(test1)
    stats = Stats(profiler)
    stats.strip_dirs()
    stats.sort_stats("cumulative")
    stats.print_stats()

def func2():
    profiler = Profile()
    profiler.runcall(test2)
    stats = Stats(profiler)
    stats.strip_dirs()
    stats.sort_stats("cumulative")
    stats.print_stats()


    
if __name__ == "__main__":
    func1()
    #func2()