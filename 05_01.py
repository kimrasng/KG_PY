# 반복문을 탈출시키는 break 문

# for i in range(1, 100):
#     print("for문을 %d번 실행했습니다." % i)
#     break

# 계속되는 반복을 논리적으로 빠져나가는 방법
# 반복문으로 다시 돌아가게 하는 continue문

# 입력 두수를 더하는 문한반복 프로그램에서 break 문으로 첫 번째 수에 0이 입력될 때 자동으로 종료(아래 결과와 같이 출력)

# hap = 0
# a, b = 0, 0

# while True:
#     a = int(input("첫번째 수를 입력하세요 : ")) # a값을 입력
#     if(a == 0): # 입력한 a값이 0이면 아래를 실행한 후 break 문으로 while 문을 탈출
#         break

#     b = int(input("두번째 수를 입력하세요 : "))
    
#     hap = a + b
#     print("%d + %d = %d" % (a, b, hap))

# print("0을 입력해서 탈출하였습니다.")


# 1~100까지 합을 구하는 for문에 누적 합계(hap)가 1000 이상이 되는 시작 지점 알기

# hap, i = 0, 0

# for i in range(1, 101):
#     hap = hap + i
#     if(hap >= 1000):
#         break

# print("1~100까지 합에서 누적 합계(hap)가 1000이상이 되는 시작 지점 : %d" % i)


# 1~100 의 합계를 (3의 배수제외하고) 

# hap, i = 0, 0

# for i in range(1, 101):
#     if i % 3 == 0:
#         continue    # continue == 건너뛰다
#     hap = hap + i

# print("1~100의 합계(3의 배수 제외하고) : %d" % hap)  

# li = []
# while True:
#     user = input("그만 하려면 q를 입력하세요.")
#     if user == 'q':
#         print("프로그램을 종료합니다")
#         break
#     li.append(int(user))
# print("입력숫자의 합 : %d" % sum(li))    # len()리스트 요서의 갯수를 알고자 할때)



# li = []
# while True:
#     user = input("그만 하려면 q를 입력하세요.")
#     if user == 'q':
#         print("프로그램을 종료합니다")
#         break
#     li.append(int(user))
# print("입력숫자의 평균 : %f" % (sum(li)/len(li)))    # len()리스트 요서의 갯수를 알고자 할때)


li = []
while True:
    user = input("그만 하려면 q를 입력하세요.")
    if user == 'q':
        print("프로그램을 종료합니다")
        break
    li.append(int(user))
avg = sum(li)/len(li)

for i in li:
    if i >= avg:
        print(i)