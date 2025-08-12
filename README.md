# ETL in Python and SQL
# Airflow + WSL + MySQL: Orders ETL (Pandas → SQLAlchemy → Airflow)

[![Python](https://img.shields.io/badge/Python-3.x-blue)](https://www.python.org/)
[![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-ORM-red)](https://www.sqlalchemy.org/)
[![MySQL](https://img.shields.io/badge/MySQL-Database-orange)](https://www.mysql.com/)
[![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-green)](https://pandas.pydata.org/)
[![Apache Airflow](https://img.shields.io/badge/Apache%20Airflow-Workflow%20Orchestration-blueviolet)](https://airflow.apache.org/)
[![WSL](https://img.shields.io/badge/WSL-Ubuntu-lightgrey)](https://learn.microsoft.com/en-us/windows/wsl/)
[![ETL](https://img.shields.io/badge/ETL-Process-brightgreen)](#)
[![Data Engineering](https://img.shields.io/badge/Data%20Engineering-Pipeline-yellow)](#)

---

**Description:**  
End-to-end ETL pipeline in **Python & SQL** — Load Excel data into **MySQL** using **SQLAlchemy** and **Pandas**, then schedule automated Orders ETL workflows using **Apache Airflow** running in **WSL/Ubuntu**.

---

## Repository Structure

```text
SQLAlchemy-VSCode-Python-script-Airflow-WSL-MySQL-Customers-Orders-etl/
├── README.md
├── .gitignore
├── requirements.txt
│
├── VS Code Python Script/
│   ├── SQLAlchemy_engine_Pandas.py        # Load Excel → MySQL via SQLAlchemy & Pandas
│   ├── Check_DB_MySQL.sql                 # MySQL queries to validate data
│   ├── Check_DB_Python.py                 # Validate MySQL data from Python
│   └── Data_quality_checks_examples.sql   # Example quality checks
│
├── dags/
│   ├── orders_dag.py                      # Airflow DAG definition
│   └── orders_etl_logic2.py               # ETL logic for Orders table
│
├── scripts/
│   ├── add_airflow_conn.sh                # Add Airflow connection
│   ├── print_win_ip.sh                    # Print Windows host IP (WSL)
│   └── run_airflow_standalone.sh          # Start Airflow standalone
│
├── docs/
│   ├── images/                            # Screenshots
│   └── notes.md                           # Notes / commands
│
└── data/
    ├── H+ Sport Customers.xlsx
    └── H+ Sport orders.xlsx
```


---

## A minimal, reproducible project that:

1. **Create a SQLAlchemy engine in VS Code & load Excel → MySQL**
   - Reads an **Excel** file with **Pandas** in VS Code.
   - Connects to **MySQL** using **SQLAlchemy**.
   - Loads data into MySQL tables using `pandas.DataFrame.to_sql()`.

2. **ETL in Python & SQL (VS Code + SQLAlchemy + MySQL) and Airflow Scheduling**
   - Reads **Excel** with **Pandas**.
   - Writes to **MySQL** via **SQLAlchemy**.
   - Schedules the job with **Apache Airflow** running in **WSL2/Ubuntu**.
   - Loads credentials from an **Airflow Connection** (`mysql_conn`).

> This repo captures the end-to-end flow we used in practice (with the gotchas fixed).

---

## Prereqs

- Windows 10/11 with **WSL2** + **Ubuntu** installed  
  ```powershell
  wsl --install -d Ubuntu
- MySQL Server on Windows (e.g., MySQL 8) and MySQL Workbench
- VS Code with Remote - WSL extension
- Python 3 (Ubuntu) with venv
- If MySQL runs on Windows, WSL clients must connect to the Windows host IP, not localhost.
