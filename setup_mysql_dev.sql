-- Print a script for prepares a MySQL server for the project.
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
-- Create User if it doesn't exist and set password
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';
-- Grant privilege on hbnb_dev_db to hbnb_dev
GRANT ALL ON hbnb_dev_db . * TO 'hbnb_dev'@'localhost';
-- Grant privilege on performance Schema to hbnb_dev
GRANT SELECT ON performance_schema . * TO 'hbnb_dev'@'localhost';
