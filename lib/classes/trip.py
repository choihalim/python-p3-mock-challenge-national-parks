
class Trip:
    
    def __init__(self, visitor, national_park, start_date, end_date):
        self._visitor = visitor
        self._national_park = national_park

        self.start_date = start_date
        self.end_date = end_date

        visitor.trips(self)
        visitor.national_parks(self.national_park)

        national_park.trips(self)
        national_park.visitors(self.visitor)

    def get_visitor(self):
        return self._visitor
    
    def set_visitor(self, visitor):
        if isinstance(visitor, Visitor):
            self._visitor = visitor
        else:
            raise Exception("Visitor must be of type Visitor.")

    def get_national_park(self):
        return self._national_park
    
    def set_national_park(self, national_park):
        if isinstance(national_park, NationalPark):
            self._national_park = national_park
        else:
            raise Exception("National Park must be of type National Park.")
    
    national_park = property(get_national_park, set_national_park)
    visitor = property(get_visitor, set_visitor)

from classes.visitor import Visitor
from classes.national_park import NationalPark