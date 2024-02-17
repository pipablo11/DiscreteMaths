from math import sqrt, ceil

def fermat_factorization(n):
    x = ceil(sqrt(n))
    b = sqrt(x*x - n)
    while b - int(b) != 0:
        x = x+1
        b = sqrt(x*x - n)

    f1 = x + b
    f2 = x - b
    print("[+] N = {} \n[+] a == {} \n[+] b == {}\n[+] f1 == {} \n[+] f2 == {}".format(n, x, b, f1, f2))


fermat_factorization(125513)

