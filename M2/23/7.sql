SELECT rating, language_id, COUNT(*) as film_count
FROM sakila.film
GROUP BY rating, language_id;