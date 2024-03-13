-- Write a script that creates the table id_not_null on your MySQL server.
-- id_not_null description:
-- id INT with the default value 1
-- name VARCHAR(256)

CREATE TABLE IF NOT EXISTS `unique_id`(
	id INT DEFAULT 1,
	UNIQUE (ID),
	name VARCHAR(256)
);
