SELECT title, LENGTH(title) AS title_length FROM sakila.film;

SELECT title FROM sakila.film WHERE LENGTH(title) > 20;

SELECT title FROM sakila.film ORDER BY LENGTH(title);

SELECT rating, COUNT(*) AS film_count FROM sakila.film
GROUP BY rating HAVING COUNT(*) > 100;