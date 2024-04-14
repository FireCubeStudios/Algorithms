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