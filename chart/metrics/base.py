class Metric:
    """Abstract base class for chart metrics."""
    name = "base"

    def compute(self, chart_data):
        raise NotImplementedError


registry = {}


def register(cls):
    """Class decorator to register metric subclasses."""
    registry[cls.name] = cls()
    return cls


def compute_all(chart_data):
    """Compute all registered metrics and return a mapping."""
    return {name: metric.compute(chart_data) for name, metric in registry.items()}
