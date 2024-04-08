-- 2
SELECT creation_date, admin_id, blog_id, blog_name FROM blogs;

-- 6
SELECT user_id, name, surname, karma FROM _users WHERE karma > 30;

-- 7 
SELECT user_id, registration_date, name, surname, karma FROM _users WHERE karma > 20 ORDER BY registration_date;

-- 9
SELECT comment_id, content_link FROM comments WHERE post_id in (1, 2);

-- 12
SELECT post_id, post_name, hub_id FROM posts WHERE post_name LIKE ('Making%');

-- #### --

-- a
SELECT count(*) Users FROM _users;

-- b
SELECT count(DISTINCT user_id) 'Unique comments' FROM comments;

-- d
SELECT avg(popularity) Average, min(popularity) Min, max(popularity) Max FROM hubs;
