import time
n=int(input())
x=int(input())
answer=[-100001]
def isCan(nums, num,x):
    for  i in nums:
        if i+x==num:
            return False
    return True
t=time.clock()
for i in range(1,n+1):
    if isCan(answer,i,x):
        answer.append(i)
print(t)