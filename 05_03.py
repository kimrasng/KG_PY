# a, b, c, d 라는 정수형 변수 선언 후 이 변수에 값을 입력받고 합계 출력하는 프로그램 

# a, b, c, d = 0, 0, 0, 0
# hap = 0

# a = int(input("1번째 숫자 : "))
# b = int(input("2번째 숫자 : "))
# c = int(input("3번째 숫자 : "))
# d = int(input("4번째 숫자 : "))

# hap = a+b+c+d
# print("합계 ==> %d" % hap)



# aa 변수에 리스트를 사용하는 프로그램 으로 수정


# aa = [0, 0, 0, 0]   # a=[0, 0, 0, 0]으로 항복이 4개 있느 리스트 생성
# hap = 0

# aa[0]=int(input("1번째 숫자 : "))   # a대신 aa[0]을 사용
# aa[1]=int(input("2번째 숫자 : "))
# aa[2]=int(input("3번째 숫자 : "))
# aa[3]=int(input("4번째 숫자 : "))

# hap = aa[0] + aa[1] + aa[2] + aa[3]

# print("합계 ==> %d" % hap)

# aa = []
# aa.append(0)
# aa.append(0)
# aa.append(0)
# aa.append(0)
# print(aa)

# a = []

# for i in range(0, 4, 1):
#     aa.append(0)

# print(aa)

# for i in range(0, 100, 1):
#     aa.append(0)

# print(len(aa))  # len() 리스트의 요소의 갯수를 수할때


# aa = []
# hap = 0 # 누적합 구할때 초기화를 반드시 해야한다

# for i in range(0, 4, 1):
#     aa.append(0)
# for i in range(0, 4, 1):
#     aa[i] = int(input(str(i+1)"번째 : "))
# hap = aa[0] + aa[1] + aa[2] + a[3]

# for i in range(0, 4 ,1):    # hap = aa[0] + aa[1] +  + aa[2] + aa[3]
#     hap += aa[i]

# print("합계==>%d" % hap)


# 리스트의 생성과 초기화


# aa = []
# bb = [10, 20, 30]
# cc = ["파이썬", "안녕", "공부"]
# dd = [10, 20, "파이썬"]


aa = []
bb = []
cc = []
value = 0

for i in range(0, 100, 1):
    aa.append(value)
    value += 2

for i in range(0, 100, 1):
    bb.append(aa[99-i])

print("bb[0]에는 %d이, bb[99]에는 %d입니다." % (bb[0], bb[99]))