CREATE DATABASE pages;

USE pages;

CREATE TABLE pages (
	page_id INT NOT NULL AUTO_INCREMENT,
	header VARCHAR(100) NOT NULL,
	content TEXT NOT NULL,
	image_url VARCHAR(100) NOT NULL,

	PRIMARY KEY (page_id)
);


