from Sets import DisjointSet

setsCount, linesCount = map(int, input().split())

Set = DisjointSet(setsCount)

# Read following lines
for _ in range(linesCount):
    operation, set1, set2 = map(int, input().split())
    if operation == 0:
        print(Set.query(set1, set2))
    elif operation == 1:
        Set.union(set1, set2)
    elif operation == 2:
        Set.move(set1, set2)