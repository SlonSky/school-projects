SET AUTOCOMMIT = 0;

SELECT * FROM blogs;

START TRANSACTION;

-- Unpointed COMMIT / ROLLBACK --

INSERT INTO blogs (blog_id, blog_name, admin_id, creation_date)
			VALUES (9, 'ROLLBACK', 4, DATE('2011-04-01'));
INSERT INTO blogs (blog_id, blog_name, admin_id, creation_date)
			VALUES (10, 'WITHOUT SAVEPOINT', 3, DATE('2002-08-05'));

ROLLBACK;
SELECT * FROM blogs;

INSERT INTO blogs (blog_id, blog_name, admin_id, creation_date)
			VALUES (9, 'Hello commit', 3, DATE('2009-10-15'));
COMMIT;
SELECT * FROM blogs;

-- Pointed ROLLBACK --

INSERT INTO blogs (blog_id, blog_name, admin_id, creation_date)
			VALUES (10, 'Point blog', 2, DATE('2012-08-01'));

SAVEPOINT point1;
INSERT INTO blogs (blog_id, blog_name, admin_id, creation_date)
			VALUES (11, 'Dummy blog', 4, DATE('2012-08-01'));

SAVEPOINT point2;
INSERT INTO blogs (blog_id, blog_name, admin_id, creation_date)
			VALUES (12, 'BlogPoint2', 3, DATE('2013-08-11'));

SELECT * FROM blogs;

ROLLBACK TO SAVEPOINT point2;
SELECT * FROM blogs;

ROLLBACK TO SAVEPOINT point1;
SELECT * FROM blogs;

COMMIT;
SELECT * FROM blogs;