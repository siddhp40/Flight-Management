class Airport():
      
    def __init__(self, code, city, country):
        self._code = code
        self._city = city
        self._country = country

    def __repr__(self):
        return ("{} ({}, {})".format(self._code, self._city, self._country))
          
    def getCode(self):
        return self._code
    
    def getCity(self):
        return self._city

    def getCountry(self):
        return self._country
        
    def setCity(self, newCity):
        self._city = newCity

    def setCountry(self, newCountry):
        self._country = newCountry