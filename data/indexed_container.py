from data.exceptions import InvalidDataError, IndexMismatchError
from data.index import Index


class IndexedContainer:
    """Represents a data structure with values and Index."""

    def __init__(self, values, index=None):
        """Initialize IndexedContainer with values and optional i   ndex."""
        if not values:
            raise InvalidDataError()
        self.values = values[:]

        if index is None:
            # generates labels from 0 to length of (values - 1)
            new_labels = list(range(len(self.values)))
            self.index = Index(new_labels)
        elif len(index.labels) != len(self.values):
            raise IndexMismatchError()
        else:
            self.index = index

    def get(self, key):
        """Return value for specific key."""
        try:
            idx = self.index.get_loc(key)
            return self.values[idx]
        except KeyError:
            return None

    def __len__(self):
        """Return number of items in the container."""
        return len(self.values)
