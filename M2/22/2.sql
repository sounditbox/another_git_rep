SELECT title, rating, length 
FROM sakila.film 
WHERE rating IN ('PG-13', 'R', 'G') AND
	  length BETWEEN 120 AND 180 AND
      title LIKE "%A";