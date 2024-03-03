from BubbleSort import BubbleSort
from Grade import Grade 

linesCount = int(input())
Sort = BubbleSort()

# Read following lines
for x in range(linesCount):
    name, grade = map(str, input().split())
    Sort.grades.append(Grade(name, grade))

# Sort and print output
Sort.Sort()
for x in range(len(Sort.grades)):
    print(Sort.grades[x].name)