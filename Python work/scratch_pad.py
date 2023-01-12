def findZigZagSequence(a, n):
    a.sort()
    mid = int((n + 1)/2)-1
    a[mid], a[n-1] = a[n-1], a[mid]

    st = mid + 1
    ed = mid +2
    while(st <= ed) and (ed < n-1):
        a[st], a[ed] = a[ed], a[st]
        st = st + 1
        ed = ed + 1

    for i in range (n):
        if i == n-1:
            print(a[i])
        else:
            print(a[i], end = ' ')
    return

def findLeastNumOfUniqueInts(arr, k) -> int:
        while k:
            for i, x  in enumerate(arr):
                if arr.count(x)<=i:
                    print(i)
                    arr.remove(x)
                    k-=1
        end=list()
        end =[x for x in arr if end.count(x)==0]  
        print(end)    
        return len(end)

print(findLeastNumOfUniqueInts([4,3,1,1,3,3,2], 3))