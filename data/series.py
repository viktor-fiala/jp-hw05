import csv
import operator
from data.indexed_container import IndexedContainer
from data.index import Index
from statistics import mean


class Series(IndexedContainer):
    """Represents a subclass of IndexedContainer with added functions."""

    def __init__(self, values, index=None):
        """Initialize Series instance."""
        super().__init__(values, index=index)
        self._shape = self.shape

    def __repr__(self):
        """Return string representation of Series."""
        return "\n".join(f"{self_lab}\t{self_val}" for self_lab, self_val in zip(self.index.labels, self.values))

    def __str__(self):
        """Return string representation of Series."""
        return repr(self)

    def __iter__(self):
        """Return generator of Series's values"""
        return (value for value in self.values)

    def __add__(self, other):
        """Element-wise addition (+)."""
        return self._apply_operator(other, operator.add)

    def __sub__(self, other):
        """Element-wise substitution (-)."""
        return self._apply_operator(other, operator.sub)

    def __mul__(self, other):
        """Element-wise multiplication (*)."""
        return self._apply_operator(other, operator.mul)

    def __truediv__(self, other):
        """Element-wise true division (/)."""
        return self._apply_operator(other, operator.truediv)

    def __floordiv__(self, other):
        """Element-wise floor division (//)."""
        return self._apply_operator(other, operator.floordiv)

    def __mod__(self, other):
        """Element-wise modulo (%)."""
        return self._apply_operator(other, operator.mod)

    def __pow__(self, other):
        """Element-wise power (** or pow())."""
        return self._apply_operator(other, operator.pow)

    def __round__(self, precision=None):
        """Return rounded values of Series."""

        def round_value(val):
            return round(val, precision)

        return self.apply(round_value)

    @classmethod
    def from_csv(cls, filepath, separator=","):
        """Create a new Series from CSV file."""
        with filepath.open(mode="r", newline="", encoding="utf-8") as file:
            csv_reader = csv.reader(file, delimiter=separator)
            rows = list(csv_reader)

        new_values = rows[1]
        new_index = Index(rows[0])

        new_series = cls(new_values, new_index)
        return new_series

    @property
    def shape(self):
        """Return amount of values of the Series as a tuple."""
        val = len(self.values)
        return (val,)

    def _apply_operator(self, other, operator):
        """Apply binary operator element-wise with another Series."""
        if not isinstance(other, Series):
            return NotImplemented

        if len(self) != len(other):
            raise ValueError("Series must have the same length.")

        else:
            result = [operator(self_val, other_val)
                      for self_val, other_val in zip(self.values, other.values)]

        return Series(result, index=self.index)

    def apply(self, func):
        """Apply func to all values and returns new Series."""

        new_values = [func(val) for val in self.values]

        new_series = Series(new_values, self.index)
        return new_series

    def abs(self):
        """Return absolute values."""
        return self.apply(abs)

    def iterate_over(self):
        """Return infinite generator of Series's values"""
        while True:
            yield from self.values

    def max(self):
        """Return maximum value."""
        return max(self.values)

    def mean(self):
        """Return arithmetic mean from module statistics."""
        return mean(self.values)

    def min(self):
        """Return minimum value."""
        return min(self.values)

    def sum(self):
        """Return sum of values."""
        return sum(self.values)
