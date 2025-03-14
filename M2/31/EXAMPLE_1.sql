SELECT
	title,
	length,
	ABS(length - (SELECT ROUND(AVG(length)) FROM film)) AS length_difference, 
	ROUND(rental_rate) AS rounded_rental_rate, 
	MOD(length, 60) AS minutes_remainder 
FROM sakila.film;