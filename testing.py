from data.index import Index

# idx = Index(["key 1", "key 2", "key 3", "key 4", "key 5"])

# print(idx)
import inspect
print("Index pochází ze souboru:", inspect.getfile(Index))
print("Index očekává parametry:", inspect.signature(Index.__init__))
