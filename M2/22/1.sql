USE sakila;

SELECT film_id, title, length, rating, rental_rate
FROM film
WHERE length < 90 AND rating = 'R';