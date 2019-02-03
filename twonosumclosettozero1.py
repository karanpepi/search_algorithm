def sumCloseTo0(arr):
    arr.sort()
    i=0
    j=arr.__len__()-1
    a=arr[i]
    b=arr[j]
    sum = abs(a+b)
    temp=0
    while(i<j-1):
        if(abs(arr[i+1]+arr[j]) < abs(arr[i]+arr[j-1]) ):
            i+=1
        else:
            j-=1
        temp = abs(arr[i] + arr[j])
        if (temp < abs(sum)):
            sum = arr[i] + arr[j]
            a=arr[i];b=arr[j]
        # if(i>=j-1):
        #     break
    return "a %d, b %d, sum %d" %(a,b,sum)
 
arr = [1, 60, -10, 70, -80, 85]
print(sumCloseTo0(arr))

