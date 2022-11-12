-- displays the average temperature (Fahrenheit) by city ordered by temperature (descending).

SELECT city, avg(value) FROM temperatues GROUP BY city ORDER BY avg(value) DESC;