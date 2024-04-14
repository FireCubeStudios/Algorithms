from SearchTree import RedBlackTree
from Flight import Flight

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
    
class TreeFlightBoard:
    def __init__(self):
        self.tree = RedBlackTree()
        self.cancelled = set()

    # check if a flight is not cancelled or null
    def validate(self, flight: Flight):
        if(flight is None): return False
        else: return not(flight in self.cancelled)

    # add a flight to the search tree
    def add(self, time: str, destination: str): self.tree.add(Flight.convert(time), Flight(time, destination))

    # cancel a flight by marking it as cancelled
    def cancel(self, time: str): 
        flight = self.tree.find(Flight.convert(time))
        if(self.validate(flight)): self.cancelled.add(flight)

    # delay a flight by cancelling it then adding a new flight at the delay location
    def delay(self, time: str, delaySeconds: int): 
        seconds = Flight.convert(time)
        flight = self.tree.find(seconds)
        if(self.validate(flight)):
            self.cancelled.add(flight)
            seconds += delaySeconds
            self.tree.add(seconds, Flight(Flight.convertToString(seconds), flight.destination))

    # reroute a flight by adding a new location to the existing flight
    def reroute(self, time: str, newDestination: str): self.add(time, newDestination)

    # return the destination of the flight at that time
    def getDestination(self, time: str) -> str: 
        flight = self.tree.find(Flight.convert(time))
        return flight.destination if(self.validate(flight)) else "-"

    # get the earliest deperature from that time
    def getNextDeparture(self, time: str) -> str: 
        flight = self.tree.ceiling(Flight.convert(time))
        if(self.validate(flight)):
            return f'{flight.time} {flight.destination}'
        else: return self.getNextDeparture(Flight.convertToString(flight.seconds + 1))

    # get the number of departures between the time interval
    def getDeparturesCount(self, minTime: str, maxTime: str) -> str: return self.countRecursive(Flight.convert(minTime), Flight.convert(maxTime), 0, self.tree.root)
    def countRecursive(self, minKey, maxKey, count, node) -> int:
        if(node.key >= minKey and node.key <= maxKey and self.validate(node.value)):
            count += 1
        if(node.left is not None and self.validate(node.left.value)):
            count = self.countRecursive(minKey, maxKey, count, node.left)
        if(node.right is not None and self.validate(node.right.value)):
            count = self.countRecursive(minKey, maxKey, count, node.right)
        return count