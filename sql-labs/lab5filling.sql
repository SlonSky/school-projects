
-- Users -- 
INSERT INTO _users (user_id, karma, registration_date, name, surname, email, nickname)
			VALUES (1, 20, now(), 'Alexander', 'Slonsky', 'a.s@mail.com', 'Slon');
INSERT INTO _users (user_id, karma, registration_date, name, surname, email, nickname)
			VALUES (2, 48, now(), 'Maxim', 'Sorokin', 'm.s@mail.com', 'Max');			
INSERT INTO _users (user_id, karma, registration_date, name, surname, email, nickname)
			VALUES (3, 25, now(), 'Ivan', 'Petrov', 'i.p@mail.com', 'Van');			
INSERT INTO _users (user_id, karma, registration_date, name, surname, email, nickname)
			VALUES (4, 14, now(), 'Kazimir', 'Petrov', 'k.p@mail.com', 'Kaizer');			

-- Admins --
INSERT INTO admins (admin_id, registration_date, name, surname, email, nickname)
			VALUES (1, now(), 'Ivan', 'Ivanov', 'i.i@mail.com', 'Odmen');

-- Hubs --
INSERT INTO hubs (hub_id, hub_name, post_amount, creation_date, popularity)
			VALUES (1, 'GameDev', 1, now(), 20);
INSERT INTO hubs (hub_id, hub_name, post_amount, creation_date, popularity)
			VALUES (2, 'C++', 6, now(), 30);
INSERT INTO hubs (hub_id, hub_name, post_amount, creation_date, popularity)
			VALUES (3, 'Security', 1, now(), 15);

-- Blogs --
INSERT INTO blogs (blog_id, blog_name, admin_id, creation_date)
			VALUES (1, 'Microsoft', 1, now());

-- Posts --
INSERT INTO posts (post_id, post_name, hub_id, user_id, blog_id, content_link, creation_date)
			VALUES (1, 'Making Doom', 1, 1, NULL, 'go.gle/12', now());
INSERT INTO posts (post_id, post_name, hub_id, user_id, blog_id, content_link, creation_date)
			VALUES (2, 'VS 16', NULL, 2, 1, 'go.gle/13', now());
INSERT INTO posts (post_id, post_name, hub_id, user_id, blog_id, content_link, creation_date)
			VALUES (3, 'New virus', NULL, 2, NULL, 'go.gle/14', now());
INSERT INTO posts (post_id, post_name, hub_id, user_id, blog_id, content_link, creation_date)
			VALUES (4, 'Making DBMS', NULL, 3, NULL, 'go.gle/124', now());

-- Comments --
INSERT INTO comments (comment_id, user_id, post_id, creation_date, content_link)
			VALUES (1, 1, 2, now(), 'go.gle/09');
INSERT INTO comments (comment_id, user_id, post_id, creation_date, content_link)
			VALUES (2, 2, 1, now(), 'go.gle/08');
INSERT INTO comments (comment_id, user_id, post_id, creation_date, content_link)
			VALUES (3, 3, 2, now(), 'go.gle/072');
INSERT INTO comments (comment_id, user_id, post_id, creation_date, content_link)
			VALUES (4, 1, 3, now(), 'go.gle/073');