
import mul
n=int(input("Enter no of rows in 1st matrix"))
mat1=[]
for i in range(0,n):
  lis=list(map(int,input().split()))
  mat1.append(lis)
x=len(mat1[0])
m=int(input("Enter no of rows in 2nd matrix"))
mat2=[]
for i in range(0,m):
  lis=list(map(int,input().split()))
  mat2.append(lis)
y=len(mat2[0])

if(x==m):
  res=mul.multiply(mat1,mat2)
  print(res)
else:
  print("NOt possible")
