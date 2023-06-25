tt1 = (10, 20, 30); print(tt1)
tt1 = 10, 20, 30; print(tt1)
# 리스트는 대괄호 []로 생성, 튜플은 소괄호()로 생성
# 튜플은 값을 수정할 수 없으며, 읽기만 가능해 일기 전용 자료를 저장할 때 사용
tt3 = (10); print(tt3)

tt3 = (10,); print(tt3)

tt4 = 10; print(tt4)
# 튜플은 소괄호 ()를 생략 가능, 항목이나 하나인 튜블은 쉼표(,) 붙임

print(tt1 = (10, 20, 30))

print(tt1.append(0))
tt1[0]=40
del(tt1)
# 튜플의 요소는 삭제 등이 안된다(읽기전용이기 떄문에) 단 전부 삭제는 가능
print(tt1 = (10, 20, 30, 40))

print(tt1[0])

print(tt1[0]+tt1[1]+tt1[2])


# 튜플 항목에 접은 가능

print(tt1[1:3])

print(tt1[1:])
print(tt1[:3])
tt2 = ('A', 'B')
tt1 + tt2
tt2*3

myTuple = (10, 20, 30)
myList = list(myTuple)
myList.append(40)
myTuple=tuple(myList)
myTuple

# 예 : 튜플 -> 리스트 -> 튜플 변환