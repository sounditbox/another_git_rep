INSERT INTO film values (1231, 'AAA', "description", "2024", 1, null, 1, 2, 123, 12, 'R', null, "2020-01-01 00:00:00");

SELECT f.title, a.first_name, a.last_name
FROM actor a
RIGHT JOIN film_actor fa ON a.actor_id = fa.actor_id
RIGHT JOIN film f ON fa.film_id = f.film_id;