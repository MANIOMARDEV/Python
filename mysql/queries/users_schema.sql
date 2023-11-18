INSERT INTO users (first_name, last_name, email)
VALUES ("Omar","mani","omarmani2016@gmail.com"),
("mohamed","lefi","mohamedlefi@gmail.com"),
("*kader","bouali","kadour@gmail.com");


SELECT * FROM users;

SELECT * FROM users
WHERE email = 'omarmani2016@gmail.com';

SELECT * FROM users
WHERE id = 3;

UPDATE users SET last_name = "Pancakes"
WHERE users.id = 3;


DELETE FROM users
WHERE users.id = 2;

SELECT * FROM users
ORDER BY first_name DESC;