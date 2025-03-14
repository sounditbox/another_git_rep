-- Находим фильмы, продолжительность которых выше средней по их рейтингу и языку
WITH rating_language_avg_length AS (
	SELECT rating, AVG(length) AS avg_length
	FROM sakila.film
	GROUP BY rating
	)

SELECT f.title, f.rating, f.length
FROM sakila.film f
JOIN rating_language_avg_length rlal ON f.rating = rlal.rating
	AND f.length > rlal.avg_length
ORDER BY rating, length
