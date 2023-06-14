
n = int(input())
m = int(input())

graph = [[] for i in range(n+1)]

for i in range(n):
    a, b = map(int, input().split())
    graph[a] += [b]
    graph[b] += [a]

visit = [0] * (n+1)

def dfs(graph, v, visit:
    visit[v] = 1
