SELECT
	title,
	CONCAT(title, ' (', rating, ')') AS title_and_rating, -- Объединяем название и рейтинг
	LENGTH(title) AS title_length, -- Длина названия
	LEFT(title, 5) AS title_prefix, -- Первые 5 букв названия
	LOWER(title) AS title_upper
FROM sakila.film;
