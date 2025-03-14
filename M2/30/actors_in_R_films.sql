SELECT first_name,
       last_name
FROM sakila.actor
WHERE actor_id IN 
	(SELECT actor_id 
     FROM film_actor 
     WHERE film_id IN 
		(SELECT film_id 
         FROM film 
         WHERE rating = 'R'));