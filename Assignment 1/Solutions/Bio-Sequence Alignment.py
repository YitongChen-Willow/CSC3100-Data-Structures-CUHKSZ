t = int(input())

for _ in range(t):

    length = int(input())
    num = input().split()
    sample = int(input())

    for _ in range(sample):

        match = 1
        pair = {}
        DNA = input()
        
        if len(DNA) != length:
            print("NO")
            continue

        for i in range(length):

            if num[i] not in pair:
                if DNA[i] in pair.values():
                    match = 0
                    break
                pair[num[i]] = DNA[i]
             
            elif pair[num[i]] != DNA[i]:
                match = 0
                break

        if match == 1:
            print("YES")
        else:
            print("NO")
