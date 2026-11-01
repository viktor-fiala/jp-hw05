from data.series import Series

assert round(Series([1.252, 2.23231312]), 2).values == [1.25, 2.23]
assert round(Series([1.6, 2.4])).values == [2, 2]
