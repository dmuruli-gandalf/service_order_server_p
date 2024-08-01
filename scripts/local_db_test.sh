# parameters are set in the following script.
source test_db_params.sh


# login to Azure
# az login --service-principal --username "${applicationId}" --password "${password}" --tenant "${tenantID}"
# az login --service-principal -u http://azure-cli-2016-08-05-14-31-15 -p ~/mycertfile.pem --tenant "${tenantID}"
# EXAMPLE az login --service-principal -u http://azure-cli-2016-08-05-14-31-15 -p ~/mycertfile.pem --tenant contoso.onmicrosoft.com
#psql -h mydemoserver.postgres.database.azure.com -U myadmin flexibleserverdb

# psql --host=<servername> --port=<port> --username=<user> --dbname=<dbname>

export PGPASSWORD=$DB_PASSWORD
psql --host="${DB_SERVER_NAME}"  --port="${DB_PORT}" --dbname="${DB_NAME}"  --username="${DB_ADMIN_NAME}" - -f work_services_test.sql

psql --host="${DB_SERVER_NAME}"  --port="${DB_PORT}" --dbname="${DB_NAME}"  --username="${DB_ADMIN_NAME}" -c "\copy work_order FROM 'data/work_order_test.csv' WITH (FORMAT CSV,DELIMITER ',' ,HEADER MATCH)"