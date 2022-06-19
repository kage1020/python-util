def inv_gcd(u, v):
    r0 = u
    s0 = 1
    t0 = 0
    r1 = v
    s1 = 0
    t1 = 1
    while(r1 != 0):
        q = r0 // r1
        r = r0 - q * r1
        s = s0 - q * s1
        t = t0 - q * t1
        r0 = r1
        s0 = s1
        t0 = t1
        r1 = r
        s1 = s
        t1 = t
    return t0


def encrypt(e, m, n):
    r = 1
    for i in range(len(e)):
        if e[i] == 1: r = r * m % n
        m = m * m % n
    return r


def main():
    print('input e, p and q: ', end='')
    e, p, q = map(int, input().split())
    n = p * q
    phi = (p - 1) * (q - 1)
    d = inv_gcd(phi, e)
    if d < 0: d = phi + d
    print('e: {}, p: {}, q: {}, n: {}, phi: {}, d: {}'.format(e, p, q, n, phi, d))
    
    print('input m: ', end='')
    m = int(input())
    e = [int(i) for i in bin(e)[2:]][::-1]
    print(e)
    c = encrypt(e, m, n)
    print('encrypted m: ', c)
    d = [int(i) for i in bin(d)[2:][::-1]]
    m_ = encrypt(d, c, n)
    print('decrypted m: ', m_)


if __name__ == '__main__':
    main()
