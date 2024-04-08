DELIMITER >>

CREATE PROCEDURE userPostsAmount(IN id INT, OUT postsAmt INT)
BEGIN
	SELECT COUNT(*) INTO postsAmt FROM posts
	WHERE user_id = id;
END >>

CREATE PROCEDURE userRating(IN id INT, OUT rating INT)
BEGIN
	SELECT ROUND((karma * 3 / 7) + 2) INTO rating FROM _users 
	WHERE user_id = id;
END >>

CREATE PROCEDURE userPosts()
BEGIN
	SELECT name, surname, 
	(SELECT COUNT(post_name) FROM posts WHERE _users.user_id = posts.user_id) AS 'posts amount'
	FROM _users;

END >>

CREATE PROCEDURE formMessages()
BEGIN
	SELECT CONCAT('Dear ', name, ' ', surname, ', ', 'your rating is: ', ROUND(karma * 3/2 - 7)) AS Message FROM _users;
END >>

DELIMITER ;