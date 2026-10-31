from data.indexed_container import IndexedContainer
from statistics import mean


class Series(IndexedContainer):
    """Represents a subclass of IndexedContainer with added functions."""

    def __init__(self, values, index=None):
        super().__init__(values, index=index)

    def max(self):
        """Return maximum value."""
        return max(self.values)

    def min(self):
        """Return minimum value."""
        return min(self.values)

    def sum(self):
        """Return sum of values."""
        return sum(self.values)

    def mean(self):
        """Return arithmetic mean from module statistics."""
        return mean(self.values)

    def apply(self, func):
        """Apply func to all values and returns new Series."""
        new_values = []
        for val in self.values:
            new_values.append(func(val))

        new_series = Series(new_values, self.index)
        return new_series

    def abs(self):
        """Return absolute values."""
        return self.apply(abs)
