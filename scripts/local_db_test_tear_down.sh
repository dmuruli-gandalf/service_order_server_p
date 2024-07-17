
# parameters are set in the following script.
source test_db_params.sh

export PGPASSWORD=$DB_PASSWORD
psql --host="${DB_SERVER_NAME}"  --port="${DB_PORT}" --dbname="${DB_NAME}"  --username="${DB_ADMIN_NAME}" - -f work_services_drop.sql
