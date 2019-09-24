CREATE TABLE classmates(
    name TEXT,
    age INTEGER,
    address TEXT
);
-- DATA 추가
INSERT INTO classmates (name, age)
VALUES('홍길동', 23);

-- 모든 열에 데이터를 추가할 때는 컬럼을 명시할 필요가 없다!
INSERT INTO classmates
VALUES('홍길동', 30, '서울');

-- 숨어있는 id 확인
SELECT rowid, * FROM classmates;


DROP TABLE classmates;

CREATE TABLE classmates (
    name TEXT NOT NULL,
    age INT NOT NULL,
    address TEXT NOT NULL
);

INSERT INTO classmates
VALUES('홍길동', 30, '서울'), ('ho', 1, '비비비');
-- 특정 column 조회
SELECT age, name FROM classmates;
-- LIMIT
SELECT rowid, name FROM classmates LIMIT 1;
-- OFFSET
SELECT rowid, name FROM classmates LIMIT 1 OFFSET 2;
-- WHERE
SELECT rowid, name FROM classmates
WHERE address='서울';
-- 특정 column 중복 제거
SELECT DISTINCT age FROM classmates;
-- 특정 id값을 제거
DELETE FROM classmates WHERE rowid=1;

-- 마지막 데이터를 삭제하고 새롭게 추가하면
-- id가 다시 활용되는 것을 볼 수 있다.
-- 이를 방지하려면, AUTOINCREMENT (django에서 id값)을 선언해서 사용해야 한다.
CREATE TABLE tests (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL
);

-- data 수정
UPDATE classmates SET address='홍홍홍' WHERE rowid=5;