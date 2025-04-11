ALTER TABLE products ADD COLUMN IF NOT EXISTS attributes JSONB;
-- Вставка данных
INSERT INTO products (product_name, sku, price, category_id, attributes)
VALUES ('Tablet', 'TB-789', 299.99, 1, '{"color": "gray", "screen_size": 10.1, "storage": 64}')
ON CONFLICT (product_name) DO NOTHING;

select * from products order by product_id;
-- Добавление данных в attributes
UPDATE products
SET attributes = '{"color": "silver", "screen_size": 13.3, "ram": 8}'
WHERE product_name = 'Laptop';

UPDATE products
SET attributes = '{"pages": 320, "author": "John Smith"}'
WHERE product_name = 'SQL for Beginners';
-- Извлечение значений
SELECT product_name, attributes->>'color' AS color FROM products where attributes is not null; -- ->> возвращает текст
SELECT product_name, attributes->'screen_size' AS screen_size FROM products where attributes is not null;

create index idx_products_attrs on products using gin (attributes);
-- Фильтрация
explain analyze SELECT product_name FROM products WHERE attributes @> '{"color": "silver"}'; -- @> - "содержит"



-- Добавляем столбец created_at (дата создания товара) в таблицу products
ALTER TABLE products ADD COLUMN IF NOT EXISTS created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW();
--Обновляем
UPDATE products SET created_at = '2024-01-15 10:00:00-08' WHERE product_name = 'Laptop';
UPDATE products SET created_at = '2024-02-20 14:30:00+03' WHERE product_name = 'SQL for Beginners';
UPDATE products SET created_at = '2024-02-28 08:45:00-05' WHERE product_name = 'Tablet';
--Опционально добавляем столбец last_modified
ALTER TABLE products ADD COLUMN IF NOT EXISTS updated_at TIMESTAMP WITH TIME ZONE DEFAULT NOW();

-- Форматирование даты и времени
SELECT
	product_name,
	created_at,
	TO_CHAR(created_at, 'YYYY-MM-DD') AS date_ymd, -- '2024-03-01’
	TO_CHAR(created_at, 'Month DD, YYYY') AS date_full, -- 'March 01, 2024'
	TO_CHAR(created_at, 'Day, HH24:MI:SS') AS day_and_time, -- 'Friday, 14:30:00'
	TO_CHAR(created_at, 'FMMonth DD, YYYY') AS date_formatted --Убираем лишние пробелы
FROM products;

SELECT
	product_name,
	created_at,
	EXTRACT(YEAR FROM created_at) AS year,
	EXTRACT(MONTH FROM created_at) AS month,
	EXTRACT(DAY FROM created_at) AS day,
	EXTRACT(HOUR FROM created_at) AS hour,
	EXTRACT(MINUTE FROM created_at) AS minute,
	EXTRACT(SECOND FROM created_at) AS second,
	EXTRACT(DOW FROM created_at) AS day_of_week, -- День недели (0-6, 0- воскресенье)
	EXTRACT(DOY FROM created_at) AS day_of_year -- День года
FROM products;


-- Округление даты и времени
select 
	product_name,
	created_at,
	DATE_TRUNC('day', created_at) AS created_at_day, -- До начала дня
	DATE_TRUNC('month', created_at) AS created_at_month, -- До начала месяца
	DATE_TRUNC('year', created_at) AS created_at_year -- До начала года
FROM products;

-- Подключаем расширение (если ещё не подключено)
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

-- Таблица с UUID
CREATE TABLE orders (
	order_id UUID PRIMARY KEY DEFAULT uuid_generate_v4(), -- Генерация UUID
	customer_id INT,
	order_date TIMESTAMP
);
-- Вставка данных
INSERT INTO orders (customer_id, order_date) VALUES (1, NOW());
select * from orders;