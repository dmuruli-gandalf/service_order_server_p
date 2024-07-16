# Variables
DB_NAME="service_order_db"
DB_USER="doadmin"
DB_PASSWORD="AVNS_G5aVksNK_ktIY5BGOKi"
DB_HOST="db-postgresql-nyc3-89951-do-user-16569667-0.c.db.ondigitalocean.com"
DB_PORT="25060"
SSL_MODE="require"  # Other options include "disable", "allow", "prefer", "require", "verify-ca", "verify-full"
SSL_ROOT_CERT="/certs/ca-certificate.crt"  # Path to the root certificate

# Export the password to avoid being prompted
export PGPASSWORD=$DB_PASSWORD

echo "Start of service database script"

# Connect to PostgreSQL and create the database
#sslmode=$SSL_MODE sslrootcert=$SSL_ROOT_CERT  psql -h $DB_HOST -U $DB_USER -p $DB_PORT -c "CREATE DATABASE $DB_NAME;"

#Create database with ssl
# Create the database
echo "Creating database '$DB_NAME'..."
psql "sslmode=$SSL_MODE sslrootcert=$SSL_ROOT_CERT host=$DB_HOST user=$DB_USER port=$DB_PORT -c "CREATE DATABASE $DB_NAME;"



#createdb -h $DB_HOST -p $DB_PORT -U $DB_USER testdb

# Check if the database was created successfully
