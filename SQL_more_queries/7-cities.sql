-- creates the database hbtn_0d_usa and the table cities (in the database hbtn_0d_usa) on your MySQL server.

CREATE DATABASE hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE TABLE cities (
    id int NOT NULL AUTO_INCREMENT UNIQUE,
    state_id int NOT NULL, FOREIGN KEY(id) REFERENCES states(id),
    name varchar(256) NOT NULL
);