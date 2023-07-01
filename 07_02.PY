# def func1():
#     a=10
#     print("func1()에서 a값 %d" % a)

# def func2():
#     print("func2()에서 a값 %d" % a)

# a = 20  # a를 선언(전역 변수)

# func1()   # func1() 함수 호출
# func2()  # func2() 함수호출

# # 지역 변수와 전역 변수의 이해
#     # 지역 변수 : 한정된 지역에서만 사용
#     # 전역 변수 : 프로그램 전체에서 사용

# def func1():
#     global a    # 이 함수 안에서는 전역변수 global 예약어로 a 변수를 전역 변수로 지정
#     a=10
#     print("func1()에서 a값 %d" % a)
# # 전역 변수 a값을 10으로 변경하므로 func1()과 func2() 함수에서 모두 전역 변수 a값을 10으로 출력

# def func2():
#     print("func2()에서 a값 %d" % a)

# a = 20

# func1()
# func2()

# def func1():
#     result = 1000
#     return result

# def func2():
#     print("반환값이 없는 함수")

# hap = 0

# hap = func1() # 반환값이 있는 함수인 finc1()을 호출하면 func1() 실행우 func1()의 반환값을 hap에 넣고
# print("func1()에서 돌려준 값 ==> %d" % hap) # 출력
# func2() # 반환값이 없는 함수인 func2()를 호출하면 변환 없음


# def multi(v1, v2):
#     retList = []    # 빈 리스트를 준비
#     res1 = v1 + v2
#     res2 = v1 - v2
#     retList.append(res1)    # 리스트ㅔ 값을 추가
#     retList.append(res2)
#     return retList  # 리스트 반환

# myList = []
# hap, sub = 0, 0

# myList = multi(100, 200)    # 반환한 리스트의 값을 각 변수에 대입
# hap = myList[0]
# hap = myList[1]


def para2_func(*para):  #(10,20,30,40,50,60,70,80,90,100)   *para로 매개변수 설정
    result = 0
    for num in para:    # result = v1+...v10

def para2_func(v1, v2, v3):
    result = 0
    result = v1 + v2 + v3
    return result

hap = 0

hap = para2_func(10,20)
print("매개변수가 2개인 함수를 호출한 결과 ==> %d" % hap)
hap = para3_func(10, 20, 30)
print("매개변수가 2개인 함수를 호출한 결과 ==> %d" % hap)
    
def para_func(v1, v2, v3=0, v4=0, v5=0, v6=0, v7=0, v8=0, v9=0, v10=0):
    result = 0
    result = v1 + v2 + v3 + v4 + v5 + v6 + v7 + v8 + v9 + v10
    return result

hap = 0

hap = para_func(10,20)
print("매개변수가 2개인 함수를 호출한 결과 ==>%d" % hap)

hap = para_func(10, 20, 30, 40, 50, 60, 70, 80, 90, 100)
print("매개변수가 10개인 함수를 호출한 결과 ==>%d" % hap)
