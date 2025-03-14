SELECT title, 
	   IFNULL(original_language_id, 1) AS original_language
FROM film;
