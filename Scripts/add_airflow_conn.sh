#(Adds/overwrites the mysql_conn Airflow connection. Replace the host with your Windows IP once you know it.)
#!/usr/bin/env bash
set -euo pipefail

CONN_ID="mysql_conn"
HOST="${1:-172.0.0.0}"   # pass your Windows IP as arg 1
LOGIN="${2:-airflow}"
PASS="${3:-pass}"     #your password
SCHEMA="${4:-hplussport}"
PORT="${5:-3306}"

airflow connections delete "$CONN_ID" >/dev/null 2>&1 || true

airflow connections add "$CONN_ID" \
  --conn-type "mysql" \
  --conn-host "$HOST" \
  --conn-login "$LOGIN" \
  --conn-password "$PASS" \
  --conn-schema "$SCHEMA" \
  --conn-port "$PORT"

echo "Airflow connection '$CONN_ID' set to mysql://$LOGIN:*****@$HOST:$PORT/$SCHEMA"
