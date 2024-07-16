 -- Postgres does not support the if not exists clause in create 
 -- database so instead of using the following
 
 -- CREATE DATABASE IF NOT EXISTS  work_services
 -- have to create a workaround

SELECT 'CREATE DATABASE work_services'
WHERE NOT EXISTS (SELECT FROM pg_database WHERE datname = 'work_services')\gexec
\c work_services

SET client_min_messages TO WARNING;

AUTOCOMMIT = ON;

CREATE TABLE IF NOT EXISTS project(
    project_id BIGSERIAL PRIMARY KEY,
    title VARCHAR(50) NOT NULL,
    notes VARCHAR(255) NOT NULL,
    start_date DATE,
    end_date DATE,
    site_location_id BIGINT,
    created_by BIGINT,
    created_ts TIMESTAMPTZ,
    updated_by BIGINT,
    updated_ts TIMESTAMPTZ
);


CREATE TABLE IF NOT EXISTS work_order(
    work_order_id BIGSERIAL PRIMARY KEY,
    title VARCHAR(50) NOT NULL,
    notes VARCHAR(255) NOT NULL,
    start_date DATE,
    end_date DATE,
    site_location_id BIGINT,
    order_source TEXT,
    recieved_by BIGINT,
    approved_id BIGINT,
    created_by BIGINT,
    created_ts TIMESTAMPTZ,
    updated_by BIGINT,
    updated_ts TIMESTAMPTZ
);

CREATE TABLE IF NOT EXISTS task(
    task_id BIGSERIAL PRIMARY KEY,
    work_order_id BIGINT,
    title VARCHAR(50) NOT NULL,
    notes VARCHAR(255) NOT NULL,
    start_date DATE,
    end_date DATE,
    approved_id BIGINT,
    created_by BIGINT,
    created_ts TIMESTAMPTZ,
    updated_by BIGINT,
    updated_ts TIMESTAMPTZ
);
CREATE TABLE IF NOT EXISTS work_order_task(
    work_order_task_id BIGSERIAL PRIMARY KEY,
    work_order_id BIGINT,
    task_id BIGINT,
    purchase_order_id BIGINT,
    created_by BIGINT,
    created_ts TIMESTAMPTZ,
    updated_by BIGINT,
    updated_ts TIMESTAMPTZ
);

CREATE TABLE IF NOT EXISTS supply(
    supply_id BIGSERIAL PRIMARY KEY,
    order_source TEXT,
    title VARCHAR(50) NOT NULL,
    description TEXT,
    notes TEXT,
    created_by BIGINT,
    created_ts TIMESTAMPTZ,
    updated_by BIGINT,
    updated_ts TIMESTAMPTZ
);

CREATE TABLE IF NOT EXISTS task_supply(
    task_supply_id BIGSERIAL PRIMARY KEY,
    task_id BIGINT,
    supply_id BIGINT,
    purchase_order_id BIGINT,
    created_by BIGINT,
    created_ts TIMESTAMPTZ,
    updated_by BIGINT,
    updated_ts TIMESTAMPTZ
);





CREATE TABLE IF NOT EXISTS project_section(
    created_by BIGINT,
    created_ts TIMESTAMPTZ,
    updated_by BIGINT,
    updated_ts TIMESTAMPTZ
);

CREATE TABLE IF NOT EXISTS project_work_order(
    created_by BIGINT,
    created_ts TIMESTAMPTZ,
    updated_by BIGINT,
    updated_ts TIMESTAMPTZ
);

CREATE TABLE IF NOT EXISTS application_user(
    application_user_id BIGSERIAL PRIMARY KEY,
    email TEXT,
    password TEXT,
    role_id BIGINT,
    created_by BIGINT,
    created_ts TIMESTAMPTZ,
    updated_by BIGINT,
    updated_ts TIMESTAMPTZ

);
CREATE TABLE IF NOT EXISTS application_user_role(
    application_user_role BIGSERIAL PRIMARY KEY,
    role_id BIGINT,
    created_by BIGINT,
    created_ts TIMESTAMPTZ,
    updated_by BIGINT,
    updated_ts TIMESTAMPTZ
);

CREATE TABLE IF NOT EXISTS role(
    role_id BIGSERIAL PRIMARY KEY,
    role_name TEXT,
    created_by BIGINT,
    created_ts TIMESTAMPTZ,
    updated_by BIGINT,
    updated_ts TIMESTAMPTZ
);

CREATE TABLE IF NOT EXISTS customer_site();

CREATE TABLE IF NOT EXISTS customer();


CREATE TABLE IF NOT EXISTS supplies_category();



CREATE TABLE IF NOT EXISTS purchase_order();

CREATE TABLE IF NOT EXISTS customer_contact();

CREATE TABLE IF NOT EXISTS WORK_ORDER_STATUS();

CREATE TABLE IF NOT EXISTS employee (
    employee_id BIGSERIAL,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    position VARCHAR(255),
    phone VARCHAR(20),
    email TEXT,
    created_by BIGINT,
    created_ts TIMESTAMPTZ,
    updated_by BIGINT,
    updated_ts TIMESTAMPTZ
);
