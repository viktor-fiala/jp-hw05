import statistics
import pytest

from data.index import Index
from data.series import Series
from data.dataframe import DataFrame
from data.indexed_container import IndexedContainer


@pytest.fixture
def values_data():
    return [20000, 300000, 20000, 50000]


@pytest.fixture
def idx():
    return Index(labels=["user 1", "user 2", "user 3", "user 4"], name="names")


def test_series(values_data, idx):
    values = values_data

    salaries = Series(values=values, index=idx)

    assert salaries.values == values
    assert isinstance(salaries.values, list)
    assert salaries.index is idx
    assert isinstance(salaries, IndexedContainer)


def test_series_sum(values_data, idx):
    salaries = Series(values=values_data, index=idx)

    assert salaries.sum() == sum(values_data)


def test_series_max(values_data, idx):
    salaries = Series(values=values_data, index=idx)

    assert salaries.max() == max(values_data)


def test_series_min(values_data, idx):
    salaries = Series(values=values_data, index=idx)

    assert salaries.min() == min(values_data)


def test_series_mean(values_data, idx):
    salaries = Series(values=values_data, index=idx)

    assert salaries.mean() == statistics.mean(values_data)


def test_series_apply(values_data, idx):
    salaries = Series(values=values_data, index=idx)

    def squared(a):
        """Returns squared number"""
        return a ** 2

    result = salaries.apply(func=squared)

    assert isinstance(result, Series)
    assert salaries is not result
    assert result.values == list(map(squared, values_data))
    assert result.index.labels == idx.labels
    assert salaries.values == values_data  # původní Series beze změny


def test_series_abs(idx):
    values = [20000, -300000, 20000, -50000]

    salaries = Series(values=values, index=idx)

    result = salaries.abs()

    assert isinstance(result, Series)
    assert salaries is not result
    assert result.values == list(map(abs, values))
    assert salaries.values == [20000, -300000, 20000, -50000]


def test_series_parent_class(values_data, idx):
    salaries = Series(values=values_data, index=idx)

    assert isinstance(salaries, IndexedContainer)
    assert not isinstance(salaries, DataFrame)
    assert not isinstance(salaries, Index)


@pytest.mark.parametrize(
    "function",
    [
        Series,
        Series.sum,
        Series.max,
        Series.min,
        Series.mean,
        Series.apply,
        Series.abs,
    ],
)
def test_docstrings(function):
    assert function.__doc__ is not None
