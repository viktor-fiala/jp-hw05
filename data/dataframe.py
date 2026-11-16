import pathlib
import csv
from data.indexed_container import IndexedContainer
from data.series import Series
from data.index import Index
from data.exceptions import InvalidDataError


class DataFrame(IndexedContainer):
    """Represents a data structure with Series as values and Index as indexes"""

    def __init__(self, values, index=None):
        """Initialize DataFrame with Series columns and an optional index."""

        if not values or any(not isinstance(val, Series) for val in values):
            raise InvalidDataError()

        super().__init__(values, index=index)

    def __repr__(self):
        """Return string representation of DataFrame."""
        return f"{self.__class__.__name__}{self.shape}"

    def __str__(self):
        """Return string representation of DataFrame."""
        return repr(self)

    def __iter__(self):
        """Return generator of Dataframe's indexes"""
        return (idx for idx in self.index.labels)

    def __len__(self):
        """Return number of items in the container."""
        return len(self.index)

    @classmethod
    def from_csv(cls, filepath, separator=","):
        """Create a new DataFrame from CSV file."""
        with filepath.open(mode="r", newline="", encoding="utf-8") as file:
            csv_reader = csv.reader(file, delimiter=separator)
            rows = list(csv_reader)

        new_data_index = rows[0][1:]

        rows = rows[1:]
        cols = list(zip(*rows))

        first_col = list(cols[0])
        new_value_index = Index(first_col)

        new_values = [Series(list(col), index=new_value_index)
                      for col in cols[1:]]

        new_dataframe = cls(new_values, index=Index(new_data_index))
        return new_dataframe

    @property
    def shape(self):
        """Return amount of rows and columns of the DataFrame as a tuple"""
        rows = len(self.values[0])
        cols = len(self.index)
        return (rows, cols)
