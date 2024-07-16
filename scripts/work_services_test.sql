 -- Postgres does not support the if not exists clause in create 
 -- database so instead of using the following
 
 -- CREATE DATABASE IF NOT EXISTS  work_services
 -- have to create a workaround

SELECT 'CREATE DATABASE work_services_test'
WHERE NOT EXISTS (SELECT FROM pg_database WHERE datname = 'work_services_test')\gexec
\c work_services_test

\i work_services.sql