class Visitor:

    def __init__(self, name):
        self.name = name
        self._trips = []
        self._national_parks = []

    def get_name(self):
        return self._name

    def set_name(self, name):
        if type(name) == str and len(name) >= 1 and len(name) <= 15 and not hasattr(self, 'name'):
            self._name = name
        else:
            raise Exception(
                "Name is not a string or not between 1 to 15 characters or name already exists")

    def trips(self, new_trip=None):
        from classes.trip import Trip
        if new_trip and isinstance(new_trip, Trip):
            self._trips.append(new_trip)
        return self._trips

    def national_parks(self, new_national_park=None):
        from classes.national_park import NationalPark
        if new_national_park and isinstance(new_national_park, NationalPark) and new_national_park not in self._national_parks:
            self._national_parks.append(new_national_park)
        return self._national_parks

    name = property(get_name, set_name)
