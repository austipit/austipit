###### lite version //

CREATE TABLE friends(
  id INTEGER, 
  name TEXT,
  birthday DATE
);

INSERT INTO friends (id, name, birthday)
VALUES (1, 'Ororo Munroe', '1940-05-30');


INSERT INTO friends (id, name, birthday)
VALUES (2, 'Mark Pitts', '1973-04-07'),
(3, 'Nina Pitts', '1972-02-01');



UPDATE friends
SET name = "Storm"
WHERE id = 1;

ALTER TABLE friends
ADD COLUMN email TEXT;

UPDATE friends
SET email = "storm@codecademy.com"
WHERE id = 1; UPDATE friends SET email = "marymark1973@gmail.com" WHERE id = 2;
UPDATE friends SET email = "ninabowie72@yahoo.com" WHERE id = 3;

DELETE FROM friends WHERE id = 1;





SELECT * FROM friends;
