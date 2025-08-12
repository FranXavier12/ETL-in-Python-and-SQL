#(Pulls DB creds from an Airflow connection called mysql_conn, reads the Excel from your Windows path, and writes to MySQL using a real SQLAlchemy Connection.)

import pandas as pd
import sqlalchemy as sa
from sqlalchemy.engine import URL
from airflow.hooks.base import BaseHook  # Airflow conn fetch

# Windows Excel file as seen from WSL
ORDERS_XLSX = (
    the file path where the xlsx file was saved: H+ Sport orders.xlsx i.e.: "/mnt/c/Users/...."
)

def _sqlalchemy_engine_from_conn_id(conn_id: str = "mysql_conn"):
    """Return a SQLAlchemy Engine built from an Airflow Connection."""
    af_conn = BaseHook.get_connection(conn_id)  # airflow.models.Connection (credentials only)
    url = URL.create(
        "mysql+pymysql",
        username=af_conn.login,
        password=af_conn.password,
        host=af_conn.host,
        port=af_conn.port or 3306,
        database=af_conn.schema,
    )
    return sa.create_engine(url, pool_pre_ping=True, future=True)

def main():
    # 1) Read & shape data
    orders = pd.read_excel(ORDERS_XLSX, sheet_name="data")
    orders = orders[["OrderID", "Date", "TotalDue", "Status", "CustomerID", "SalespersonID"]]

    # 2) Build Engine, open SA Connection, write
    engine = _sqlalchemy_engine_from_conn_id("mysql_conn")
    with engine.begin() as sa_conn:
        orders.to_sql("orders", con=sa_conn, if_exists="replace", index=False)

    print("ETL script executed successfully.")
