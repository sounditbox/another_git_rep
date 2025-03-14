SELECT a1.first_name as name1, 
	   a1.last_name as surname1,
       a2.first_name as name2,
       a2.last_name as surname2,
       fa1.film_id
FROM actor a1 
JOIN film_actor fa1 ON a1.actor_id = fa1.actor_id
JOIN film_actor fa2 ON fa1.film_id = fa2.film_id
JOIN actor a2 ON a2.actor_id = fa2.actor_id
WHERE a1.actor_id != a2.actor_id
ORDER BY fa1.film_id

