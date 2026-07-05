a, b = map(int, input().split())
n = int(input())
ans = 0

for _ in range(n):
    cart = list(map(int, input().split()))
    x, y = cart.count(a)>cart.count(-1*a), cart.count(b)>cart.count(-1*b)
    if x and y: ans += 1

print(ans)