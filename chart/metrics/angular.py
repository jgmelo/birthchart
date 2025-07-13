from .base import Metric, register


@register
class AngularHouses(Metric):
    """List planets located in angular houses (1, 4, 7, 10)."""

    name = "angular_houses"

    def compute(self, chart_data):
        angular_nums = {1, 4, 7, 10}
        planets = chart_data.get("planets", [])
        return [p["name"] for p in planets if p.get("house") in angular_nums]
