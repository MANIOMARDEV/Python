-- Add users
INSERT INTO users (first_name, last_name) VALUES
("Jane", "Amsden"), 
("Emily", "Dixon"), 
("Theodore", "Dostoevsky"), 
("William", "Shapiro"), 
("Lao", "Xiu");

-- Add books
INSERT INTO books (title, num_of_pages) VALUES
("C sharp", 500), 
("Java", 800), 
("Python", 700), 
("PHP", 850), 
("Ruby", 750);

-- Disable safe updates
SET SQL_SAFE_UPDATES = 0;

-- Update book title
UPDATE books SET title = "C#" WHERE title = "C Sharp";

-- Update user's first name
UPDATE users SET first_name = "Bill" WHERE id = 4;

-- Have the first user favorite the first 2 books
INSERT INTO favorites (user_id, book_id) VALUES
(1, 1), (1, 2);

-- Have the second user favorite the first 3 books
INSERT INTO favorites (user_id, book_id) VALUES
(2, 1), (2, 2), (2, 3);

-- Have the third user favorite the first 4 books
INSERT INTO favorites (user_id, book_id) VALUES
(3, 1), (3, 2), (3, 3), (3, 4);

-- Have the fourth user favorite all the books
-- Assuming you have a way to get the total number of books, let's say it's 5
INSERT INTO favorites (user_id, book_id) VALUES
(4, 1), (4, 2), (4, 3), (4, 4), (4, 5);

-- Show all favorites
SELECT * FROM favorites;

-- Get users who favorited book with id 3
SELECT users.first_name, users.last_name FROM users 
JOIN favorites ON users.id = favorites.user_id
JOIN books ON favorites.book_id = books.id
WHERE books.id = 3;

-- Remove a favorite (user 1, book 3)
DELETE FROM favorites WHERE user_id = 1 AND book_id = 3;

-- Add a new favorite (user 5, book 2)
INSERT INTO favorites (user_id, book_id) VALUES (5, 2);

-- Get book titles favorited by user 3
SELECT title FROM books
JOIN favorites AS faves ON faves.book_id = books.id
WHERE faves.user_id = 3;

-- Get names of users who favorited book 5
SELECT first_name, last_name FROM users
JOIN favorites ON users.id = favorites.user_id
WHERE favorites.book_id = 5;