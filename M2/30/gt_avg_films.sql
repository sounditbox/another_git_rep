-- Находим фильмы, продолжительность которых выше средней
SELECT title, length
FROM sakila.film
WHERE length > (SELECT AVG(length) FROM film);
