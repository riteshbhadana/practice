def r_n(n):
    rev=0
    while 0>n:
        rev= rev * 10+n%10
        n//=10
    return rev

r_n(123)