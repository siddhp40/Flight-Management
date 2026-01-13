from Flight import *
from Airport import *

def nextValue(certainLine, index):
    value = ""
    for i in range(index, len(certainLine)):
        if certainLine[i] == ',':
            index = i+1
            break
        else:
            value += certainLine[i]
    value = value.strip()
    return value, index


    
allAirports = []
allFlights = {}
# Declares global variable allAirport and allFlights
def loadData(airportFile, flightFile):
    
    try:
        with open(airportFile) as f:
            content = f.readlines()
            for line in content:
                # For line in airport.txt
                i = 0
                airportCode, i = nextValue(line, i)
                country, i = nextValue(line, i)
                city, i = nextValue(line, i)
                # Get value of airportCode Country and City to declare the object
                oneAirport = Airport(airportCode, city, country)
                allAirports.append(oneAirport)
                # Append to list

    except FileNotFoundError:
        print("Error when opening the file")
        return 0
        # Throw error if you file can't be opened
    listAllFlights = []
    try:
        with open(flightFile) as f:
            content = f.readlines()
            for line in content:
                i = 0
                originAirport = None
                destAirport = None
                flightCode, i = nextValue(line, i)
                originCode, i = nextValue(line, i)
                destCode, i = nextValue(line, i)

                for oneAirport in allAirports:
                    if oneAirport.getCode() == originCode:
                        originAirport = oneAirport
                    elif oneAirport.getCode() == destCode:
                        destAirport = oneAirport
                    if originAirport is not None and destAirport is not None:
                        listAllFlights.append(Flight(flightCode, originAirport, destAirport))
                        break

                # Find the city and country of originCode and destCode so we can make it an Airport Object
                # Create the final flight object and append to list all flights

    except FileNotFoundError:
        print("Error when opening the file")
        return 0
    
    for oneAirport in allAirports:
        airportCode = oneAirport.getCode()
        listOneOrigin = []
        for oneFlight in listAllFlights:
            flightOrigin = (oneFlight.getOrigin()).getCode()
            if flightOrigin == airportCode:
                listOneOrigin.append(oneFlight)
        allFlights[airportCode] = listOneOrigin
        # Add keys by reading oneairport and add values by reading listOneOrigin
    return True

def getAirportByCode(code):
    # Finds all airportCodes with the airport
    # Done by reading all codes in allAirports
    # If code matches code given then return the airport
    for oneAirport in allAirports:
        airportCode = oneAirport.getCode()
        if code == airportCode:
            return oneAirport

def findAllCityFlights(city):
    # First I get all the keys so I can access the dictionary
    codeList = []
    cityList = []
    for airport in allAirports:
        codeList.append(airport.getCode())
    # Then I make sure either the origin of the airport or the destination of the airport is the city we are looking for
    # If it is I add it to a list and then return the list
    for code in codeList:
        for flight in allFlights[code]:
            if (flight.getOrigin()).getCity() == city:
                cityList.append(flight)
            elif (flight.getDestination()).getCity() == city:
                cityList.append(flight)
    return cityList

def findAllCountryFlights(country):

    codeList = []
    countryList = []
    for airport in allAirports:
        codeList.append(airport.getCode())
    
    # Instead of checking for the city I swap for the country and use the same code from above
    for code in codeList:
        for flight in allFlights[code]:
            if (flight.getOrigin()).getCountry() == country:
                countryList.append(flight)
            elif (flight.getDestination()).getCountry() == country:
                countryList.append(flight)
        
    return countryList

def findFlightBetween(origAirport, destAirport):

    # I first check direct flight by looking at flights that start from origAirport by using the .getCode()
    # Then I check if the destination code is the same as the destinationairport given
    # If found then it is a direct flight and we can just return that
    # If not the code below will be run which checks for inbetween flights
    flightsWithOrigin = allFlights[origAirport.getCode()]
    for flights in flightsWithOrigin:
        finalDest = (flights.getDestination()).getCode()
        if finalDest == destAirport.getCode():
            return "Direct Flight: {} to {}".format(origAirport.getCode(), destAirport.getCode())

    # I get keys of all the destinations in flightsWithOrigins and then check the destination of those to see if it matches destAirport
    # If it does I add it to a set
    inBetweenFlights = set()
    for flights in flightsWithOrigin:
        inBetweenFlight = (flights.getDestination()).getCode()
        allInBetweenFlights = allFlights[inBetweenFlight]
        for betweenFlight in allInBetweenFlights:
            finalDest = (betweenFlight.getDestination()).getCode()
            if finalDest == destAirport.getCode():
                inBetweenFlights.add(inBetweenFlight)
    # I return the set if it contains some elements, if not I just return -1 representing no flight found
    
    if len(inBetweenFlights) == 0:
        return -1
    return inBetweenFlights

def findReturnFlight(firstFlight):
    # I look at the flights with origin of the destination of the first flight
    # Then I see if any of those destination has the orginal origin as the destination
    # If so I return the return flight
    # If not I return -1 which means no return flight found

    destinationFlights = allFlights[(firstFlight.getDestination()).getCode()]
    for flight in destinationFlights:
        if (flight.getDestination()).getCode() == (firstFlight.getOrigin()).getCode():
            return flight

    return -1