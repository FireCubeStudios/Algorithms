class Flight:
    def __init__(self, time: str, destination: str):
        self.time = time
        self.destination = destination
        self.seconds = Flight.convert(time)

    # Convert the time string 00:00:00 to seconds
    @staticmethod
    def convert(time: str) -> int: 
        hours, minutes, seconds = map(int, time.split(':'))
        return (hours * 3600) + (minutes * 60) + seconds
    
    # Convert seconds to a time string 00:00:00
    @staticmethod
    def convertToString(seconds: int) -> str: 
        return f'{(seconds // 3600):02}:{(seconds % 3600) // 60:02}:{(seconds % 3600) % 60:02}'
    
class TableFlightBoard:
    def __init__(self):
        self.flights = {}

    # add a flight to the search tree
    def add(self, time: str, destination: str): self.flights.update({time: destination})

    # cancel a flight by marking it as cancelled
    def cancel(self, time: str): self.flights.pop(time)

    # delay a flight by cancelling it then adding a new flight at the delay location
    def delay(self, time: str, delaySeconds: int): 
        destination = self.flights[time]
        self.cancel(time)
        self.add(Flight.convertToString(Flight.convert(time) + delaySeconds), destination)

    # reroute a flight by adding a new location to the existing flight
    def reroute(self, time: str, newDestination: str): self.flights[time] = newDestination

    # return the destination of the flight at that time
    def getDestination(self, time: str) -> str: 
        try: return self.flights[time]
        except: return "-"

    # get the earliest deperature from that time
    def getNextDeparture(self, time: str) -> str: 
        seconds = Flight.convert(time)
        current = seconds + 1000000000
        flight = Flight(time, "")
        for key in self.flights:
            flightSeconds = Flight.convert(key)
            if(flightSeconds < current and flightSeconds >= seconds):
                current = flightSeconds
                flight.time = key
                flight.destination = self.flights[key]
        return f'{flight.time} {flight.destination}'

    # get the number of departures between the time interval
    def getDeparturesCount(self, minTime: str, maxTime: str) -> str: 
        count = 0
        min = Flight.convert(minTime)
        max = Flight.convert(maxTime)
        for key in self.flights:
            flightSeconds = Flight.convert(key)
            if(flightSeconds <= max and flightSeconds >= min): count += 1
        return count
    
flights, operations = map(int, input().split())
Board = TableFlightBoard()

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