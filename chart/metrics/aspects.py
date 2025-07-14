from .base import Metric, register

ASPECTS = {
    "conjunction": (0, 8),
    "sextile": (60, 6),
    "square": (90, 8),
    "trine": (120, 8),
    "opposition": (180, 8),
}


def angle_diff(a, b):
    diff = abs(a - b) % 360
    if diff > 180:
        diff = 360 - diff
    return diff


@register
class Aspects(Metric):
    """Compute major aspects between planets."""

    name = "aspects"

    def compute(self, chart_data):
        planets = chart_data.get("planets", [])
        results = []
        for i, p1 in enumerate(planets):
            for p2 in planets[i + 1:]:
                diff = angle_diff(p1["lon"], p2["lon"])
                for aspect, (angle, orb) in ASPECTS.items():
                    if abs(diff - angle) <= orb:
                        results.append(f"{p1['name']} {aspect} {p2['name']}")
                        break
        return results
