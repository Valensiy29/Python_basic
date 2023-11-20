class Date:
    def __init__(self,date):
        self.date = date.split('-')
    def set_date(self):
        if int(self.date[0]) in range(0,30) and int(self.date[1]) in range(0,12) and self.date == '2023':
            pass

print(Date('10-12-2077').set_date())