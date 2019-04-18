# QuantStrategy
A package developed for Quantitative Strategy base on Tushare open-source api 


# Setup the database first
PostgreSQL is adopted as database management system:

##### create database user $yourname as super user, and set the password
sudo -u postgres createuser --superuser yourname
sudo -u postgres psql
\password yourname
\q

##### create a database $stockdata with $yourname as owner
sudo -u postgres createdb -O yourname stockdata 

