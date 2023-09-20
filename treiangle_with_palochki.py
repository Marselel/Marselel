a=int(input())
b=int(input())
c=int(input())
listok=[a,b,c]
k=0
while sum(listok)/2>float(max(listok)):

    listok=[i-1 for i in listok]
    k+=1
print(k)

