select a1.first_name, 
	   a1.last_name,
       a2.first_name,
       a2.last_name
from actor a1
join actor a2 ON a1.first_name = a2.first_name AND
				NOT a1.actor_id = a2.actor_id;