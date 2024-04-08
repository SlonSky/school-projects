-- JOINs --

SELECT _users.karma, _users.name, _users.surname, posts.post_name
FROM _users JOIN posts ON _users.user_id = posts.user_id
ORDER BY _users.karma;

SELECT _users.karma, _users.name, _users.surname, posts.post_name
FROM _users INNER JOIN posts ON _users.user_id = posts.user_id
ORDER BY _users.karma;
-- ^ do it but order by user posts amount With inner select

SELECT posts.post_name, hubs.hub_name
FROM posts LEFT JOIN hubs ON posts.hub_id = hubs.hub_id;

-- Inserted queries --

SELECT name, surname, 
	(SELECT COUNT(post_name) 
	 FROM posts 
	 WHERE _users.user_id = posts.user_id) AS 'posts amount'
FROM _users;

SELECT blog_id AS ID, blog_name, 
	(SELECT COUNT(post_id) 
	 FROM posts 
	 WHERE ID = blog_id) AS 'posts amount' 
FROM blogs 
ORDER BY (SELECT COUNT(post_id) FROM posts WHERE ID = blog_id) DESC;

SELECT name, surname 
FROM _users 
WHERE _users.user_id IN(SELECT user_id FROM comments);