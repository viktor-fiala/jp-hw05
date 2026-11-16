from data.index import Index
from data.series import Series

users = Index(["user 1", "user 2", "user 3", "user 4"], name="names")
cash_flow = Series(['1', '1', '', '1'], index=users)

values1 = cash_flow.values


def convert_points(self):
    if self == "":
        return 0
    self = int(self)
    return self


def apply(self, func):
    """Apply func to all values and returns new Series."""

    new_values = [func(val) for val in self.values]


print(cash_flow.apply(lambda val: 0 if val == "" else int(val)).values)
# print(cash_flow.sum())
