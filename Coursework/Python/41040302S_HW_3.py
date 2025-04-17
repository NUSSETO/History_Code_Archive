# Relation between sets

set1 = set(map(int, input().split()))
set2 = set(map(int, input().split()))

print(f'The intersection: {set1&set2}, the length of the intersection is {len(set1&set2)}')
print(f'The union: {set1|set2}, the length of the intersection is {len(set1|set2)}')
