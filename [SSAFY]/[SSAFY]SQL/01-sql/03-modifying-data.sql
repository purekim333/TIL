-- 공통
SELECT * FROM articles;
DROP TABLE articles;
PRAGMA table_info('articles');

-- 사전 준비
CREATE TABLE articles(
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  title VARCHAR(100) NOT NULL,
  content VARCHAR(200) NOT NULL,
  createdAt DATE NOT NULL  
);

-- 1. Insert data into table
INSERT INTO 
  articles (title, content, createdAt)
VALUES
  ('hello', 'world', '2000-01-01');
  
INSERT INTO 
  articles (title, content, createdAt)
VALUES
  ('title1', 'content1', '2000-01-01'),
  ('title2', 'content2', '2000-01-01'),
  ('title3', 'content3', '2000-01-01');

INSERT INTO 
  articles (title, content, createdAt)
VALUES
  ('mytitle', 'mycontent', DATE());
-- 2. Update data in table
UPDATE articles
SET title = 'update title'
WHERE id = 1;

UPDATE articles
SET 
  title = 'update title',
  content = 'update Content'
WHERE id = 2;

-- 3. Delete data from table
DELETE FROM articles
WHERE
  id = 3;

DELETE FROM articles
WHERE id IN(
  SELECT id FROM articles
  ORDER BY createdAt
  LIMIT 2
);

DELETE FROM articles;