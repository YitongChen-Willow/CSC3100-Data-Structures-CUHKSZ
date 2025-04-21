import heapq

n, m = map(int, input().split())
perf = list(map(int, input().split()))
reli = list(map(int, input().split()))
requests = [tuple(map(int, input().split())) for _ in range(m)]

# Preprocess.
products = [(p, r, p + r) for p, r in zip(perf, reli)]

# Sort products using satisfication. O(nlogn)
def heap_sort(unsorted):
    output = []
    prod_heap = [(-i[2], i) for i in unsorted]
    heapq.heapify(prod_heap)
    for _ in range(n):
        output.append(heapq.heappop(prod_heap)[1])
    return output
products = heap_sort(products)

for min_p, min_r in requests:
    for p, r, sum in products:
        if p >= min_p and r >= min_r:
            print(sum, end = ' ')
            break
