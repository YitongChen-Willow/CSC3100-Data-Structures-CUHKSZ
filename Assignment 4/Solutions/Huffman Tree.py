import heapq

class HuffmanNode:
    def __init__(self, freq, char = None, left = None, right = None):
        self.freq = freq
        self.char = char
        self.left = left
        self.right = right
    
    def __lt__(self, other):
        return self.freq < other.freq
    
string = input()

# Frequency for distinct chars.
freq_dict = {}
for char in string:
    freq_dict[char] = freq_dict.get(char, 0) + 1

if len(freq_dict) == 1:
    print(len(string))
else:
    # Construct Huffman tree.
    freq_heap = [HuffmanNode(freq, char) for char, freq in freq_dict.items()]
    heapq.heapify(freq_heap)

    while len(freq_heap) != 1:
        l, r = heapq.heappop(freq_heap), heapq.heappop(freq_heap)
        node = HuffmanNode(l.freq + r.freq, left = l, right = r)
        heapq.heappush(freq_heap, node)
    
    def create_code(start, cur_code):
        if (start is not None) and (start.char is not None):
            code_dict[start.char] = cur_code
        elif start is not None:
            create_code(start.left, cur_code + '0')
            create_code(start.right, cur_code + '1')

    # Construct codes.
    root = freq_heap[0]
    code_dict = {}
    create_code(root, '')

    bits = sum(len(code_dict[char]) for char in string)
    print(bits)
