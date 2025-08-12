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

### SQLAlchemy-VSCode-Python-script-Airflow-WSL-MySQL-Customers-Orders-etl/
├── README.md                         # Project overview and instructions
├── .gitignore                        # Git ignore rules
├── requirements.txt                  # Python dependencies
│
├── VS Code Python Script/            # Local Python scripts for ETL & checks
│   ├── SQLAlchemy_engine_Pandas.py   # Load Excel → MySQL via SQLAlchemy & Pandas
│   ├── Check_DB_MySQL.sql            # SQL queries to validate loaded data
│   ├── Check_DB_Python.py            # Validate MySQL data from Python
│   └── Data_quality_checks_examples.sql # Example data-quality checks
│
├── dags/                             # Apache Airflow DAGs and ETL logic
│   ├── orders_dag.py                 # Airflow DAG definition for Orders ETL
│   └── orders_etl_logic2.py          # Python ETL logic for Orders table
│
├── scripts/                          # Setup & operational helper scripts
│   ├── add_airflow_conn.sh           # Add Airflow MySQL connection
│   ├── print_win_ip.sh               # Print Windows host IP (for WSL)
│   └── run_airflow_standalone.sh     # Launch Airflow in standalone mode
│
├── docs/                             # Documentation & notes
│   ├── images/                       # Screenshots / diagrams
│   └── notes.md                      # Commands, tips, and project notes
│
└── data/                             # Source datasets (sample Excel files)
    ├── H+ Sport Customers.xlsx
    └── H+ Sport orders.xlsx


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
