aa=[10, 20, 30, 40]
print(aa[-1])

print(aa[-2])

print(aa[0:3])

print(aa[2:4])

print(aa[2:])

print(aa[:2])

aa = [10, 20, 30]
bb = [40, 50, 60]
print(aa+bb)

print(aa*3)

aa=[10, 20, 30, 40, 50, 60, 70]
print(aa[::2])
print(aa[::3])
print(aa[::-2])
print(aa[::-3])
print(aa[::-1])

aa=[10, 20, 30]
aa[1]=[200]
print(aa)

aa[1] = 200
print(aa)

aa[1:2] = [200, 201]
print(aa)

aa=[10, 20, 30]
del(aa[1])
print(aa)

aa=[10, 20, 30, 40, 50]
aa[1:4]=[]

print(aa)

aa=[10, 20, 30]; aa=[]; print(aa)

aa=[10, 20, 30]; aa=None; print(aa)

aa=[10, 20, 30]; del(aa); print(aa)

myList = [30, 10, 20]
print("현제리스트 : %s" % myList)

myList.append(40)
print("append(40)후의 리스트 : %s" % myList)

print("pop()후의 리스트 : %s" % myList.pop())
print("pop()후의 리스트 : %s" % myList)
myList.sort()
print("sort()후의 리스트 : %s" % myList)

print("reverse()후의 리스트 : %s" % myList)
print("20값의 위치 %s" % myList)
print("20값의 위치 %s" % myList.index(20))
myList.insert(2, 222)
print("insert(2, 222)후의 리스트 : %s" % myList)

myList.remove(222)
print("remove(222)후의 리스트 : %s" % myList)

myList.extend([77, 88, 77])
print("extend([77, 88, 77])후의 리스트 : %s" % myList)

print("77값의 개수 : %d" % myList.count(77))

myList = [30, 10, 20]
newlist = sorted(myList)
print("sorted()후의 myList:%s" % myList)
# sort 함수는 리스트명.sort()형식으로 "리스트형의 메소드"이며 리스트 원본값을 직접 수정
# sotred 함수는 sorted(리스트명) 형식으로 "내장함수" 이며 리스트 원본 값은 그대로이고 정렬 값을 변환