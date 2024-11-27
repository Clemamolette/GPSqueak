# Script to initialize the database.

psql -U admin -d gpsdatabase -h localhost -p 5432 -c "CREATE TABLE IF NOT EXISTS coordinates(id SERIAL PRIMARY KEY, ip VARCHAR(50), latitude FLOAT, longitude FLOAT);"