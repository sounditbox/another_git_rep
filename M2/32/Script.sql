CREATE TABLE products (
	product_id SERIAL PRIMARY KEY, -- Первичный ключ (уникальный и NOT NULL)
	product_name VARCHAR(255) NOT NULL,
	sku VARCHAR(50) UNIQUE, -- Артикул (должен быть уникальным)
	description TEXT,
	price NUMERIC(10, 2)
);
-- Таблица categories с автоинкрементным первичным ключом (SERIAL)
CREATE TABLE categories (
	category_id SERIAL PRIMARY KEY, -- SERIAL
	category_name VARCHAR(255) NOT NULL UNIQUE
);

DROP TABLE products;
-- Добавляем FOREIGN KEY в таблицу products
CREATE TABLE products (
	product_id SERIAL PRIMARY KEY,
	product_name VARCHAR(255) NOT NULL,
	sku VARCHAR(50) UNIQUE,
	description TEXT,
	price NUMERIC(10, 2) CHECK (price > 0), -- Цена должна быть больше 0
	category_id INTEGER REFERENCES categories(category_id)
);
-- Пример с CHECK (скидка не может быть больше цены)
CREATE TABLE order_items (
	order_item_id INTEGER PRIMARY KEY,
	product_id INTEGER,
	quantity INTEGER,
	price NUMERIC(10, 2),
	discount NUMERIC(10, 2),
	CHECK (discount <= price),
	foreign key (product_id) REFERENCES products(product_id)
);

-- Используем таблицу categories, созданную ранее
-- category_id SERIAL PRIMARY KEY,
-- category_name VARCHAR(255) NOT NULL UNIQUE
-- Добавляем категории
INSERT INTO categories (category_name) VALUES ('Electronics'); -- category_id указывать не нужно!
INSERT INTO categories (category_name) VALUES ('Books');
INSERT INTO categories (category_name) VALUES ('Clothing');

-- Смотрим, что получилось
SELECT * FROM categories;


-- Добавляем товары в products (используя category_id)
INSERT INTO products (product_name, sku, price, category_id)
VALUES ('Laptop', 'LT-123', 1200.00, 1); -- category_id = 1 (Electronics)

INSERT INTO products (product_name, sku, price, category_id)
VALUES ('SQL for Beginners', 'BK-456', 29.99, 2); -- category_id = 2 (Books)

SELECT * FROM products;


-- Увеличиваем цену Laptop на 10%
UPDATE products
SET price = price * 1.10
WHERE product_name = 'Laptop';

-- Меняем категорию для товара 'SQL for Beginners' на 'Programming' (сначала добавим такую категорию)
INSERT INTO categories (category_name) VALUES ('Programming');

-- Обновление с подзапросом
UPDATE products
SET category_id = (SELECT category_id FROM categories WHERE category_name = 'Programming')
WHERE product_name = 'SQL for Beginners';


update categories c 
set category_id = 42
where category_name = 'Programming';


ALTER TABLE products ADD COLUMN IF NOT EXISTS tags TEXT[];

insert into products (product_name, sku, price, category_id)
select 'Product' || id , 'sku' || id, id, 1 from generate_series(500001, 5000000) as id;

create index idx_products_name on products using hash (product_name);
explain analyze 
select *
from products p 
where p.product_name = 'Product-1';


-- Представление, которое показывает информацию о товарах и категориях
CREATE OR REPLACE VIEW product_info AS
SELECT
	p.product_id,
	p.product_name,
	p.sku,
	p.price,
	c.category_name,
	p.tags
FROM products p
JOIN categories c ON p.category_id = c.category_id;
-- Используем представление
SELECT * FROM product_info;
SELECT * FROM product_info WHERE category_name = 'Electronics';
SELECT * FROM product_info WHERE price > 100;
SELECT product_name, attributes->>'color' AS color FROM product_info;
DROP VIEW product_info;


-- || (конкатенация)
SELECT product_name || ' (SKU: ' || sku || ')' AS product_with_sku
FROM products;

-- LIKE (с учётом регистра)
SELECT product_name FROM products WHERE product_name LIKE 'L%'; -- Начинается на 'L'
SELECT product_name FROM products WHERE product_name LIKE '%book%'; -- Содержит 'book'
SELECT product_name FROM products WHERE product_name LIKE '_a%'; -- Второй символ 'a'
-- ILIKE (без учёта регистра)
SELECT product_name FROM products WHERE product_name ILIKE 'laptop%'; -- Начинается на 'laptop'


-- Добавляем данные в tags
UPDATE products SET tags = '{"electronics", "computer"}' WHERE product_name = 'Laptop';
UPDATE products SET tags = '{"book", "programming"}' WHERE product_name = 'SQL for Beginners';
-- Выборка
SELECT product_id, product_name, tags FROM products ORDER by product_id ;
SELECT product_name, tags[1] AS first_tag FROM products ORDER by product_id ; -- Первый элемент (индексация с 1!)
-- Поиск по массиву
SELECT product_name FROM products WHERE 'computer' = ANY(tags); -- Есть ли 'computer' в массиве?
-- Длина массива
SELECT product_name, array_length(tags, 1) FROM products  ORDER by product_id ;
--Объединение
SELECT ARRAY[1,4,3] || ARRAY[3,1] AS contains;



