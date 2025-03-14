DROP TABLE IF EXISTS myschema.customer;

CREATE TABLE myschema.customer (
	id INT AUTO_INCREMENT PRIMARY KEY,
	email varchar(50) UNIQUE NOT NULL,
    first_name varchar(30) NOT NULL,
    last_name varchar(30) NOT NULL,
    create_date DATETIME DEFAULT "1970-01-01 00:00:00",
    info TEXT
);
