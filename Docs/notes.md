# Notes: ETL in Python & SQL (VS Code + SQLAlchemy + MySQL) and Airflow Scheduling

This document summarizes the hands-on steps to:
1) Create a SQLAlchemy engine from VS Code and load Excel → MySQL using Pandas, and
2) Schedule the job with Airflow (WSL/Ubuntu), pulling credentials from an Airflow Connection.

## A) SQLAlchemy engine in a VS Code Python script (MySQL)

**Goal:** Load the `customers` DataFrame (from Excel) into MySQL with SQLAlchemy. :contentReference[oaicite:1]{index=1}

### Install
```bash
python -m pip install sqlalchemy pymysql pandas openpyxl
**Note:** pymysql is the driver for MySQL.