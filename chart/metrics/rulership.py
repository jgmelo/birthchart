from .base import Metric, register

RULERS = {
    "Sun": {"Leo"},
    "Moon": {"Cancer"},
    "Mercury": {"Gemini", "Virgo"},
    "Venus": {"Taurus", "Libra"},
    "Mars": {"Aries", "Scorpio"},
    "Jupiter": {"Sagittarius", "Pisces"},
    "Saturn": {"Capricorn", "Aquarius"},
}


@register
class Rulership(Metric):
    """List planets located in the sign they rule."""

    name = "rulership"

    def compute(self, chart_data):
        results = []
        for planet in chart_data.get("planets", []):
            rulers = RULERS.get(planet["name"], set())
            if planet["sign"] in rulers:
                results.append(planet["name"])
        return results
