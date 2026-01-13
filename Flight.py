from Airport import *
class Flight():

    def __init__(self, flightNo, origin, destination):
        # Initalizes flightNo, origin and destination
        result1 = isinstance(origin, Airport)
        result2 = isinstance(destination, Airport)
        if not(result1) or not(result2):
            raise TypeError("the origin and destination must be airport objects")
        self._flightNo = flightNo
        self._origin = origin
        self._destination = destination
    
    def __repr__(self):
        toReturn = "Flight: {} from {} to {}".format(self._flightNo, self._origin.getCity(), self._destination.getCity())
        if self.isDomesticFlight():
           toReturn += " {domestic}"
        else:
            toReturn += " {international}"
        return toReturn
    def __eq__(self, other):
        # To make sure no error is thrown, I check if other is a Flight object before comparing values
        # I return False if other is not a Flight
        # I don't throw an error as its possible I am comparing a Flight object with another data type
        result1 = isinstance(other, Flight)
        if not(result1):
            return False
        if self._origin == other._origin and self._destination == other._destination:
            return True
        return False

    def getFlightNumber(self):
        return self._flightNo

    def getOrigin(self):
        return self._origin
    
    def getDestination(self):
        return self._destination
        
    def isDomesticFlight(self):
        # Compares the origin country and the destination country and returns true if they are the same
        # If not I return false
        if self._origin.getCountry() == self._destination.getCountry():
            return True
        return False

    def setOrigin(self, newOrigin):
        self._origin = newOrigin

    def setDestination(self, newDestination):
        self._destination = newDestination



