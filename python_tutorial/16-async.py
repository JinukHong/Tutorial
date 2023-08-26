import asyncio
import time

# 동기: 팬티를 입고 바지를 입을 수 없다.
# 비동기: 상의 하의 동시에 입을 수 잇다. -> 다중 스레드에서 분화, 

#  프로세스  - 스레드 -> 힙 메모리 공유, 스택 메모리 생성.
#          - 스레드 - 코루틴 -> 메모리 생성할 필요 없다. (네트워크 작업 등 메모리가 필요 없고 비동기적으로 처리 가능한 경우 사용)
#                 - 코루틴

async def wait_network():
    print("네트워크 다운로드 중...")
    await asyncio.sleep(3.0)

async def func1():

    start = time.time()

    task1 = asyncio.create_task(wait_network())
    task2 = asyncio.create_task(wait_network())

    await task1
    await task2

    end = time.time()

    delta = end-start
    print(f"총 시간: {delta:.3f} sec")



if __name__ == "__main__":
    asyncio.run(func1())
