#!/usr/bin/env bash
set -euo pipefail
export AIRFLOW_HOME="${AIRFLOW_HOME:-$HOME/airflow_home}"
mkdir -p "$AIRFLOW_HOME"
pkill -f 'airflow' || true
airflow standalone
