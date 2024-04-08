
-- Users -- 
INSERT INTO _users (user_id, karma, registration_date, name, surname, email, nickname)
			VALUES (1, 20, now(), 'Alexander', 'Slonsky', 'a.s', 'Slon');
INSERT INTO _users (user_id, karma, registration_date, name, surname, email, nickname)
			VALUES (2, 48, now(), 'Maxim', 'Sorokin', 'm.s', 'Max');			
INSERT INTO _users (user_id, karma, registration_date, name, surname, email, nickname)
			VALUES (3, 25, now(), 'Ivan', 'Petrov', 'i.p', 'Van');			
INSERT INTO _users (user_id, karma, registration_date, name, surname, email, nickname)
			VALUES (4, 14, now(), 'Kazimir', 'Petrov', 'k.p', 'Kaizer');			
INSERT INTO _users (user_id, karma, registration_date, name, surname, email, nickname)
			VALUES (5, 50, now(), 'Aleksei', 'Golovazkiy', 'a.g', 'JIEXA');			
INSERT INTO _users (user_id, karma, registration_date, name, surname, email, nickname)
			VALUES (6, 29, now(), 'Timur', 'Cherniy', 't.c', 'Mr.Black');			
INSERT INTO _users (user_id, karma, registration_date, name, surname, email, nickname)
			VALUES (7, 32, now(), 'Petr', 'Bobylev', 'p.b', 'Petya');			
INSERT INTO _users (user_id, karma, registration_date, name, surname, email, nickname)
			VALUES (8, 22, now(), 'Maxim', 'Gorbachev', 'm.g', 'SSSR');			
INSERT INTO _users (user_id, karma, registration_date, name, surname, email, nickname)
			VALUES (9, 99, now(), 'Ieschua', 'Ga-Nozri', 'jesuslovesyou', 'RapGod');	
INSERT INTO _users (user_id, karma, registration_date, name, surname, email, nickname)
			VALUES (10, 15, now(), 'Mark', 'Green', 'm.g', 'Zlen');			

-- Admins --
INSERT INTO admins (admin_id, registration_date, name, surname, email, nickname)
			VALUES (1, now(), 'Ivan', 'Ivanov', 'i.i@mail.com', 'Odmen');
INSERT INTO admins (admin_id, registration_date, name, surname, email, nickname)
			VALUES (2, now(), 'Andrey', 'Volosov', 'a.v@mail.com', 'Bread');
INSERT INTO admins (admin_id, registration_date, name, surname, email, nickname)
			VALUES (3, now(), 'Sheri', 'Richman', 's.r@mail.com', 'Kroshka');
INSERT INTO admins (admin_id, registration_date, name, surname, email, nickname)
			VALUES (4, now(), 'Koshmadu', 'Taliban', 'allahuakbar@mail.com', 'Mohamed');
INSERT INTO admins (admin_id, registration_date, name, surname, email, nickname)
			VALUES (5, now(), 'Joy', 'Grey', '50shadows@mail.com', 'Kerya');

-- Hubs --
INSERT INTO hubs (hub_id, hub_name, post_amount, creation_date, popularity)
			VALUES (1, 'GameDev', 1, now(), 20);
INSERT INTO hubs (hub_id, hub_name, post_amount, creation_date, popularity)
			VALUES (2, 'C++', 6, now(), 30);
INSERT INTO hubs (hub_id, hub_name, post_amount, creation_date, popularity)
			VALUES (3, 'Security', 1, now(), 15);
INSERT INTO hubs (hub_id, hub_name, post_amount, creation_date, popularity)
			VALUES (4, '.NET', 1, now(), 25);

-- Blogs --
INSERT INTO blogs (blog_id, blog_name, admin_id, creation_date)
			VALUES (1, 'Microsoft', 1, DATE('2014-04-15'));
INSERT INTO blogs (blog_id, blog_name, admin_id, creation_date)
			VALUES (2, 'Kesh', 2, DATE('2015-03-16'));
INSERT INTO blogs (blog_id, blog_name, admin_id, creation_date)
			VALUES (3, 'NullPointerException', 3, DATE('2015-11-19'));
INSERT INTO blogs (blog_id, blog_name, admin_id, creation_date)
			VALUES (4, 'Oracle', 4, DATE('2014-06-11'));
INSERT INTO blogs (blog_id, blog_name, admin_id, creation_date)
			VALUES (5, 'Linux', 1, DATE('2014-09-20'));
INSERT INTO blogs (blog_id, blog_name, admin_id, creation_date)
			VALUES (6, 'Arduino', 1, DATE('2014-10-25'));
INSERT INTO blogs (blog_id, blog_name, admin_id, creation_date)
			VALUES (7, 'Hardware', 2, DATE('2012-01-05'));
INSERT INTO blogs (blog_id, blog_name, admin_id, creation_date)
			VALUES (8, 'OpenGL', 3, DATE('2015-08-01'));

-- Posts --
INSERT INTO posts (post_id, post_name, hub_id, user_id, blog_id, content_link, creation_date)
			VALUES (1, 'Making Doom', 1, 1, 2, 'go.gle/12', now());
INSERT INTO posts (post_id, post_name, hub_id, user_id, blog_id, content_link, creation_date)
			VALUES (2, 'VS 16', NULL, 2, 1, 'go.gle/13', now());
INSERT INTO posts (post_id, post_name, hub_id, user_id, blog_id, content_link, creation_date)
			VALUES (3, 'New virus', NULL, 2, 2, 'go.gle/14', now());
INSERT INTO posts (post_id, post_name, hub_id, user_id, blog_id, content_link, creation_date)
			VALUES (4, 'Making DBMS', NULL, 3, 3, 'go.gle/124', now());

-- Comments --
INSERT INTO comments (comment_id, user_id, post_id, creation_date, content_link)
			VALUES (1, 1, 2, now(), 'go.gle/09');
INSERT INTO comments (comment_id, user_id, post_id, creation_date, content_link)
			VALUES (2, 2, 1, now(), 'go.gle/08');
INSERT INTO comments (comment_id, user_id, post_id, creation_date, content_link)
			VALUES (3, 3, 2, now(), 'go.gle/072');
INSERT INTO comments (comment_id, user_id, post_id, creation_date, content_link)
			VALUES (4, 1, 3, now(), 'go.gle/073');