def compare(x,y):
    if x+y > y+x:
        return True
    return False

def merge_sort(arr, compare_func):

    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2

    left_half = merge_sort(arr[:mid], compare_func)
    right_half = merge_sort(arr[mid:], compare_func)

    return merge(left_half, right_half, compare_func)

def merge(left, right, compare_func):

    sorted_arr = []
    i = j = 0
    
    while i < len(left) and j < len(right):
        if compare_func(left[i], right[j]):
            sorted_arr.append(left[i])
            i += 1
        else:
            sorted_arr.append(right[j])
            j += 1
    
    sorted_arr.extend(left[i:])
    sorted_arr.extend(right[j:])
    
    return sorted_arr

level = int(input().split()[1])

for _ in range(level):

    blocks = input().split()
    blocks.pop(0)
    position = blocks.pop(len(blocks)-1)
    leading = [blocks.pop(int(position)-1)]
    
    sorted_arr = leading + merge_sort(blocks, compare)
    result = "".join(sorted_arr)

    print(result)
    