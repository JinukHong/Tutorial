# 블로킹 io에서 스레드 사용해 병렬성 회피
# 파이썬은 소스코드를 바이트 코드(3.6부터는 16비트 명령어 사용)
# 바이트 코드 인터프리터는 파이썬 프로그램이 실행되는 동안 일관성있게 유지해야 하는 상태가 존재하기 때문에 GIL(전역 인터프리터 락)을 사용해 강제로 유지
# GIL은 뮤텍스이며 선점형 멀티스레드로 인해 영향을 받는 것을 방지
# 파이썬도 다중 스레드를 지원하지만 한번에 하나의 스레드만 사용함

# 프로세스, 쓰레드 단위
# GIL -> 멀티스레드하려면 이해해야됨. 인터프리터는 한줄한줄 해석되는데 한줄씩 byte code로 컴파일 -> 한줄만 실행할 수 있게 lock 걸어둠.(byte code 가 쓰레드에 들어가면 lock 걸리고 나갈때 lock 해제. mutex)
# lock 만드는 정책.

import os
import dis
import time
import random
from threading import Thread

def save_file(file_path, data):
    with open(file_path, "w") as f:
        f.write(data)

def count_num(num):
    cnt = 0
    for _ in range(num):
        cnt += 1

def func1():
    # 동기적 프로그래밍
    data = ["\n" if i % 100 == 0 else str(random.random()) for i in range(1, 1000001)]
    data = ''.join(data)
    start = time.time()
    save_file(f"test/test1.txt", data)
    count_num(1000000)
    
    end = time.time()

    delta = end-start
    print(f"총 시간: {delta:.3f} sec")


def func2():
    # 멀티스레드 사용
    data = ["\n" if i % 100 == 0 else str(random.random()) for i in range(1, 1000001)]
    data = ''.join(data)

    start = time.time()

    # 스레드 여러개 -> c/c++은 병렬적으로 가능하지만 파이썬은 하나씩. cpu 바운드 작업과 io 바운드 작업이 같이 걸리는 작업 실행할 때 파이썬 멀티스레드 가능.
    # (cpu)파이썬에선 cpu bound 2개도 안됨. c/c++은 되긴 함 - (ram - 입출력(I/o) - 하드) io bound - DMA(direct memory access)는 동시에 못함.
    threads = []
    thread1 = Thread(target=save_file, args=["test/test2.txt", data])
    thread2 = Thread(target=count_num, args=[1000000])
    thread1.start()
    thread2.start()
    for th in threads:
        th.join() # 부모 -> 자식 부모가 종료되지 않게 기다려줌.

    end = time.time()
    delta = end-start
    print(f"총 시간: {delta:.3f} sec")


    
if __name__ == "__main__":
    func1()
    func2()