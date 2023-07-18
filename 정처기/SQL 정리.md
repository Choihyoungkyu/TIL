# SQL 정리

---

## DDL - CREATE, ALTER, DROP, TRUNCATE

- 데이터를 정의하는 언어
- 테이블과 같은 데이터 고조를 정의하는데 사용되는 명령어들로 특정 구조를 생성, 변경, 삭제, 이름을 바꾸는 데이터 구조와 관련된 명령어들

| 구분 | DDL 명령어 | 설명                                           |
| :--: | :--------: | ---------------------------------------------- |
| 생성 |   CREATE   | 데이터베이스 오브젝트를 생성하는 명령어        |
| 수정 |   ALTER    | 데이터베이스 오브젝트를 변경하는 명령어        |
| 삭제 |    DROP    | 데이터베이스 오브젝트를 삭제하는 명령어        |
|      |  TRUNCATE  | 데이터베이스 오브젝트의 내용을 삭제하는 명령어 |



### 생성 - CREATE

#### CREATE TABLE

```sql
CREATE TABLE 테이블명
{
	컬럼명 데이터타입 [제약조건],
	...
};
```

- CREATE TABLE의 제약조건

|     제약조건      | 설명                                                         |
| :---------------: | :----------------------------------------------------------- |
|    PRIMARY KEY    | - 테이블의 기본 키를 정의<br />- 유일하게 테이블의 각 행을 식별 |
| <br />FOREIGN KEY | - 외래 키를 정의<br />- 참조 대상을 테이블(컬럼명)로 명시<br />- 열과 참조된 테이블의 열 사이의 외래 키 관계를 적용하고 설정 |
|      UNIQUE       | - 테이블 내에서 얻은 유일한 값을 갖도록 하는 제약조건        |
|     NOT NULL      | - 해당 컬럼은 NULL 값을 포함하지 않도록 하는 제약조건        |
|       CHECK       | - 개발자가 정의하는 제약조건<br />- 참(TRUE)이어야 하는 조건을 지정 |
|      DEFAULT      | - 데이터를 INSERT 할 때 해당 컬럼의 값을 넣지 않는 경우 기본값으로 설정해주는 제약조건 |



#### CREATE VIEW

```sql
CREATE VIEW 뷰이름 AS 조회쿼리;
```

- VIEW 테이블의 SELECT 문에는 UNION이나 ORDER BY 절을 사용할 수 없다
- 컬럼명을 기술하지 않으면 SELECT 문의 컬럼명이 자동으로 사용



#### CREATE OR REPLACE VIEW 기본문법

```sql
CREATE OR REPLACE VIEW 뷰이름 AS 조회쿼리;
```

- CREATE OR REPLACE VIEW는 뷰를 교체하는 명령
- OR REPLACE라는 키워드를 추가하는 것을 제외하고는 CREATE VIEW와 사용 방법이 동일



#### CREATE INDEX

```sql
CREATE [UNIQUE] INDEX 인덱스명 ON 테이블명(컬럼명1, 컬럼명2, ...);
```

- 인덱스를 생성하는 명령
- UNIQUE는 생략 가능
- 인덱스 걸린 컬럼에 중복 값을 허용하지 않음
- 복수 컬럼을 인덱스로 걸 수 있음



### 수정 - ALTER

#### ALTER TABLE 컬럼 추가

```sql
ALTER TABLE 테이블명 ADD 컬럼명 데이터타입 [제약조건];
```

- 테이블에 필요한 컬럼을 추가하는 문법
- CREATE TABLE의 컬럼에 사용되는 제약조건들은 ALTER TABLE에서도 사용 가능



#### ALTER TABLE 컬럼 수정

```sql
ALTER TABLE 테이블명 MODIFY 컬럼명 데이터타입 [제약조건];
```

- 테이블에 필요한 컬럼을 수정하는 문법
- 테이블 생성을 위한 CREATE 문에 제약조건을 명시 후에 ALTER를 통해 테이블 제약조건의 변경이 가능



#### ALTER TABLE 컬럼 삭제

```sql
ALTER TABLE 테이블명 DROP 컬럼명;
```

- 테이블에 불필요한 컬럼을 삭제하는 문법



#### ALTER INDEX

```sql
ALTER [UNIQUE] INDEX 인덱스명 ON 테이블명(컬럼명1, 컬럼명2, ...);
```



### 삭제 - DROP, TRUNCATE

#### DROP TABLE

```sql
DROP TABLE 테이블명 [CASCADE | RESTRICT];
```

- DROP TABLE은 테이블을 삭제하는 명령
- 옵션으로 CASCADE와 RESTRICT가 있음
  - CASCADE : 참조하는 테이블까지 연쇄적으로 제거하는 옵션
  - RESTRICT : 다른 테이블이 삭제할 테이블을 참조 중이면 제거하지 않는 옵션
  - CASCADE와 RESTRICT의 경우 외래 키(FOREIGN KEY)가 걸려 있을 때 해당



#### TRUNCATE TABLE

```sql
TRUNCATE TABLE 테이블명;
```

- TRUNCATE TABLE은 테이블 내의 데이터들을 삭제하는 명령



#### DROP VIEW

```sql
DROP VIEW 뷰이름;
```



#### DROP INDEX

```sql
DROP INDEX 인덱스명;
```

---

## DML - SELECT, INSERT, UPDATE, DELETE

### SELECT

```sql
SELECT * FROM 테이블명
```

- 데이터 조회할 때 사용



### INSERT

```sql
INSERT INTO 테이블명(컬럼1, 컬럼2, 컬럼3, ...) VALUES(컬럼1의 값, 컬럼2의 값, ...);
```

```sql
# 예시
INSERT INTO EMP(EMPNO, ENAME, JOB) VALUES(9999, 'BILL', 'CEO');
```

- 데이터를 입력할 때 사용
- 입력하지 않은 값은 자동으로 NULL 값 입력



### UPDATE

```sql
UPDATE 테이블명 SET 변경할 컬럼1 = 변경할 데이터1, 변경할 컬럼2 = 변경할 데이터2, ... WHERE 컬럼=조건데이터;
```

```sql
# 예시
UPDATE EMP SET JOB='INTERN', SAL=2000 WHERE ENAME='BILL';
```

- 입력되어 있는 데이터 내용 중 변경이 필요한 부분 수정



### DELETE

```sql
DELETE FROM 테이블명 WHERE 삭제할 컬럼명=조건;
```

```sql
# 예시
DELETE FROM EMP WHERE EMPNO='9999';
```

- 데이터 삭제 시 사용

---

## DCL - GRANT, REVOKE, COMMIT, ROLLBACK

- 데이터의 보완, 무결성, 데이터 회복, 병행수행, 제어 등을 정의하는데 사용하는 언어



### GRANT TO

```sql
# 권한부여
GRANT [권한] ON 테이블명 TO 사용자명;

# 사용자 등록 및 권한부여
GRANT [권한] ON 테이블명 TO 사용자명 IDENTIFIED BY '비밀번호';

# 권한 확인
SHOW GRANTS FOR [유저_ID]@[호스트];
```

```sql
# 예시
GRANT SELECT, INSERT, UPDATE ON 테이블명 TO 사용자명;

GRANT ALL PRIVILEGES ON 테이블명 TO 사용자명;
```

- 데이터베이스 사용자에게 권한(제어 가능한 권한 참조)을 부여하는 명령



### REVOKE FROM

```sql
REVOKE [권한] ON 테이블명 FROM 사용자명;
```

- 데이터베이스 사용자로부터 권한을 제거하는 명령



### COMMIT

```sql
COMMIT;
```

- 데이터베이스의 작업한 결과를 물리적 디스크로 저장하고, 작업을 정상적으로 완료시키는 명령



### ROLLBACK

```sql
ROLLBACK;
```

- 데이터베이스의 트랜잭션 작업이 비정상적으로 종료되었을 때 원래의 상태로 복구하는 명령
- COMMIT 명령어를 사용하기 이전의 상태로만 ROLLBACK 가능

