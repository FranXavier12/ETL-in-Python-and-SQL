# VS Code Python script**: SQLAlchemy engine + Pandas → load Excel to MySQL

import pandas as pd
import sqlalchemy as sa

customers = pd.read_excel("H+ Sport Customers.xlsx", sheet_name="data")  # DataFrame
customers = customers.drop_duplicates()
customers = customers.drop(columns='Zipcode')

engine = db.create_engine("mysql+pymysql://root:<PASSWORD>@localhost:3306/hplussport")
customers.to_sql("customers", con=engine, if_exists='replace', index=False)
# What to_sql does and each parameter: writes the DataFrame to the given table, replacing if it already exists, without writing the index

print("Uploaded to hplussport.customers")
