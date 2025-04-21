from collections import deque

def bfs(start):
    dist = [0 if i == start else -1 for i in range(N + 1)]
    wait_nodes = deque([start])
    while wait_nodes:
        current_node = wait_nodes.popleft()
        for obj_node, w in adj[current_node]:
            if dist[obj_node] == -1:
                dist[obj_node] = dist[current_node] + w
                wait_nodes.append(obj_node)
    end_node = max(key_nodes, key = lambda k: dist[k])
    return dist, end_node

N, D = map(int, input().split())
key_nodes = list(map(int, input().split()))

# Construct adjacent list.
adj = [[] for _ in range(N + 1)]
for i in range(2, N + 1):
    u, w = map(int, input().split())
    adj[u].append((i, w))
    adj[i].append((u, w))

# Start with a random key node. Find one of the end node of key_nodes.
start = key_nodes[0]
dist_s, u = bfs(start)

# Find the other end node of key_nodes.
dist_u, v = bfs(u)
dist_v, _ = bfs(v)

for i in range(1, N + 1):
    print(max(dist_u[i], dist_v[i]))
