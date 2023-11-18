INSERT INTO users (first_name, last_name)
VALUES ("Amy","giver"),("Eli","buyers"),("dane","Reys"),("pole","Rezdz"),("poald","toyy"),("sadsl","faderosa");
INSERT INTO users_has_users (user_id,friend_id)
VALUES (1,2),(1,4),(1,6),(2,1),(2,3),(2,5),(3,2),(3,5),(4,3),(5,1),(5,6),(6,2),(6,3);
SELECT users.first_name, users.last_name, users2.first_name as friend_first_name, users2.last_name as friend_last_name FROM users
JOIN users_has_users ON users.id = users_has_users.user_id
LEFT JOIN users as users2 ON users2.id = users_has_users.friend_id;
SELECT users2.first_name as first_name, users2.last_name as last_name, users.first_name as friends_with FROM users
JOIN users_has_users ON users.id = users_has_users.user_id
LEFT JOIN users as users2 ON users2.id = users_has_users.friend_id
WHERE users.id = 1;
SELECT COUNT(*) as users_has_users from users_has_users;

SELECT user_id, users.first_name, users.last_name, count(user_id) as num_of_friends from users_has_users
JOIN users ON users.id = users_has_users.user_id
GROUP BY user_id
ORDER BY num_of_friends DESC
LIMIT 1;

SELECT users2.first_name as first_name, users2.last_name as last_name, users.first_name as friends_with FROM users
JOIN users_has_users ON users.id = users_has_users.user_id
LEFT JOIN users as users2 ON users2.id = users_has_users.friend_id
WHERE users.id = 3
ORDER BY first_name;
