from PriorityQueue import PriorityQueue
from Party import Party

parties, seats = map(int, input().split())
queue = PriorityQueue()

# Add parties to PriorityQueue and also parliament
for _ in range(parties): 
    queue.Add(Party(int(input())))

# Allocate seats
for _ in range(seats): 
    queue.tree[1].seats += 1
    queue.tree[1].value = queue.tree[1].votes / (queue.tree[1].seats + 1)
    queue.SwimDown(1)

# Print votes
for party in queue.items:
    print(party.seats)

