# SQL 튜닝

---

### 용어 정리

> **데이터베이스** : 데이터들의 집합체
>
> **DBMS(Database Management System)** : 데이터베이스를 관리하는 시스템 (Oracle, DB2, MS SQL Server 등)
>
> **SQL(Structured Query Language)** : 데이터베이스를 관리하는 언어(데이터베이스 생성 및 데이터 입력, 변경, 삭제, 조회 등)



### SQL 튜닝

- 최소한의 CPU, I/O, Memory를 사용하여 최대한 빠른 시간 내에 원하는 데이터 작업을 수행하도록 만드는 것
- 튜닝시 주의할 점들
  1. 분석 및 설계 단계
     - 사용자의 데이터 처리 및 조회 패턴을 감안한 업무 요건 분석 - ex) 검색 가능성이 높은 컬럼을 인덱스로 지정
     - 중요 업무 화면의 SQL 성능 최적화를 고려한 화면 설계 - ex) 필수 입력값을 제시하거나 기간을 정해 속도를 줄임
     - 업무 성격에 따른 최적화된 데이터 모델링 - ex) 실시간 화면인지 집계 화면인지에 따라 중요도를 다르게 설계
  2. 개발 및 구현 단계
     - 개발 환경과 운영 환경의 설정 맞추기
     - 개발 환경과 운영 환경의 데이터 양 및 구성의 차이 - ex) 운영과 개발의 적재된 데이터 용량이 다르므로 주의



### SQL 튜닝 순서

1. 튜닝 대상 SQL 수집
   - 각종 테스트 수행 시 느린 SQL
   - 메모리 영역에 보존되어 있는 느린 SQL
   - 개발팀 및 업무팀이 느리다고 판단하여 튜닝을 요청한 SQL
   - 실시간 모니터링 결과 느린 SQL
2. SQL 문제점 분석 및 개선 사항 도출
   - 대상 SQL의 실행 계획 분석
   - 각종 TRACE 파일을 활용한 분석
   - 인덱스 생성 및 변경, SQL 수정, 힌트 추가 및 변경 등의 개선안 도출
3. 개선 사항 적용 및 개선 효과 확인
   - 해당 SQL의 담당자에게 개선 사항 전달
   - 개선 사항 적용 가능 여부 확인
   - 적용에 따른 개선 효과 확인



### SQL 튜닝 유형(책 목차)

1. SQL 튜닝 개요
2. 옵티마이저
3. 실행 계획
4. 인덱스
5. 조인
6. 힌트



### SQL 문제 유형

- 인덱스 : 52%
- 조인 : 20%
- 기타 : 11%
- 업무요건 : 9%
- SQL 구문 오류 : 6%
- OBJECT 관리 미흡 : 1%
- AP 로직 : 1%

---

## SQL 힌트

> 힌트를 사용하면 옵티마이저의 모드, 사용할 인덱스, 조인 방식, 스캔 방식까지 제어가 가능
>
> 옵티마이저의 한계를 사람의 판단으로 조율할 수 있게 해주는 도구로 생각하면 됨



### 힌트 사용시 주의사항

- 힌트 사용전 미치는 영향을 충분히 검토하고 신중하게 적용해야 함
- 특히 입력되는 조건값에 따라 다양하게 변하는 SQL을 사용할 때는, 경우의 수를 모두 감안하여 사용하고자 하는 힌트의 적절성을 판단해야 함
- 또한, 힌트 사용전 DBMS의 통계 정보가 정확한지, 필요한 인덱스들이 만들어져 있는지를 우선 확인하는 습관을 길러야 함



### 힌트의 문법

```sql
--ORACLE
1) SELECT /*+ 힌트 */		-> 주로 사용
2) SELECT --+ 힌트
```



### 힌트의 종류

- 옵티마이저 (다음에 공부해서 올게요..)
- 접근 경로 및 인덱스
- 조인
- 기타



## 접근 경로 및 인덱스

#### (1) INDEX

```sql
/*+ INDEX(table_name index_name) */
```

- 특정 인덱스를 사용하도록 강제로 제어하는 힌트로, 튜닝시 많이 쓰는 힌트 중 하나
- 반대로 특정 인덱스를 사용하지 않기를 원할 경우 `NO_INDEX` 힌트를 사용하는데, 가급적 사용하지 않는 것을 권장
- 인덱스 이름을 명확하게 지정하지 않고 특정 컬럼에 생성된 인덱스를 사용하고자 할 경우 `/*+ INDEX(table_name column_name) */` 로 사용 가능하나, 가급적 인덱스 이름을 명확하게 지정하는 것이 좋음



**예시)**

```sql
SELECT LOGIN_ID, USER_ID, ...
FROM TB_ORG_USER
WHERE LOGIN_ID = :0
	AND GROUP_ID = :1
;
```

실행계획

```
---------------------------------------------------
|  0 | SELECT STATEMENT							|							|
|  1 |  TABLE ACCESS BY INDEX ROWID	| TB_ORG_USER |
|* 2 |   INDEX RANGE SCAN						|	IX_ORG_USR1	|
---------------------------------------------------
```

인덱스 구조

| 테이블 이름 | 인덱스 이름 | 구성 컬럼 |
| ----------- | ----------- | --------- |
| TB_ORG_USER | IX_ORG_USR1 | GROUP_ID  |
|             | IX_ORG_USR4 | NAME      |
|             | IX_ORG_USR3 | LOGIN_ID  |

- WHERE 조건절에서 조건으로 사용되는 컬럼 LOGIN_ID가 변별력이 훨씬 높은 컬럼임에도 불구하고, GROUP_ID 컬럼에 생성한 IX_ORG_USR1 인덱스를 사용하는 것을 실행 계획을 통해 알 수 있음

- 원인

  1. 해당 테이블의 통계 정보가 잘못된 경우
  2. 컬럼의 데이터 분포 편차가 큰 경우 --> 이 예제에서의 원인

- 해결 방법

  ```sql
  SELECT /*+ INDEX(TB_ORG_USER IX_ORG_USR3) */ 
  	LOGIN_ID, USER_ID, ...
  FROM TB_ORG_USER
  WHERE LOGIN_ID = :0
  	AND GROUP_ID = :1
  ;
  ```



#### (2) FULL

```sql
/*+ FULL(table_name) */
```

- 특정 테이블에 대해 FULL TABLE SCAN을 하고자 할 때 설정하는 힌트
- INDEX SCAN이 적합하지 않음에도 불구하고 실행 계획에서 INDEX SCAN을 채택하고 있는 경우 주로 사용



**예시)**

```sql
SELECT CODE,
			 FNAME
 FROM	 TB_UNIT_CODE
 WHERE TYPE   = 'MAIN'
	 AND SUB    = 'MAIN_R'
	 AND USABLE = 'Y'
ORDER BY CODE;
```

실행계획

```
Rows		Execution Plan
--------------------------------------------------------
|   0 | SELECT STATEMENT		GOAL: CHOOSE
|   3 |  TABLE ACCESS (BY INDEX ROWID) OF 'TB_UNIT_CODE'
| 129 |   INDEX (FULL SCAN) OF 'PK_UNIT_CODE' (UNIQUE)
--------------------------------------------------------
```

인덱스 구조

| 테이블 이름  | 인덱스 이름  | 구성 컬럼 |
| ------------ | ------------ | --------- |
| TB_UNIT_CODE | PK_UNIT_CODE | CODE      |

- TB_UNIT_CODE라는 테이블은 코드 값을 저장하는 작은 사이즈의 테이블이며, 입력 당시에 이미 코드값의 순서대로 데이터가 입력되어 있음

- 하지만 ORDER BY 절에서 CODE 컬럼 값을 기준으로 정렬을 하고 있어서 이 컬럼에 만들어진 인덱스를 FULL SCAN하고 있음

- 따라서 인덱스를 사용하지 않고 테이블 전체를 검색해서 원하는 결과를 얻어오도록 FULL 힌트를 추가하면 성능이 향상됨

  ```sql
  SELECT /*+ FULL(TB_UNIT_CODE) */
  			 CODE,
  			 FNAME
   FROM	 TB_UNIT_CODE
   WHERE TYPE   = 'MAIN'
  	 AND SUB    = 'MAIN_R'
  	 AND USABLE = 'Y'
  ORDER BY CODE;
  ```

  

## 조인

#### (1) ORDERED

```sql
/*+ ORDERED */
```

- 조인 순서를 지정하는 힌트
- FROM절에 기술된 테이블의 순서대로 조인을 처리하도록 함
- ex) A, B, C, D 순서로 FROM절에 기술되어 있으면 이 순서대로 실제 테이블에 접근하게 됨



#### (2) LEADING

```sql
/*+ LEADING(table_name1 table_name2 ...) */
```

- FROM절에 기술된 테이블 순서와 관계없이 힌트에 직접 조인 순서를 기술
- 주로, 드라이빙 테이블을 변경하고자 할 때 사용



**예시)**

```sql
SELECT *
FROM  (SELECT INNER_TABLE.*,
      				ROWNUM AS ROW_SEQ
       FROM   (SELECT /*+ LEADING(TB) */
              				TA.CUST_NO,
               				TA.CUST_DOC_NO,
 				              TC.CUST_NAME,
               				...
               FROM		TB_DOC_DATA TA,
               				TB_DOC_CNT	TB,
               				TB_PERSON		TC
               WHERE	TA.DOC_NO = TB.DOC_NO
               	 AND	TA.CUST_NO = TC.CUST_NO
               	 AND	TB.DEL_YN = 'Y'
               	 AND	TB.CLASS_CODE = '2'
               ORDER BY TC.CUST_NAME
              ) INNER_TABLE
      WHERE 	ROWNUM <= 100
      )
WHERE ROW_SEQ BETWEEN 1 AND 100
;
```

- 힌트가 없으면 ORDER BY 절 때문에 TC를 드라이빙 테이블로 선택함
- `TB.CLASS_CODE = '2'` 조건이 변별력이 더 높은 조건이라 TB 테이블을 드라이빙 테이블로 하는 것이 더 유리하므로 힌트를 추가하는게 성능이 향상됨



## 기타

#### (1) PARALLEL

```sql
/*+ PARALLEL(table_name degree) */
```

- 하나의 작업을 여러 개의 서버 프로세스가 동시에 병렬로 처리하도록 설정하는 힌트
- DEGREE : 몇 개의 서버 프로세스가 동시에 처리하게 할 것인지 설정하는 값
- 각각의 프로세스에게 분배하는 방식을 제어하기 위해서는 `PQ_DISTRIBUTE` 힌트를 함께 사용하는 방법도 있음
- **PARALLEL 힌트는 DBMS의 자원을 임의로 할당하여 사용하게 하는 역할을 하므로, 무분별하게 사용하는 것은 시스템 전체에 영향을 끼칠 수 있음**



**예시)**

```sql
SELECT	VX.CLASS_CODE,
				VX.MANAGE_DEPT,
				COUNT(DISTINCT( VX.CUST_NO )),
				COUNT(*),
				SUM(VX.A_AMT + VX.B_AMT)
FROM		(SELECT /*+ PARALLEL(TB_MASTER 4) */ 
        				CLASS_CODE,
         				CUST_NO,
         				MANAGE_DEPT,
         				...
         FROM		TB_MASTER
        ) VX
GROUP BY VX.CLASS_CODE,
				 VX.MANAGE_DEPT;
```

- WHERE 조건절에 대상을 걸러내기 위한 검색 조건이 없음
- 즉, 대량의 데이터를 가지고 할 수밖에 없는 작업의 성능 개선을 위해 PARALLEL 힌트를 사용함



