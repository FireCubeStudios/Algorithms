from FlightBoard import FlightBoard

flights, operations = map(int, input().split())
Board = FlightBoard()

# Add Flights to FlightBoard
for _ in range(flights):
    time, destination = map(str, input().split())
    Board.add(time, destination)

# Execute operation and print result
for _ in range(operations):
    operation = input().split()
    instruction = operation[0]
    if(instruction == "cancel"): Board.cancel(operation[1])
    elif(instruction == "delay"): Board.delay(operation[1], int(operation[2]))
    elif(instruction == "reroute"): Board.reroute(operation[1], operation[2])
    elif(instruction == "destination"): print(Board.getDestination(operation[1]))
    elif(instruction == "next"): print(Board.getNextDeparture(operation[1]))
    elif(instruction == "count"): print(Board.getDeparturesCount(operation[1], operation[2]))
