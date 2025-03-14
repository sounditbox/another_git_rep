SELECT a.first_name, a.last_name, f.title
FROM actor a JOIN film_actor fa 
ON a.actor_id = fa.actor_id
JOIN film f ON fa.film_id = f.film_id
ORDER BY f.title
