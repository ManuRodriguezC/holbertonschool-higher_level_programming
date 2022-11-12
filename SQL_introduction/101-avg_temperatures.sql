-- displays the average temperature (Fahrenheit) by city ordered by temperature (descending).

sudo mysqldump -uroot -p hbtn_0c_0 < temperature.sql

SELECT city, avg(value) FROM temperatues GROUP BY city ORDER BY avg(value) DESC;