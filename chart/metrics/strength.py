from .base import Metric, register
from .rulership import RULERS
from .dignities import EXALTATION, FALL, DETRIMENT


@register
class PlanetaryStrength(Metric):
    """Assign a basic strength score based on essential dignity."""

    name = "planetary_strength"

    def compute(self, chart_data):
        strength = {}
        for planet in chart_data.get("planets", []):
            name = planet["name"]
            sign = planet["sign"]
            if sign in RULERS.get(name, set()):
                score = 5
            elif sign in EXALTATION.get(name, set()):
                score = 4
            elif sign in DETRIMENT.get(name, set()):
                score = -5
            elif sign in FALL.get(name, set()):
                score = -4
            else:
                score = 0
            strength[name] = score
        return strength
