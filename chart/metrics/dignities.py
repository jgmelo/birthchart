from .base import Metric, register

EXALTATION = {
    "Sun": {"Aries"},
    "Moon": {"Taurus"},
    "Mercury": {"Virgo"},
    "Venus": {"Pisces"},
    "Mars": {"Capricorn"},
    "Jupiter": {"Cancer"},
    "Saturn": {"Libra"},
}

FALL = {
    "Sun": {"Libra"},
    "Moon": {"Scorpio"},
    "Mercury": {"Pisces"},
    "Venus": {"Virgo"},
    "Mars": {"Cancer"},
    "Jupiter": {"Capricorn"},
    "Saturn": {"Aries"},
}

DETRIMENT = {
    "Sun": {"Aquarius"},
    "Moon": {"Capricorn"},
    "Mercury": {"Sagittarius", "Pisces"},
    "Venus": {"Aries", "Scorpio"},
    "Mars": {"Taurus", "Libra"},
    "Jupiter": {"Gemini", "Virgo"},
    "Saturn": {"Cancer", "Leo"},
}


@register
class Dignities(Metric):
    """Classify planets by essential dignities and debilities."""

    name = "dignities"

    def compute(self, chart_data):
        result = {"exaltation": [], "detriment": [], "fall": []}
        for planet in chart_data.get("planets", []):
            name = planet["name"]
            sign = planet["sign"]
            if sign in EXALTATION.get(name, set()):
                result["exaltation"].append(name)
            if sign in DETRIMENT.get(name, set()):
                result["detriment"].append(name)
            if sign in FALL.get(name, set()):
                result["fall"].append(name)
        return result
