.mode csv
.import users.csv users

-- 1. 나이가 30 이상인 사람
SELECT * FROM users WHERE age >= 30;

-- 2. 나이가 30이상인 사람의 이름
SELECT first_name FROM users WHERE age >= 30;

-- 3. 나이가 30이상, 성이 김인 사람
SELECT * FROM users WHERE age >= 30 AND last_name=='김';

-- 4. 나이가 30이상, 김씨 인원수
SELECT COUNT(*) FROM users WHERE age >= 30 AND last_name=='김';

-- 5. 전체 데이터 갯수
SELECT count(*) FROM users

-- 6. 전체 평균 나이
SELECT AVG(age) FROM users;

-- 7. 30 이상 평균 나이
SELECT AVG(age) FROM users WHERE age >= 30;

-- 8. balance가 가장 높은 사람 이름과 액수
SELECT first_name, MAX(balance) FROM users;

-- 9. 30이상 사람의 계좌 평균
SELECT AVG(balance) FROM users WHERE age >= 30;

-- wild cards    
-- '-': 반드시 이 자리에 한 개 이상의 문자가 존재해야 한다.
-- '%': 이 자리에 문자열이 있어도 되고 없어도 된다.

-- 10. 20대인 사람
SELECT COUNT(*) FROM users WHERE age LIKE '2_';

-- 11. 지역번호가 02인 사람(서울)
SELECT COUNT(*) FROM users WHERE phone LIKE '02-%';

-- 12. 이름이 '준'으로 끝나는 사람
SELECT * FROM users WHERE first_name LIKE '%준';

-- 13. 중간번호가 5114인 사람
SELECT * FROM users WHERE phone LIKE '%-5114-%';

-- 정렬 SELECT columns FROM TABLE ORDER BY column1, column2 ... ASC|DESC;  ASC: 오름차순(default), DESC: 내림차순
-- 14. 나이 많은 사람 10명
SELECT first_name, last_name, age FROM users ORDER BY age, last_name DESC LIMIT 10;

-- 15. 나이, 성 순으로 오름차순 10명
SELECT first_name, last_name, age FROM users ORDER BY age, last_name ASC LIMIT 10;

-- 16.
SELECT first_name, last_name, age FROM users ORDER BY age, last_name ASC LIMIT 1 OFFSET 9;


CREATE TABLE articles (title TEXT NOT NULL, content TEXT NOT NULL);
INSERT INTO articles VALUES ('111', '111');
-- 특정 테이블 이름 변경
ALTER TABLE articles RENAME TO news;
-- 특정 테이블에 새로운 column attribute 추가
ALTER TABLE news ADD COLUMN created_at DTAETIME NOT NULL DEFAULT 1;  -- NOT NULL 조건을 없에거나 default 지정을 해야 생성됨
