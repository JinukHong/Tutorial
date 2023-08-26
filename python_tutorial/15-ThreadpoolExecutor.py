# 블로킹 io에서 스레드 사용해 병렬성 회피
# 파이썬은 소스코드를 바이트 코드(3.6부터는 16비트 명령어 사용)
# 바이트 코드 인터프리터는 파이썬 프로그램이 실행되는 동안 일관성있게 유지해야 하는 상태가 존재하기 때문에 GIL(전역 인터프리터 락)을 사용해 강제로 유지
# GIL은 뮤텍스이며 선점형 멀티스레드로 인해 영향을 받는 것을 방지
# 파이썬도 다중 스레드를 지원하지만 한번에 하나의 스레드만 사용함

import os
import dis
import time
import random
from threading import Thread
from concurrent.futures import ThreadPoolExecutor

def wait_second():
    print("스레드 작업중...")
    time.sleep(3)


def func1():
    # 동기적 프로그래밍
    start = time.time()
    for _ in range(5):
        wait_second()
    end = time.time()

    delta = end-start
    print(f"총 시간: {delta:.3f} sec")


def func2():
    # 멀티스레드 사용
    start = time.time()

    with ThreadPoolExecutor(max_workers=3) as pool:
        for _ in range(5): # 5개 돌리니깐
            task = pool.submit(wait_second)

    end = time.time()
    delta = end-start
    print(f"총 시간: {delta:.3f} sec")


    
if __name__ == "__main__":
    #func1()
    func2()