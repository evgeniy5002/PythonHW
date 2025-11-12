import requests
import datetime


class NbuRate:
    def __init__(self, j: dict):
        """{'r030': 12, 'txt': 'Алжирський динар', 'rate': 0.32171, 'cc': 'DZD', 'exchangedate': '10.11.2025'}"""
        self.r030 = j["r030"]
        self.name = j["txt"]
        self.rate = j["rate"]
        self.abbr = j["cc"]
        self.date = j["exchangedate"]

    def __str__(self):
        return "%s (%s) %f" % (self.abbr, self.name, self.rate)


class NbuRatesData:
    __url = "https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?json"

    def __init__(self, url=None):
        request = requests.get(url or self.__url)
        response = request.json()
        self.exchange_date = response[0]["exchangedate"]
        self.rates = [NbuRate(r) for r in response]
        pass


def main():
    date = input_date()
    url = f"https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?date={date}&json"

    rates_data = NbuRatesData(url)
    rates_data.rates.sort(key=lambda x: x.abbr)

    print(rates_data.exchange_date, *rates_data.rates, sep="\n")


def input_date() -> str:
    months_days = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}

    while True:
        date = input("Input date [yyyymmdd]: ")

        if len(date) != 8 or not date.isdigit():
            print("Invalid format")
            continue

        year = int(date[:4])
        month = int(date[4:6])
        day = int(date[6:8])

        if year < 1996 or year > 2025:
            print("Invalid year")
            continue

        if month not in months_days.keys():
            print("Invalid month")
            continue

        if month == 2 and (year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)):
            days = 29
        else:
            days = months_days[month]

        if day < 1 or day > days:
            print("Invalid day")
            continue

        entered_date = datetime.date(year, month, day)
        if entered_date > datetime.date.today():
            print("Date must be in the past")
            continue

        return date


if __name__ == "__main__":
    main()
