def arrayElementOnce(arr):
    htable={}
    for i in arr: 
        if i in htable:
            htable[i]=htable[i]+1
        else: 
            htable[i]=1
    op=[]
    for j in htable.keys():
        if htable[j]==1: 
            op.append(j)
    print(op)

arr = [7, 7, 1, 1, 2,3,4,5, 5, 6, 7,6,9,8,9]
arrayElementOnce(arr)