import sqlite3
CONN = sqlite3.connect("national_parks.db")
CURSOR = CONN.cursor()


class NationalPark:
    all = []

    def __init__(self, name):
        self.name = name
        NationalPark.all.append(self)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if  hasattr(self, 'name'):
            raise Exception("Cannot change the name after instantiation.")
        elif not isinstance(name, str) or not (len(name) >= 3):
            raise Exception("Needs to be longer than 3")
        else:
            self._name = name

    def trips(self):
        return [trip for trip in Trip.all if type(Trip) and trip.national_park == self]

    def visitors(self):
        return list(set(trip.visitor for trip in Trip.all if type(Visitor) and trip.national_park == self))
    
    def total_visits(self):
        trip_list = self.trips()
        if  len(trip_list) >= 1:
            return len(trip_list)
        else:
            return 0
    
    def best_visitor(self):
        visitor_count = {}
        for trip in Trip.all:
            if trip.national_park == self:
                visitor_count[trip.visitor] = visitor_count.get(trip.visitor, 0) + 1

        if visitor_count:
            max_visits = max(visitor_count.values())
            best_visitors = [visitor for visitor, visits in visitor_count.items() if visits == max_visits]
            return best_visitors[0]
        else:
            return None
        # park_visitor = [trip.visitor for trip in Trip.all if trip.national_park == self]
        # breakpoint()
        # return [visitor for visitor in Visitor.all if visitor.name == park_visitor]
        #search Trip for visitor with the most visits
        #search Visitor for the visitor
            #

class Trip:
    all = []

    def __init__(self, visitor, national_park, start_date, end_date):
        self.visitor = visitor
        self.national_park = national_park
        self.start_date = start_date
        self.end_date = end_date
        Trip.all.append(self)

    @property
    def start_date(self):
        return self._start_date
    
    @start_date.setter
    def start_date(self, start_date):
        if isinstance(start_date, str) and len(start_date) >= 7:
            if format(start_date):
                self._start_date = start_date
        return start_date
    
    @property
    def end_date(self):
        return self._end_date
    
    @end_date.setter
    def end_date(self, end_date):
        if isinstance(end_date, str) and len(end_date) >= 7:
            if format(end_date):
                self._end_date = end_date
        return end_date
    
    @property
    def visitor(self):
        return self._visitor
    
    @visitor.setter
    def visitor(self, visitor):
        if isinstance(visitor, Visitor):
            self._visitor = visitor
        else:
            raise ValueError("Invalid visitor type")
        
    @property
    def national_park(self):
        return self._national_park
    
    @national_park.setter
    def national_park(self, national_park):
        if isinstance(national_park, NationalPark):
            self._national_park = national_park
        else:
            raise ValueError("Invalid national park type")


class Visitor:
    all = []

    def __init__(self, name, id = None):
        self.name = name
        self._id = id
        Visitor.all.append(self)

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if isinstance(name, str) and 0 < len(name) < 16:
            self._name = name
        return name

    def trips(self):
        return [trip for trip in Trip.all if isinstance(trip, Trip) and trip.visitor == self]
    
    def national_parks(self):
        return list(set(trip.national_park for trip in Trip.all if trip.visitor == self and isinstance(trip.national_park, NationalPark)))
    
    def total_visits_at_park(self, park):
        pass