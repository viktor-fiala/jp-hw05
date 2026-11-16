import pytest

from data.exceptions import DuplicateKeyError, IndexMismatchError, InvalidDataError


def test_duplicate_key_error():
    with pytest.raises(DuplicateKeyError) as err:
        raise DuplicateKeyError([1, 2, 3, 2, 1])

    assert err.value.duplicates == [1, 2]


def test_duplicates_order():
    # každá duplicita jen jednou, v pořadí prvního výskytu
    assert DuplicateKeyError(["b", "a", "b", "c", "a", "b"]).duplicates == ["b", "a"]
    assert DuplicateKeyError(["x", "y"]).duplicates == []


@pytest.mark.parametrize(
    "entity",
    [IndexMismatchError, InvalidDataError, DuplicateKeyError],
)
def test_is_exception(entity):
    assert issubclass(entity, Exception)


@pytest.mark.parametrize(
    "entity",
    [IndexMismatchError, InvalidDataError, DuplicateKeyError],
)
def test_docstrings(entity):
    assert entity.__doc__ is not None
