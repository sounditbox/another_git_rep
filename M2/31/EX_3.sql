-- Преобразуем строку '2006-02-15' в дату
SELECT STR_TO_DATE('2006-02-15', '%Y-%m-%d');
-- Преобразуем строку 'February 15, 2006' в дату
SELECT STR_TO_DATE('February 15, 2006', '%M %d, %Y');
-- Преобразуем дату последнего обновления в строку в формате 'DD.MM.YYYY’
SELECT DATE_FORMAT(last_update, '%d.%m.%Y') FROM sakila.actor;
-- Преобразуем DATETIME в строку, оставив только время
SELECT DATE_FORMAT(last_update, '%H:%i:%s') FROM sakila.rental;