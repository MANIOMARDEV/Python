INSERT INTO users (first_name, last_name) values ("Jane", "Amsden"), ("Emily", "Dixon"), ("Theodore", "Dostoevsky"), ("William", "Shapiro"), ("Lao", "Xiu");
INSERT into books (title, num_of_pages) VALUES ("C sharp", 500), ("Java", 800), ("Python", 700), ("PHP", 850), ("Ruby", 750);
SET SQL_SAFE_UPDATES = 0;
UPDATE books SET title = "C#"
WHERE title = "C Sharp";
UPDATE users SET first_name = "bill"
WHERE id = 4 ;
-- Query: Have the first user favorite the first 2 books
INSERT INTO favorites (user_id, book_id)
VALUES (1, 1), (1, 2);

-- Query: Have the second user favorite the first 3 books
INSERT INTO favorites (user_id, book_id)
VALUES (2, 1), (2, 2), (2, 3);

-- Query: Have the third user favorite the first 4 books
INSERT INTO favorites (user_id, book_id)
VALUES (3, 1), (3, 2), (3, 3), (3, 4);

-- Query: Have the fourth user favorite all the books
-- Assuming you have a way to get the total number of books, let's say it's 5
INSERT INTO favorites (user_id, book_id)
VALUES (4, 1), (4, 2), (4, 3), (4, 4), (4, 5);
select * FROM favorites
SELECT users.first_name, users.last_name FROM users
JOIN favorites on users.id = user_id
JOIN books on favorites.book_id = books.id
WHERE books.id = 3;
DELETE from favorites
where book_id = 3 AND user_id = 1;
INSERT into favorites (user_id, book_id) 
VALUES (5, 2);
SELECT title from books
JOIN favorites as faves on faves.book_id = books.id
WHERE faves.user_id = 3;
SELECT first_name, last_name from users
JOIN favorites on users.id = favorites.user_id
WHERE favorites.book_id = 5;