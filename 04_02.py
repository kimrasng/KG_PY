# print("안녕하세요")
# print("안녕하세요")
# print("안녕하세요")
# print("안녕하세요")
# print("안녕하세요")

# for i in range(0, 5, 1):
#     print("안녕하세요")


# range()함수 형식의 for문


# for 변수 in range(시작값, 끝값+1, 증가값):
#   실행 문장


# 리스트 형식의 for문


# for i in [0, 1, 2, 3, 4]:
#     print("안녕하세요")


# 서식이용


# for i in range(0, 5, 1):
#     print("%d : 안녕하세요" % i)

# for i in range[0, 1, 2, 3, 4]:
#     print("%d : 안녕하세요" % i)


# 1~5까지 숫자 출력(세로)


# for i in range(1, 6, 1):
#     print("%d" % i)

# 1~5 까지 숫자 출력(가로)
# for i in range(1, 6, 1):
#     print("%d" % i, end="   ")  # end=" "는 끝에 가로로 이어서 출력


# hap = 1+2+3+4+5+6+7+8+9+10

# print("1에서 10까지의 합계 : %d" % hap)

# for i in range(1, 11, 1):
#     hap = hap + i
# print("1에서 10까지의 합계 : %d" % hap)

# hap = 0 # 누적합을 구할때는 hap의 초기화(변수에 값을 대입)가 필요하다.
# for i in range(1, 11, 1):
#     hap = hap + i # hap 의 누적합
# print("1에서 10까지의 합계 : %d" % hap)


# 500과 1000사이에 있는 홀수의 합계

# hap = 0

# for i in range(499, 1001, 2):
#     hap = hap + i
    
# print("500과 1000사이에 있는 홀수의 합계는 %d" % hap)


# 키보드로 입력한 수까지의 함계 구하기

# hap = 0
# i = 0
# num = 0

# a = int(input("값을 입력하세여 : "))
# for i in range(1, num+1, 1)
#     hap + hap + i

# print("1에서 %d까지의 합계 : %d" % num, hap)


# 시작값과 끝값, 증가값가찌 사용자 입력

# hap = 0
# i = 0
# num1, num2, num3 = 0, 0, 0

# num1 = int(input("시작값을 입력하시오 : "))
# num2 = int(input("끝값을 입력하시오 : "))
# num3 = int(input("증가값을 입력하시오 : "))

# for i in range(num1, num2+1, num3):
#     hap = hap + i

# print("%d 에서 %d 까지 %d 씩만큼 증가한 수의 합계 : %d" % num1, num2, num3, hap)


# for i in ["월", "화", "수", "목", "금", "토", "일"]:
#     print("%s" % i)   # print("%c", % i)도 가능

# for i in ["월", "화", "수", "목", "금", "토", "일"]:
#     print("%s" % i, end="   ")


dan = int(input("단을 입력하세요 : "))

for i in range(1, 10, 1):
    print("%d x %d = %2d" % (dan, i, dan*i))