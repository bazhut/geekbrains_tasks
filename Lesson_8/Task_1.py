class Date:
    def __init__(self, day, month, year):
        self.date_day = day
        self.date_month = month
        self.date_year = year

    @classmethod
    def set_int_date(cls, date_inp):
        my_date = map(int, str(date_inp).split("-"))
        day, month, year = my_date
        return cls(day, month, year)

    @staticmethod
    def check_date(obj):
        month_days = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
        if obj.date_year % 400 == 0 or obj.date_year % 4 == 0:
            month_days[2] = 29
            if not 0 < obj.date_day <= month_days[obj.date_month]:
                return f"В {obj.date_month} месяце не может быть {obj.date_day} дней!"
        else:
            if not 0 < obj.date_day <= month_days[obj.date_month]:
                return f"В {obj.date_month} месяце не может быть {obj.date_day} дней!"
        if not 0 < obj.date_month < 13:
            return f"В году не может быть месяца - {obj.date_month}!"
        if not 1900 < obj.date_year < 2201:
            return f"Это точно верный год - {obj.date_year}?!"
        return f"Дата введена корректно!"


try:
    date = Date.set_int_date("06-03-2021")
    print(Date.check_date(date))
except ValueError:
    print("Проверьте вводимые данные! Формат ввода: 'dd-mm-yyyy'")
