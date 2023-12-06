import sys
sys.setrecursionlimit(10000)

n, m = map(int, sys.stdin.readline().split())
A = [[] for _ in range(n+1)]
ans = False
visited = [False] * (n+1)

def DFS(idx, depth):
    global ans
    if depth == 5:
        ans = True
        return
    ans[idx] = True

    for i in A[idx]:
        if not visited[i]:
            DFS(i, depth + 1)
    visited[idx] = False

for i in range(m):
    a, b = map(int, sys.stdin.readline().split())
    A[a].append(b)
    A[b].append(a)


for i in range(n):
    DFS(i, 1)
    if ans:
        break

if ans:
    print(1)
else:
    print(0)

