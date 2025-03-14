SELECT rental_date, return_date, NULLIF(return_date, rental_date)
FROM rental;