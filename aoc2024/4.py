with open('data.txt', 'r') as f:
    lines = f.readlines()
nums = [line.split('   ') for line in lines]
left, right = [int(n[0]) for n in nums], [int(n[1]) for n in nums]
left.sort()
right.sort()

print(sum(abs(l - r) for l, r in zip(left, right)))
