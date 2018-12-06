import pandas as pd

from datetime import datetime


def date_converter(row):
    return (datetime.strptime(row["Дата заезда"], "%Y-%m-%d") - datetime.strptime(row["Дата создания"], "%Y-%m-%d")).days


def extract_season(row):
    month = datetime.strptime(row["Дата создания"], "%Y-%m-%d").month
    if month in (12, 1, 2,):
        return 1
    elif month in (3, 4, 5):
        return 2
    elif month in (6, 7, 8):
        return 3
    elif month in (9, 10, 11):
        return 4
    else:
        raise ValueError


data = pd.read_csv("bookings_example.csv")

data["До заезда"] = data.apply(lambda row: date_converter(row), axis=1)
data["Сезон"] = data.apply(lambda row: extract_season(row), axis=1)

data = data[["Стоимость тарифа", "Глубина бронирования", "До заезда", "Сезон"]]
