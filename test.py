
n,a,b = map(int,input().split())
"""
ans = 0
for i in range(1,n+1):
    s = 0
    n2 = i
    while n2>0:
        q,mod = divmod(n2,10)
        s += mod
        n2 = q
    if (a-1)<s<(b+1):
        ans += i

print(ans)
"""
def ans(i):
    s = i
    ans = 0
    while s>0:
        q,mod = divmod(s,10)
        ans += mod
        s = q
    if (a-1)<ans<(b+1):
        return i
    else:
        return 0

print(sum([ans(i) for i in range(1,n+1)]))
