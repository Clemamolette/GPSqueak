# Gotta Pursue the Squeak
Clementine Galloy, Noe Faucher & Mael Triquet

![logo](rsc/logo_gpsqueak.png)


## Architecture

![architecture](rsc/schéma%20structure%20projet%20GPS.jpg)


## PostgreSQL required package
Run the following to be able to iteract with the database:

sudo apt install postgresql postgresql-contrib
sudo -i -u postgres
psql
CREATE DATABASE gpsdatabase;
CREATE USER admin WITH PASSWORD 'admin';
GRANT ALL PRIVILEGES ON DATABASE gpsdatabase TO admin;
