from data.indexed_container import IndexedContainer
from data.series import Series
from data.index import Index
from data.exceptions import InvalidDataError, IndexMismatchError


class DataFrame(IndexedContainer):
    """Represents a data structure with Series as values and Index as indexes"""

    def __init__(self, values, index=None):
        """Initialize DataFrame with Series columns and an optional index."""
        for val in values:
            if not isinstance(val, Series):
                raise InvalidDataError()

        super().__init__(values, index=index)

    def __repr__(self):
        """Return string representation of DataFrame."""
        return f"{self.__class__.__name__}{self.shape}"

    def __str__(self):
        """Return string representation of DataFrame."""
        return repr(self)

    def __len__(self):
        """Return number of items in the container."""
        return len(self.index)

    @classmethod
    def from_csv(cls, text, separator=","):
        """Create a new DataFrame from CSV formatted text."""
        text = text.splitlines()
        first_row = text[0].split(separator)
        new_data_index = []

        for n in range(1, len(first_row)):
            new_data_index.append(first_row[n])

        rows = []
        for r in range(1, len(text)):
            row = text[r].split(separator)
            rows.append(row)

        cols = list(zip(*rows))
        first_col = list(cols[0])
        new_value_index = Index(first_col)

        new_values = []
        for c in range(1, len(cols)):
            val = Series(list(cols[c]), index=new_value_index)
            new_values.append(val)

        new_dataframe = DataFrame(new_values, index=Index(new_data_index))

        return new_dataframe

    @property
    def shape(self):
        """Return amount of rows and columns of the DataFrame as a tuple"""
        rows = len(self.values[0])
        cols = len(self.index)
        return (rows, cols)
