from data.exceptions import InvalidDataError, IndexMismatchError
from data.index import Index


class IndexedContainer:
    """Represents a data structure with values and Index."""

    def __init__(self, values, index=None):
        """Initialize IndexedContainer with values and optional indexes."""
        if not values:
            raise InvalidDataError()

        self._values = values[:]
        self._index = None

        if index is None:
            # generates labels from 0 to length of (values - 1)
            new_labels = list(range(len(self.values)))
            self.index = Index(new_labels)
        else:
            self.index = index

    def __getitem__(self, key):
        """Return value for specific key"""
        idx = self.index.get_loc(key)
        return self.values[idx]

    def __len__(self):
        """Return number of items in the container."""
        return len(self.values)

    @property
    def values(self):
        """Return the list of values."""
        return self._values

    @property
    def index(self):
        """Return the Index object of the container."""
        return self._index

    @index.setter
    def index(self, new_index):
        """Set a new Index for the container"""
        if len(new_index) != len(self.values):
            raise IndexMismatchError()
        else:
            self._index = new_index

    def get(self, key):
        """Return value for specific key."""
        try:
            return self[key]
        except KeyError:
            return None

    def items(self):
        """Return touple (key, value)"""
        return zip(self.index, self.values)
