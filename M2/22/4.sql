SELECT title, rating, length 
FROM film 
WHERE rating IN ('PG-13', 'R', 'G') AND
	  length BETWEEN 120 AND 180
ORDER BY length, rating, title;