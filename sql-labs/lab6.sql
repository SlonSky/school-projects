-- I --
# 1
SELECT surname, CONCAT(email, '@mail.com') AS 'e-mail' FROM _users;

# 2
SELECT surname, karma FROM _users WHERE karma > 23;

# 3
SELECT surname, ROUND(karma * 3/2 - 7) AS Rating FROM _users;

-- II --
# 1
SELECT CONCAT('Dear ', name, ' ', surname, ', ', 'your rating is: ', ROUND(karma * 3/2 - 7)) AS Message FROM _users;

-- III --
# 1
SELECT blog_name FROM blogs WHERE creation_date < DATE('2015-01-01');

# 2													   
SELECT name, 
	   surname, 
	   email 
FROM admins             -- Blogs created earlier than 2015-01-01 --
WHERE admin_id IN (SELECT admin_id FROM blogs WHERE creation_date < DATE('2015-01-01'));

# 3
SELECT admin_id AS ID, 
	   name, 
	   surname,   -- Blogs belong to current admin count -- 
	  (SELECT 
	      CASE 
	          WHEN COUNT(blog_id) = 0
	              THEN 'No blogs'
	          ELSE COUNT(blog_id)
	      END
	   FROM blogs WHERE admin_id = ID) AS 'Blogs amount'
FROM admins;
