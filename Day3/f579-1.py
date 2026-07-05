a, b = map(int, input().split())
n = int(input())
ans = 0

for _ in range(n):
    cart = list(map(int, input().split()))
    cart.sort()
    for i in cart:
        if i >= 0: break
        cart.remove(-1*i)
    if (a in cart) and (b in cart):
        ans += 1

print(ans)