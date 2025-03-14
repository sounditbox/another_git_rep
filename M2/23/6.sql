SELECT  rating,
		COUNT(*) as film_count,
		AVG(length) as average_length,
		MAX(rental_rate) as max_rental_rate
FROM sakila.film
GROUP BY rating;
