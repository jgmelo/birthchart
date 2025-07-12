# astro_calculations.py

from flatlib.chart import Chart
from flatlib.datetime import Datetime
from flatlib.geopos import GeoPos
from flatlib import const

def get_chart_data(utc_datetime, latitude, longitude):
    """Computes planetary and house data using Flatlib."""
    date_str = utc_datetime.strftime("%Y/%m/%d")
    time_str = utc_datetime.strftime("%H:%M:%S")

    pos = GeoPos(latitude, longitude)
    dt = Datetime(date_str, time_str, '+00:00')  # UTC

    chart = Chart(dt, pos, hsys=const.HOUSES_PLACIDUS)

    # Get planets
    planets_of_interest = [const.SUN, const.MOON, const.MERCURY, const.VENUS,
                           const.MARS, const.JUPITER, const.SATURN]

    planets = []
    for p in planets_of_interest:
        obj = chart.get(p)
        planets.append({
            "name": p,
            "sign": obj.sign,
            "lon": float(obj.lon),
            "house": chart.houses.getObjectHouse(obj)
        })

    # Get Ascendant
    asc = chart.get(const.ASC)

    return {
        "planets": planets,
        "ascendant": {
            "sign": asc.sign,
            "lon": float(asc.lon)
        },
        "houses": [
            {
                "number": i + 1,
                "sign": house.sign,
                "lon": float(house.lon)
            } for i, house in enumerate(chart.houses)
        ]

    }
