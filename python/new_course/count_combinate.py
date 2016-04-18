def count(n,k):
    if k == 0: return 1
    if k > n: return 0
    return count(n - 1, k) + count(n - 1, k - 1)


# x,y = map(int, input().split())

print(count(map(int, input().split())))
