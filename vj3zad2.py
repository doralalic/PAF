def zbrajanje(N):
    a=5.0
    for i in range(1, N):
        a=a+1/3
    for i in range(1, N):
        a=a-1/3
    print(a)

zbrajanje(200)
zbrajanje(2000)
zbrajanje(20000)