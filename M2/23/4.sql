SELECT title,
	CASE rating
		WHEN 'G' THEN 'Для всех возрастов'
		WHEN 'PG' THEN 'Рекомендуется присутствие родителей'
		WHEN 'PG-13' THEN 'Детям до 13 лет просмотр не желателен'
		WHEN 'R' THEN 'Лицам до 17 лет обязательно присутствие взрослого'
		WHEN 'NC-17' THEN 'Лицам до 18 лет просмотр запрещён'
		ELSE 'Рейтинг не определён'
	END as rating_description
FROM film;
