from data.indexed_container import IndexedContainer
from data.series import Series
from data.exceptions import InvalidDataError, IndexMismatchError


class DataFrame(IndexedContainer):
    """Represents a data structure with Series as values and Index as indexes"""

    def __init__(self, values, index=None):
        for val in values:
            if not isinstance(val, Series):
                raise InvalidDataError()

        super().__init__(values, index=index)

    def __len__(self):
        """Return number of items in the container."""
        return len(self.index)
