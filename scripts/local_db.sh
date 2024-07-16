#!/bin/bash
# Default Variables
# Note: After install create local user db_dev
#CREATE USER service_app_admin SUPERUSER;
#CREATE DATABASE db_dev WITH OWNER db_dev;
#ALTER user service_app_admin with password 'adminPassw0rd1';

DB_SERVER_NAME=localhost
DB_PORT=5432
DB_ADMIN_NAME=service_app_admin
DB_NAME=postgres
DB_ADMIN_PASSWORD=adminPassw0rd1


# login to Azure
# az login --service-principal --username "${applicationId}" --password "${password}" --tenant "${tenantID}"
# az login --service-principal -u http://azure-cli-2016-08-05-14-31-15 -p ~/mycertfile.pem --tenant "${tenantID}"
# EXAMPLE az login --service-principal -u http://azure-cli-2016-08-05-14-31-15 -p ~/mycertfile.pem --tenant contoso.onmicrosoft.com
#psql -h mydemoserver.postgres.database.azure.com -U myadmin flexibleserverdb

# psql --host=<servername> --port=<port> --username=<user> --dbname=<dbname>

export PGPASSWORD=$DB_PASSWORD
psql --host="${DB_SERVER_NAME}"  --port="${DB_PORT}" --dbname="${DB_NAME}"  --username="${DB_ADMIN_NAME}" - -f work_services_dev.sql