-- workshop 18, 19
CREATE TABLE bands(
    id INTEGER PRIMARY KEY,
    name TEXT,
    debut INTEGER
);
INSERT INTO bands
VALUES(1, 'Queen', 1973), (2, 'Coldplay', 1998), (3, 'MCR', 2001);
SELECT id, name from bands;
SELECT name from bands WHERE debut < 2000;

ALTER TABLE bands ADD COLUMN members INTEGER;
UPDATE bands SET members=4 WHERE id=1;
UPDATE bands SET members=5 WHERE id=2;
UPDATE bands SET members=9 WHERE id=3;
SELECT * from bands

UPDATE bands SET members=5 WHERE id=3;

DELETE FROM bands WHERE id=2
SELECT * from bands;



-- homework 18, 19
CREATE TABLE friends(
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    location TEXT NOT NULL
);
.schema friends

INSERT INTO friends
VALUES(1, 'Justin', 'Seoul'), (2, 'Simon', 'New York'), (3, 'Chang', 'Las Vegas'), (4, 'John', 'Sydney');
SELECT * from friends;

ALTER TABLE friends ADD COLUMN married INTEGER;

.schema friends

-- 1. 기존 테이블명 변경
ALTER TABLE friends RENAME TO tmp;
-- 2. 새로운 테이블 생성
CREATE TABLE friends(
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    location VARCHR(100) NOT NULL
);
-- 3. 데이터를 이동시키고 삭제
INSERT INTO frients SELECT * FROM tmp;
-- 4. 임시 테이블 삭제
DROP TABLE tmp;

INSERT INTO friends (married) VALUES (1), (0), (0), (1);
SELECT * from friends;

UPDATE friends SET married=1 WHERE id=1;
UPDATE friends SET married=0 WHERE id=2;
UPDATE friends SET married=0 WHERE id=3;
UPDATE friends SET married=1 WHERE id=4;
SELECT * from friends;

-- id          name        debut       members
-- ----------  ----------  ----------  ----------
-- 1           Queen       1973        4
-- 2           Coldplay    1998        5
-- 3           MCR         2001        5