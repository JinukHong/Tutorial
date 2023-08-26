def index_words(text):
    result = []
    if text:
        result.append(0)
    for idx, letter in enumerate(text):
        if letter == ' ':
            result.append(idx + 1)
    return result

def index_iter(text): # generator 란? iterable 객체. => __next__, __iter__ 포함, next(객체) -> 다음꺼 뽑아주는 역할.
    if text:
        yield 0 # 함수 진행하다가 yield 만나면 return. -> next -> yield 만나면 return
    for idx, letter in enumerate(text):
        if letter == ' ':
            yield idx + 1
    # 한번만 쓰고 버릴꺼 왜쓰냐? 용량 큰 파일은 메모리에 한번에 다 안들어감, 그리고 너무 오래걸림. 한줄씩만 가져와서 return 하게하면 훨씬 메모리 효율적
    # yield from 이란?
    # 오류 반환도 가능, throw 로 받음.

def func1():
    sentence = "컴퓨터(영어: Computer, 문화어: 콤퓨터, 순화어: 전산기)는 진공관"
    result = index_words(sentence)
    print(result)

def func2():
    sentence = "컴퓨터(영어: Computer, 문화어: 콤퓨터, 순화어: 전산기)는 진공관"
    it = index_iter(sentence)
    #print(type(it))
    for i in it:
        print(i)

if __name__ == "__main__":
    #func1()
    func2()