# PL/SQL

---

> **PL/SQL (Oracle's Procedural Language extension to SQL, 절차형 SQL)**
>
> 1) 응용 프로그램에서의 데이터베이스 처리 성능을 향상시키기 위해 SQL 문장에서 **변수정의, 조건처리(IF), 반복처리(LOOP, WHILE, FOR) 등을 지원**하며, **오라클 자체에 내장되어 있는** Procedure Language
>
> 2) PL/SQL을 이용해 다양한 저장 모듈(Stored Module)을 개발 가능
>
>    - 저장 모듈 : PL/SQL 문장을 데이터베이스 서버에 저장하여 사용자와 어플리케이션 사이에서 공유할 수 있도록 만든 일종의 SQL 컴포넌트 프로그램
>
>    - Oracle의 저장 모듈에는 **프로시저(Procedure), 사용자 정의 함수(User Defined Function), 트리거(Trigger)**가 있음
>
> 3) Block 구조로 되어있어 다수의 SQL 문을 한 번에 ORACLE DB로 보내서 처리하므로 수행 속도 향상 가능 (통신량 감소, 모듈화 가능)



### PL/SQL 블록(Anonymous Block) 구조 및 특징

![PL:SQL_구조](./Photos/PL:SQL_구조.png)



|           | 사용자 정의 함수(Function)                                   | 프로시저(Procedure)                                          | 트리거(Trigger)                                        |
| :-------: | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------ |
| 생성 방법 | CREATE FUCNTION 문으로 생성                                  | CREATE PROCEDURE 문으로 생성                                 | CREATE TRIGGER 문으로 생성                             |
| 실행 방법 | 다른 프로그래밍 언어처럼 함수명()로 실행                     | EXECUTE 프로시저명() 명령을 통해 실행                        | 특정 쿼리 실행 시 DB에 의해 자동 실행                  |
|   특징    | 프로시저처럼 SQL과 로직을 묶은 명령문<br />반드시 결과값을 return 해야 됨 | BEGIN ~ END 절 내에서 COMMIT, ROLLBACK과 같은 트랜잭션 명령어(TCL) 사용이 가능 | BEGIN ~ END 절 내에서 트랜직션 명령어(TCL) 사용 불가능 |



### 프로시저(Procedure)

- 자주 실행해야하는 특정 작업을 필요할 때 호출하기 위해 절차적인 언어를 이용해 작성한 이름이 있는 프로그램 모듈(Block)



### 프로시저 문법

```sql
CREATE [OR REPLACE] PROCEDURE "PROCEDURE_NAME"(ARGUMENTS [MODE] DATA_TYPE1, ...)
IS[AS] ...
BEGIN ...
EXCEPTION ...
END;
/
```

- CREATE : 구문을 이용해 생성
- OR REPLACE : 같은 프로시저가 있을 때, 기존의 프로시저를 무시하고 새로운 내용으로 덮어쓰겠다는 의미
- MODE : 매개변수의 역할을 결정, (IN, OUT, INOUT)
  - IN : 운영체제에서 프로시저로 전달된 변수의 모드
  - OUT : 프로시저에서 처리된 결과라 운영체제로 전달
  - INOUT : IN과 OUT 두 가지 기능 모두 수행
- IS : PL/SQL의 Block을 시작한다는 의미
  - 프로시저 내에서 사용할 변수를 선언하는 곳
  - LOCAL 변수는 ISdhk BEGIN 사이에 선언
- EXCEPTION : BEGIN ~ END 사이에서 실행되는 SQL 문으로 실행 도중 발생한 에러를 처리하는 예외 처리부
- END : 실행문의 종료를 의미
- / : END; 뒤에 위치하는 슬래쉬(/)는 데이터베이스에게 프로시저를 컴파일하라는 명령



### 프로시저 예시

```sql
CREATE OR REPLACE PROCEDURE p_outTest(
	p_NAME OUT VARCHAR2
)
IS
BEGIN
	p_NAME := 'GOOD';
	DBMS_OUTPUT.PUT_LINE('호출 완료');
END;
-- 프로시저 정의
-- 만약 DECLARE로 선언되었다면 해당 변수는 일회용
--------------------------------------------------------------------------------
DECLARE OUT_MSG VARCHAR2(2000);
BEGIN p_outTest(OUT_MSG);	-- 프로시저를 실행한후에 out을 받을 변수 지정
DBMS_OUTPUT.PUT_LINE(OUT_MSG);	-- 출력
```

```
호출 완료
GOOD
```

---



# TypeHandler

- MyBatis를 사용할 때 일반적으로 Java 타입을 사용하기 때문에 알맞게 변경해줄 필요가 있음
- 이때, TypeHandler를 사용해 가장 적합한 Java 타입을 찾음
- 지원하지 않거나 비표준인 타입에 대해서 typeHandler를 만들거나 override 할 수 있음
- Override 방법
  1. Interface (org.apache.ibatis.type.TypeHandler)를 구현
  2. org.apache.ibatis.type.BaseTypeHandler를 extend 한다
- Override 했으면 JDBC 타입으로 매핑해야됨



### Example

- TypeHandler 생성

```java
@MappedJdbcTypes(JdbcType.VARCHAR)
public class ExampleTypeHandler extends BaseTypeHandler<String> {

  @Override
  public void setNonNullParameter(PreparedStatement ps, 
                                  int i,
                                  Object parameter, 
                                  JdbcType jdbcType) throws SQLException {
    // parameter를 Encrypt 한다.
    ps.setString(i, (String)encrypt(parameter));
  }

  @Override
  public String getNullableResult(ResultSet rs, 
                                  String columnIndex) throws SQLException {

    // ResultSet으로 부터 가져온 Data를 Decrypt 한다.
    return decrypt(rs.getString(columnName));
  }
  
  private String encrypt(String toEncrypt) { ... }

  private String decrypt(String toDecrypt) { ... }
}
```

- TypeHandler 적용

```xml
<!-- mybatis-config.xml -->
<typeHandlers>
  <typeHandler handler="xxx.yyy.zzz.ExampleTypeHandler"/>
</typeHandlers>
```



### 사용처

- 마스킹 : 계좌번호, 연락처, 주소, 이름 등
- Java에서 지원하지 않는 DB 타입 : Long



### Oracle SQL`s Data Type

| 데이터 유형      | 설명                                                        |
| ---------------- | ----------------------------------------------------------- |
| VARCHAR2(size)   | 가변 길이 문자 데이터                                       |
| CHAR(size)       | 고정 길이 문자 데이터                                       |
| NUMBER(p, s)     | 가변 길이 숫자 데이터                                       |
| DATE             | 날짜 및 시간 값                                             |
| LONG             | 가변 길이 **문자 데이터**(최대 2GB)                         |
| CLOB             | 문자 데이터(최대 4GB)                                       |
| RAW and LONG RAW | 원시 이진 데이터                                            |
| BLOB             | 바이너리 데이터(최대 4GB)                                   |
| BFILE            | 외부 파일에 저장된 바이너리 데이터(최대 4GB)                |
| ROWID            | 테이블에 있는 행의 고유한 주소를 나타내는 base-64 숫자 체계 |



###  Oracle - LONG Type

- **Long**은 서브쿼리를 사용해 테이블을 생성할 때 복사되지 않는다
- GROUP BY or ORDER BY 절에 포함될 수 없다
- LONG 컬럼은 Index가 될 수 없다
- Substr, Instr 등 SQL Function에서 참조될 수 없다
- 각 테이블당 하나의 LONG 열만 사용할 수 없다
- LONG에 대해 제약 조건을 정의할 수 없다
- LONG 대신 CLOB을 사용할 수 있다



### 문제가 됐던 이유

- LONG 타입 필드를 서브쿼리로 조회하면 오류가 발생함

  (PL/SQL Developer, Orange 등 DB Tool로 조회하면 괜찮지만)

- Oracle Long Type은 Java에서 지원하지 않기 때문

  ```sql
  SELECT (SELECT LONG_DATA -- LONG 타입 필드
          FROM TBL
          WHERE 1=1
          	AND COL1 = A.COL1
         )
  FROM TBL A
  ```

  ```
  ORA-00997: LONG 데이터 유형은 사용할 수 없습니다.
  ```

- Oracle function을 이용한 해결방법

  ```sql
  CREATE OR REPLACE FUNCTION FN_LONG_TO_VARCHAR (
  	P_COL1	VARCHAR2
  )
  	RETURN VARCHAR
  AS
  	DATA	 VARCHAR2 (20000);
  BEGIN
  	SELECT LONG_DATA
  	INTO DATA
  	FROM TBL
  	WHERE 1=1
  		AND COL1 = P_COL1
  	;
  	RETURN DATA;
  END;
  ```

  ```SQL
  SELECT FN_LONG_TO_VARCHAR(A.COL1)
  FROM TBL A
  ```

- TypeHandler를 이용한 해결방법

  ```java
  package com.pure.test.typehandler;
   
   
  /**
   * 이메일 암호화 Custom Type Handler
   * 
   * @author Pure
   *
   */
  public class EmailCipherTypeHandler extends AbstractCipherTypeHandler {
      
      /* (non-Javadoc)
       * @see com.pure.test.typehandler.AbstractCipherTypeHandler#isCipher()
       */
      @Override
      protected final boolean isCipher() {
          return true;
      }
  }
  
  ```
  
  