
DB_SERVER_NAME=localhost
DB_PORT=5432
DB_ADMIN_NAME=service_app_admin
DB_NAME=work_services
DB_ADMIN_PASSWORD=adminPassw0rd1



export PGPASSWORD=$DB_PASSWORD
psql --host="${DB_SERVER_NAME}"  --port="${DB_PORT}" --dbname="${DB_NAME}"  --username="${DB_ADMIN_NAME}" - -f work_services_drop.sql
