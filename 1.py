
num1 = int(input())
num2 = int(input())
li=[]
s=set()
count=0
for i in range(num1,num2+1):
    li.append(i)
for i in range(0,len(li)):
    st=str(li[i])
    for j in range(0,len(st)):
        s.add(st[j])
    if(len(st)==len(s)):
        count+=1
    s.clear()
    
print(count)
