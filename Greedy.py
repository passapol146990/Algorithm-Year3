import heapq as h
import sys as s

def construc(edges, end):
    adj = [[] for _ in range(end)]
    for u, v, wt in edges:
        adj[u].append([v, wt])
        adj[v].append([u, wt])
    return adj

def greedy(end, node, start):
    adj = construc(node, end)
    pq = []
    dist = [s.maxsize] * end
    h.heappush(pq, [0, start]) 
    dist[start] = 0

    while pq:
        d, u = h.heappop(pq)
        if dist[u] < d:
            continue
        for v, weight in adj[u]:
            if dist[v] > dist[u] + weight:
                dist[v] = dist[u] + weight
                h.heappush(pq, [dist[v], v])
    return dist

start = 0
end = 14
node = [[0, 1, 4],[0, 7, 8],[1, 7, 11],[1, 2, 8],[7, 8, 7],[7, 6, 1],[6, 8, 6],[8, 2, 2],[2, 5, 4],[2, 3, 7],[6, 5, 2],[3, 5, 14],[3, 4, 9],[5, 4, 10]]

result = greedy(end, node, start)
print(result)

    
