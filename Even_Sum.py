a=[]
sum_no=0
n=int(input("Enter NO. OF terms "))
for j in range(0,n):
    b=int(input())
    a.append(b)
for i in range(n):
   if a[i]%2==0:
       sum_no=sum_no+a[i]
print(sum_no)
