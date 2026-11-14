from data.exceptions import InvalidDataError, DuplicateKeyError


class Index:
    """Represents an index structure for labels."""

    def __init__(self, labels, name=""):
        """Initialize the Index with given labels and an optional name."""
        # LBYL
        if not labels:
            raise InvalidDataError()

        duplicate_keys = DuplicateKeyError(labels)

        if duplicate_keys.duplicates:
            raise duplicate_keys

        self._labels = labels[:]
        self.name = name

    def __iter__(self):
        """Return generator of Index labels."""
        return (label for label in self.labels)

    def __len__(self):
        """Return the number of labels in the Index."""
        return len(self.labels)

    @property
    def labels(self):
        """Return the labels list."""
        return self._labels

    def get_loc(self, key):
        """Return index (numeric position) if key exists in Index datastructure."""
        # EAFP
        try:
            return self.labels.index(key)
        except ValueError:
            raise KeyError(f"Key: {key} is not in Index")
