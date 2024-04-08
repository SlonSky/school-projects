DELIMITER >>

-- increments hub posts amount when adding new post
CREATE TRIGGER hub_posts_amt_inc AFTER INSERT ON posts
FOR EACH ROW
BEGIN
UPDATE hubs 
SET post_amount = post_amount + 1
WHERE hub_id = NEW.hub_id;
END >> 

-- guarentees unique blog name
CREATE TRIGGER blog_name_limiter BEFORE INSERT ON blogs
FOR EACH ROW
BEGIN
IF (SELECT blog_id FROM blogs WHERE blog_name = NEW.blog_name) <> NULL 
	THEN SIGNAL SQLSTATE '20001' SET MESSAGE_TEXT = 'Blog with current name exists';
END IF;
END >>

DELIMITER ;

