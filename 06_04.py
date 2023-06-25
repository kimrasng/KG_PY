dic1 = {1:'a', 2:'b', 3:'c'}
print(dic1)

dic2 = {'a':1, 'b':2, 'c':3}
print(dic2)

# 키와 값의 위치를 사용자가 정할수 있다.
# 키와 값은 사용자가 지정하는 것이지 규정은 없음
# 주의할 점 : 딕셔너리에는 순서가 없어 생상한 순서대로 딕셔너리가 구성되어 있다는 보장 없음
student1 = {'학번' : 1000, '이름' : '홍길동', '학과': '컴퓨터학과'}
print(student1)

student1['연락처']='010-1111-2222'
print(student1)
student1['학과']='파이썬학과'
print(student1)
del(student1['학과'])
print(student1)
student1 = {'학번' : 1000, '이름' : '홍길동', '학과': '컴퓨터학과', '학번' : 2000}
student1.get('주소')
print(student1.keys())
print(list.student1.keys())
print(student1.values())

list(student1.values())
student1.items()

# 딕셔너리.items() 함수를 사용하면 튜플 형태로도 구할 수 있음