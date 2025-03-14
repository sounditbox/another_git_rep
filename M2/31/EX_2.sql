-- Примеры использования функций даты и времени
SELECT
rental_id,
rental_date,
return_date,
DATEDIFF(return_date, rental_date) AS rental_days, -- Количество дней проката
DATE_FORMAT(rental_date, '%W, %M %e, %Y') AS formatted_rental_date -- Форматированная дата аренды
FROM sakila.rental;
--Пример DATE_ADD/DATE_SUB
SELECT DATE_ADD(rental_date, INTERVAL 3 DAY)
FROM sakila.rental;
