from SearchTree import RedBlackTree
from Flight import Flight

class FlightBoard:
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
        return f'{flight.time} {flight.destination}' if(self.validate(flight)) else "-"

    # get the number of departures between the time interval
    def getDeparturesCount(self, minTime: str, maxTime: str) -> str: return "-"