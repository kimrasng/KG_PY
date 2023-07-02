# 문제1

# sum = 0
# num = 0

# for num in range(0, 1000):
#     if num % 3 == 0 or num % 5 == 0:
#         sum + num
        
# print(num)

# print(sum(num for num in range(1, 1000) if num % 3 == 0 or num % 5 == 0))
# 컴프리핸쎤 ==> 수식 for in range() if 조건식

# 문제2

# sum, sqrsum = 0, 0
# for i in range(1, 101):
#     sum += i    # 합
#     sqrsum += i*i   # 제곱의 합

# print(sum*sum - sqrsum) # 합의 제곱 - 제곱의 합

# print(abs(sum(num for num in range(1, 101))**2 - sum(num**2 for num in range(1, 101))))

# perfect number

# N = int(input("Input a natural number: "))  # 숫자를 하나 입력한다

# result = [] # 완전수를 저장할 리스트

# for i in range(1, N+1): # 1부터 입력한 숫자까지
#     sum = 0 # 누적 된 숫자 합 변수
#     for j in range(1, i):   # 1부터 i(입력숫자)까지
#         if i%j == 0:    # 앿의 조건이면
#             sum += j    # 약수들의 누적 합을 구한다. sum은 j의 누적합

#         if i == sum:    # i는 약수 끝 숫자와 sum의 자신을 제외한 약수들의 누적합 이 자신과 같으면, 즉완전수면
#             result.append(i)    # 각 숫자를 리스트에 저장

# print(result)


# sumSec = 0  # 초의 총합을 저장할 변수
# for hour in range(24) : # 시간
#     for minute in range(60) : # qns
#         if '3' in str(hour) or '3' in str(minute) : # 시간이나 3이 들어가면
# # str(hour) 에서 만 13시이면 문자변환 후 1, 3으로 분리함. 그래서 시간이나 불에 3이 들어가면 if in문이 참이 된다.
#             sumSec += 60    # 60초씩 더함
# print(sumSec)

temp = [0, 0, 0, 0, 0, 0, 0, 0] # 리스트 생성
for num in range(1, 1001):  # 1~1000
    for tp in (str(num)):   # 각 수샂를 배열로 취급하기 위해 string화 시킴(숫자을 쪼갬 에 100을 1, 0, 0)
        temp[int(tp)]+=1    # 넣을땐 다시 int로 해서 temp에 넣음 ==> 1은 temp[int(tp)]+=1에 넣으면 temp[1]+=1 ==> temp[1] = temp[1] + 1

for i in range(10): # 출력
    print(i, ":", temp[i], "개")