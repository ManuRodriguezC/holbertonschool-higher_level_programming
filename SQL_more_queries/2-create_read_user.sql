-- creates the database hbtn_0d_2 and the user user_0d_2.

CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';
GRANT SELECT ON *.* TO 'user_0d_2'@'localhost';
CREATE user_0d_2 hbtn_0d_2 IF NOT EXISTS;