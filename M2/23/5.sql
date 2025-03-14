SELECT title,
	CASE 
		WHEN length < 60 THEN 'Короткометражный'
		WHEN length BETWEEN 60 AND 120 THEN 'Средней продолжительности'
		WHEN length > 120 THEN 'Длинный'
		ELSE 'Продолжительность неизвестна'
	END as length_category
FROM film;
