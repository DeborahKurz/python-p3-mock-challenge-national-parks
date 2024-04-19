class NationalPark:

    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if  hasattr(self, '_name'):
            raise AttributeError("Cannot change the name after instantiation.")
        elif isinstance(name, str) and len(name) >= 3:
            self._name = name
        return name
        

    def trips(self):
        pass
    
    def visitors(self):
        pass
    
    def total_visits(self):
        pass
    
    def best_visitor(self):
        pass

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

class Visitor:

    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if isinstance(name, str) and 0 < len(name) < 16:
            self._name = name
        return name
    
    def trips(self):
        pass
    
    def national_parks(self):
        pass
    
    def total_visits_at_park(self, park):
        pass