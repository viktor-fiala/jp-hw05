from data.dataframe import DataFrame
from data.index import Index
from data.series import Series

users = Index(["user 1", "user 2", "user 3", "user 4"], name="names")

salaries = Series([20000, 300000, 20000, 50000], index=users)
names = Series(["Lukas Novak", "Petr Pavel",
               "Pavel Petr", "Ludek Skocil"], index=users)
cash_flow = Series([-100, 10000, -2000, 1100], index=users)

data = DataFrame([names, salaries, cash_flow],
                 index=Index(["names", "salary", "cash flow"]))

assert [key for key in data] == ["names", "salary", "cash flow"]
assert data["salary"] is salaries

assert list(data.items()) == list(
    zip(["names", "salary", "cash flow"], [names, salaries, cash_flow]))
