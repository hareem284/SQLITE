# importing SQLTE3
import _sqlite3
# importing pandas
import pandas as pd
CONECT=_sqlite3.connect('database.sqlite')
print("connection is established")
TABLES=pd.read_sql("SELECT * FROM sqlite_master WHERE type='table';",CONECT)
print(TABLES)
