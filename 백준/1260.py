from collections import deque

N,M,R = map(int,input().split())

result_d = []
result_b = []

graph = []
visited = [False] * (N+1)
for i in range(N+1):
    graph.append([])


for i in range(1,M+1):
    current_node, next_node = map(int,input().split())
    graph[current_node].append(next_node)
    graph[next_node].append(current_node)


def dfs(graph, v, visited):
    visited[v] = True
    result_d.append(v)
    graph[v].sort()
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)
            
dfs(graph, R, visited)


visited = [False] * (N+1)
def bfs(graph, v, visited):
    queue = deque([v])
    visited[v] = True
    while queue:
        node = queue.popleft()
        result_b.append(node)
        for i in graph[node]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

bfs(graph, R, visited)

print(' '.join(map(str,result_d)))
print(' '.join(map(str,result_b)))