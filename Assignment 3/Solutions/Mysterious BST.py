n, Q = map(int, input().split())
values = list(map(int, input().split()))

nodes = {}
for i in range(1, n+1):
    nodes[i] = {'value': values[i-1], 'exist': 1, 'parent': 0, \
                'left': 0, 'right': 0, 'size': 1}
    
# Construct BST.
for id in range(2, n+1):
    cur_id = 1 
    insert_node = nodes[id]

    while True:
        cur_node = nodes[cur_id]
        if insert_node['value'] > cur_node['value']:
            if not cur_node['right']:
                cur_node['right'] = id
                break
            else:
                cur_id = cur_node['right']
        else:
            if not cur_node['left']:
                cur_node['left'] = id
                break
            else:
                cur_id = cur_node['left']

    insert_node['parent'] = cur_id
    # Update sizes.
    while cur_id:
        nodes[cur_id]['size'] += 1
        cur_id = nodes[cur_id]['parent']

for _ in range(Q):
    op, id, K = map(int, input().split())
    par_id = nodes[id]['parent']

    # Insert or delete.
    if op == 1:
        nodes[id]['exist'] = 0
        if nodes[par_id]['left'] == id:
            nodes[par_id]['left'] = 0
        else:
            nodes[par_id]['right'] = 0
        while par_id:
            nodes[par_id]['size'] -= 1
            par_id = nodes[par_id]['parent']
    else:
        nodes[id]['exist'] = 1
        if nodes[id]['value'] < nodes[par_id]['value']:
            nodes[par_id]['left'] = id
        else:
            nodes[par_id]['right'] = id
        while par_id:
            nodes[par_id]['size'] += 1
            par_id = nodes[par_id]['parent']
    
    cur_id = 1
    while True:
        cur_node = nodes[cur_id]
        if cur_node['right']:
            r_size = nodes[cur_node['right']]['size']
        else:
            r_size = 0
        
        if r_size >= K:
            cur_id = cur_node['right']
        else:
            K -= r_size
            if K == 1:
                break
            K -= 1
            cur_id = cur_node['left']
    
    print(cur_node['size'])
    