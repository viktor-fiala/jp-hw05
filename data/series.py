from data.indexed_container import IndexedContainer
from data.index import Index
from statistics import mean
import operator


class Series(IndexedContainer):
    """Represents a subclass of IndexedContainer with added functions."""

    def __init__(self, values, index=None):
        """Initialize Series instance."""
        super().__init__(values, index=index)
        self._shape = self.shape

    def __repr__(self):
        """Return string representation of Series."""
        result = ""
        for i in range(0, len(self.index.labels)):
            if i < len(self.index.labels) - 1:
                result += f"{self.index.labels[i]}\t{self.values[i]}\n"
            else:
                result += f"{self.index.labels[i]}\t{self.values[i]}"
        return result

    def __str__(self):
        """Return string representation of Series."""
        return repr(self)

    def _apply_operator(self, other, operator):
        """Apply binary operator element-wise with another Series."""
        if not isinstance(other, Series):
            return NotImplemented

        if len(self) != len(other):
            raise ValueError("Series must have the same length.")

        else:
            result = []
            for i in range(len(self)):
                result.append(operator(self.values[i], other.values[i]))

        return Series(result, index=self.index)

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
    def from_csv(cls, text, separator=","):
        """Create a new Series from CSV formatted text."""
        text = text.splitlines()
        new_values = text[1].split(separator)
        new_index = Index(text[0].split(separator))
        new_series = Series(new_values, new_index)

        return new_series

    @property
    def shape(self):
        """Return amount of values of the Series as a tuple."""
        val = len(self.values)
        return (val,)

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
