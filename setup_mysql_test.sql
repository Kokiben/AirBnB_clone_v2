-- Print a script for prepares a MySQL server for the project
-- Print testing db hbnb_test_db
CREATE DATABASE IF NOT EXISTS hbnb_test_db;
-- Create User if it doesn't exist and password
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';
-- Grant privilege on hbnb_test_db to hbnb_test
GRANT ALL ON hbnb_test_db . * TO 'hbnb_test'@'localhost';
-- Grant privilege on performance Schema to hbnb_test
GRANT SELECT ON performance_schema . * TO 'hbnb_test'@'localhost';
