CREATE DATABASE Forum;
USE Forum;

CREATE TABLE _users ( 
	user_id INT(8) NOT NULL AUTO_INCREMENT, 
	karma INT(3) NOT NULL, 
	registration_date DATE NOT NULL, 
	name VARCHAR(20) NOT NULL, 
	surname VARCHAR(20) NOT NULL, 
	email VARCHAR(20) NOT NULL, 
	nickname VARCHAR(20) NOT NULL, 
	PRIMARY KEY(user_id)
);

CREATE TABLE admins ( 
	admin_id INT(8) NOT NULL AUTO_INCREMENT, 
	registration_date DATE NOT NULL, 
	name VARCHAR(20) NOT NULL, 
	surname VARCHAR(20) NOT NULL, 
	email VARCHAR(20) NOT NULL, 
	nickname VARCHAR(20) NOT NULL, 
	PRIMARY KEY(admin_id)
);

CREATE TABLE hubs ( 
	hub_id INT(8) NOT NULL AUTO_INCREMENT, 
	hub_name VARCHAR(30) NOT NULL, 
	post_amount INT(8) NOT NULL, 
	creation_date DATE NOT NULL, 
	popularity INT(3) NOT NULL, 
	PRIMARY KEY (hub_id)
);

CREATE TABLE blogs ( 
	blog_id INT(8) NOT NULL AUTO_INCREMENT, 
	blog_name VARCHAR(30) NOT NULL, 
	admin_id INT(8) NOT NULL,
	creation_date DATE NOT NULL,
	PRIMARY KEY (blog_id),
	FOREIGN KEY (admin_id) REFERENCES admins(admin_id)
		ON UPDATE CASCADE
		ON DELETE RESTRICT	
); 

CREATE TABLE posts ( 
	post_id INT(8) NOT NULL AUTO_INCREMENT, 
	post_name VARCHAR(20) NOT NULL, 
	hub_id INT(8),
	user_id INT(8) NOT NULL,
	blog_id INT(8),
	content_link VARCHAR(30) NOT NULL, 
	creation_date DATE NOT NULL,
	PRIMARY KEY (post_id),
	FOREIGN KEY (hub_id) REFERENCES hubs(hub_id)
		ON UPDATE CASCADE
		ON DELETE SET NULL, 
	FOREIGN KEY (user_id) REFERENCES _users(user_id)
		ON UPDATE CASCADE
		ON DELETE CASCADE, 
	FOREIGN KEY (blog_id) REFERENCES blogs(blog_id)
		ON UPDATE CASCADE
		ON DELETE SET NULL	
); 

CREATE TABLE comments ( 
	comment_id INT(8) NOT NULL AUTO_INCREMENT, 
	user_id INT(8) NOT NULL,
	post_id INT(8) NOT NULL,
	creation_date DATE NOT NULL, 
	content_link VARCHAR(30) NOT NULL,
	PRIMARY KEY (comment_id),
	FOREIGN KEY (user_id) REFERENCES _users(user_id)
		ON UPDATE CASCADE
		ON DELETE RESTRICT, 
	FOREIGN KEY (post_id) REFERENCES posts(post_id)
		ON UPDATE CASCADE
		ON DELETE CASCADE	
);