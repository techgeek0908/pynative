def func(n):
    a=[]
    for i in n:
        if i!=1:
            a.append(i)
    return a
list1=[1,1,2,3,4,5,1,2,1]
res=func(list1)
print(res)