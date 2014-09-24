def euler3():
    n = 600851475143
    i = 2
    while i < n/i:
        if n % i == 0:
            n = n / i

        else:
            i += 1

    print i        

euler3()           


