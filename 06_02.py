list1 = []  # 1차원 리스트로 사용할 list1(행)과 2차원 리스트로 사용할 lust2(열)준비
list2 = []
value = 1   # value는 리스트에 입력할 1~12의 값으로 사용할 변수

for i in range(0, 3):   # 리스트의 행 단위 만들기 위해 3회 반복
    for k in range(0, 4):   # 4회 반복해 항목 4개인 1차원 리스트 생성하는데, 처음에는 [1, 2, 3, 4]열의 값의 리스트를 만듬
        list1.append(value)
        value += 1
    list2.append(list1) # 2차원 리스트에 추가
    list1 = []  # 1차원 리스트를 다시 비움
for i in range(0, 3):   # 2차원 리스트 출력
    for k in range(0, 4):   # '리스트명[행][열]' 방식으로 각 항목 출력
        print("%d" % list2 [i][k], end="    ")
    print("")   # 행 하나 출력 후 한 행 띄워서 출력 위해 print()문 사용