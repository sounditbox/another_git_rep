SELECT title, IF(length > 120, 'Длинный', 'Короткий') AS film_length
FROM film;
