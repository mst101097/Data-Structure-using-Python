def fab(n):
    if n <= 1:
        return n
    else:
        return(fab(n-1)+fab(n-2))
    
count = 6

if count <= 0:
    print("Enter the Number More than 2 ")
else:
    for i in range(count):
        print(fab(i),end=" ")
'''
# if interviewer ask last value of fabonic series than 
if count <= 0:
    print("Enter the Number More than 2 ")
else:
    for i in range(count):
        last_value = fab(i)

    print(last_value)'''
'''
# if interviewer ask sum of fabnnoic series 

if count <= 0:
    print("Enter the Number More than 2 ")
else:
    sum = 0
    for i in range(count):
        sum = sum + fab(i)
    print(sum)'''
