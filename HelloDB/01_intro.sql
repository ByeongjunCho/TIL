-- 데이터베이스 생성 $ sqlite3 db.sqlite3
.databases
-- CSV 파일로 테이블 생성
.mode csv
.import hellodb.csv examples
-- 테이블 조회
SELECT * FROM examples;
-- 깔끔하게 보기
.headers ON
.mode column
-- 스키마 조회
.schema examples