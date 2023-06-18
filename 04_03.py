# for i in range(0, 3 ,1):
#     for k in range(0, 2, 1):
#         print("안녕(i값 : %d, k값 : %d)" % (i, k))

# 외부 변수인 i는 계속 0, 1, 2로 변경된 후 끝나지만, 내부 변수인 k는 0과 1을 계속 반복

# 중첩 for 문
    # 반복문안에 반복문 (종속문장에 반복문이 준재)
# 처리 순서
    # 외부 변수인 i는 계속 0, 1, 2로 변경된 후 끝나지만, 내부 변수인 k는 0과 1을 계속 반복


# 중첩 for문 활용 2단부터 9단까지 구구달 세로로 출력


# for i in range(2, 10, 1):
#     for k in range(1, 10, 1):
#         print(" %d x %d = %d" % (i, k, i*k))
#     print("")


# 중첩 for 문 활용 2단부터 9단까지 구구단 가로 출력


# for k in range(1, 10, 1):   # i는 1~9까지에 대해 각 단을 출력. i구구단에서 곱하는 뒷자리수
#     for i in range(2, 10, 1):   # k는 각 단/ i(1~9까지의 값), k(단), i*k(단*1~9까지의 값)
#         print(" %2d x %2d = %2d" % (k, i, i*k), end="  ")   # end = "    "는 옆으로 출력
#     print("")   # 구구단의 각행을 출력 후 줄바꿈


N = int(input("수 입력 : "))

for i in range(1, N, 1):
    su = 0
    for k in range(1, i+1):
        if k % 2==0:
            su = su + 1 # su += 1같다
    print("%d : %d 개" % (i, su))