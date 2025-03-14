SELECT fa.film_id, count(*) as actors_count
FROM actor a INNER JOIN film_actor fa 
ON a.actor_id = fa.actor_id
group by fa.film_id