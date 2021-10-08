n=int(input())
marks=[]
for i in range(n):
    names=input()
    score=float(input())
    record=[names,score]
    marks.append(record)
    markslist=marks.append(score)
marks.sort()
print(marks)
print(markslist)
