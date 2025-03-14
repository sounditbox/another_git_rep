SELECT a.first_name, a.last_name, f.title
FROM sakila.actor a
LEFT JOIN sakila.film_actor fa ON a.actor_id = fa.actor_id
LEFT JOIN sakila.film f ON fa.film_id = f.film_id;