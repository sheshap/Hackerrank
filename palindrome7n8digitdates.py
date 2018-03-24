leap=[]
nonleap=[]
nlmonth=[31,28,31,30,31,30,31,31,30,31,30,31]
lmonth=[31,29,31,30,31,30,31,31,30,31,30,31]
leap_year=[]
nonleap_year=[]
pals = []
def pal(start,end):
    count = 0
    if (start < 1000 or end > 9999):
        return 0;
    else:
        for i in range(start,end):
            if i % 4 == 0 and (i %100 != 0 or i % 400 == 0):
                 leap.append(i)
            else:
                 nonleap.append(i)
        for i in range(start,end):
            if i in leap:
                for l in range(1,len(lmonth)+1):
                    for j in range(1,lmonth[l-1]+1):
                        A = str('{:02}'.format(l)+'{:02}'.format(j)+'{:04}'.format(i))
                        if A[::1] == A[::-1]:
                            pals.append(A)
                        B = str('{:00}'.format(l)+'{:00}'.format(j)+'{:00}'.format(i))
                        if B[::1] == B[::-1]:
                            pals.append(B)
            else:
                for l in range(1,len(nlmonth)+1):
                    for j in range(1,nlmonth[l-1]+1):
                        X = str('{:02}'.format(l)+'{:02}'.format(j)+'{:04}'.format(i))
                        if X[::1] == X[::-1]:
                            pals.append(X)
                        Y = str('{:00}'.format(l)+'{:00}'.format(j)+'{:00}'.format(i))
                        if Y[::1] == Y[::-1]:
                            pals.append(Y)
        for i in range(len(pals)):
            if len(pals[i])>=7: #remove this if condition if palindrome of 6 digits is also needed
                count=count+1
        return count

YYYY = input("Enter Year: ")
yy100 = (int(YYYY)//100)*100
print(pal(yy100+1,yy100+101))
