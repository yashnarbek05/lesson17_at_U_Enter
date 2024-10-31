from xmlrpc.client import DateTime


class Date:
    def __init__(self, year, month, day):
        if year < 1900:
            print("Enter year bigger than 1900")
            return
        elif not 1 <= month <= 12:
            print("enter month [1,12]")
            return
        elif not 1<= day <= 31:
            print("Enter day in [1,31]")
            return
        self.year = year
        self.month = month
        self.day = day

    def __str__(self):
        return f"{self.day}.{self.month}.{self.year}"

    def show_time(self):
        print("year:", self.year)
        print("month:", self.month)
        print("day:", self.day)
        