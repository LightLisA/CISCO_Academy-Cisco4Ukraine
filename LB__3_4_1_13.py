class WeekDayError(Exception):
    pass


class Weeker:
    __daysOfWeek = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']

    def __init__(self, day):
        try:
            self.__currentDay = Weeker.__daysOfWeek.index(day)
        except ValueError:
            raise WeekDayError

    def __str__(self):
        return Weeker.__daysOfWeek[self.__currentDay]

    def add_days(self, n):
        self.__currentDay = (self.__currentDay + n) % 7

    def subtract_days(self, n):
        self.__currentDay = (self.__currentDay - n) % 7


try:
    weekday = Weeker('Mon')
    print(weekday)
    weekday.add_days(15)
    print(weekday)
    weekday.subtract_days(23)
    print(weekday)
    weekday = Weeker('Monday')
except WeekDayError:
    print("Sorry, I can't serve your request.")
