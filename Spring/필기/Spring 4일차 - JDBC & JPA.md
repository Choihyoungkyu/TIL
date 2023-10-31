# Spring 4일차 - JDBC & JPA

---

### Hibernate vs JPA

- **JPA**는 기술 명세를 정의함. 즉, **API**임.
  - 엔터티가 무엇인지 정의하는 방식을 의미하는 **인터페이스**를 나타냄
  - 객체를 테이블로 매핑하는 방식을 정의
    (= 엔터티를 매핑하는 방법, 속성을 매핑하는 방법, EntityManager를 활용하는 방법을 정의)
    - `@Entity`를 활용해서 엔터티를 정의함
    - `@Column(name="이름")`를 활용해서 속성 매핑
      - 만약 이름이 같으면 이 어노테이션은 없어도 됨
    - `EntityManager`를 활용해 엔터티들의 메서드들을 정의함
- **Hibernate** : JPA에서 매우 인기 있는 구현체
  - JPA에 매핑된 방식을 보고 그걸 구현
  - 코드에서 Hibernate를 직접 사용할 수 있는 옵션이 있음
    - `@Entity` -> `org.hibernate.annotations`에서 임포트하면 됨
  - JPA를 통해 Hibernate JAR를 클래스 경로에 추가해서 Hibernate를 JPA 구현체로 사용하는 것이 더 좋음
    - Hibernate로만 한정해서 쓰고 싶지 않기 때문
- Toblink : JPA에서 사용할 수 있는 또 다른 구현체



---

### Learning JPA and Hibernate - Approach

- 01: Create a **Spring Boot Project** with H2

  - start.spring.io -> Dependencies : Spring Web, Spring Data JPA, Spring Data JDBC, H2 Database

- 02: Create **COURSE table**

  - ```properties
    spring.h2.console.enabled=true
    spring.datasource.url=jdbc:h2:mem:testdb
    ```

  - ```sql
    create table course
    (
    	id bigint not null,
    	name varchar(255) not null,
    	author varchar(255) not null,
    	primary key (id)
    );
    ```

  - http://localhost:8080/h2-console -> enter using the url

- 03: Use **Spring JDBC** to play with COURSE table



---

### JDBC to Spring JDBC to JPA to Spring Data JPA

- **JDBC**

  - Write a lot of SQL queries! (delete from todo where id=?)
  - And write a lot of Java code

  ```java
  public void deleteTodo (int id) {
    PreparedStatement st = null;
    try {
      st = db.conn.prepareStatement("delete from todo where id=?");
      st.setInt(1, id);
      st.execute();
    } catch (SQLException e) {
      logger.fatal("Query Failed : ", e);
    } finally {
      if (st != null) {
        try {st.close();}
        catch (SQLException e) {}
      }
    }
  }
  ```

- **Spring JDBC**

  - Write a lot of SQL queries (delete from todo where id=?)
  - BUT lesser Java code

  ```java
  public void deleteTodo(int id) {
    jdbcTemplate.update("delete from todo where id=?", id);
  }
  ```

- **JPA**

  - Do NOT worry about queries
  - Just Map Entities to Tables!

- **Spring Data JPA**

  - Let's make JPA even more simple!
  - I will take care of everything!



---

### Insert the hard-corded data using Spring JDBC

```java
// CourseJdbcRepository.java

@Repository
public class CourseJdbcRepository {
  
  @Autowired
  private JdbcTemplate springJdbcTemplate;
  
  private static String INSERT_QUERY =
    """
      insert into course (id, name, author)
      values(1, 'Learn AWS', 'in28mintues');
    """;
        
	public void insert() {
      springJdbcTemplate.update(INSERT_QUERY);
    }
}
```

```java
@Component
public class CourseJdbcCommandLineRunner implements CommandLineRunner {
  
  @Autowired
  private CourseJdbcRepository repository;
  
  @Override
  public void run(String... args) throws Exception {
    repository.insert();
  }
}
```

- `CommandLineRunner` : Spring 애플리케이션 시작 시에 실행될 로직이 있을 때 활용
  - 여기서는 애플리케이션 시작시 `insert` 실행



---

### Insert the data Using Spring JDBC

```java
// CourseJdbcRepository.java

@Repository
public class CourseJdbcRepository {
  
  @Autowired
  private JdbcTemplate springJdbcTemplate;
  
  // 값을 받아서 넣고 싶으면 특정 값이 아닌 "?" 사용하기!!
  private static String INSERT_QUERY =
			"""
				insert into course (id, name, author)
				values(?, ?, ?);
			""";
        
  public void insert(Course course) {
		springJdbcTemplate.update(INSERT_QUERY, 
				course.getId(), course.getName(), course.getAuthor());
	}
}
```

```java
// CourseJdbcCommandLineRunner.java

@Component
public class CourseJdbcCommandLineRunner implements CommandLineRunner {

	@Autowired
	private CourseJdbcRepository repository;
	
	@Override
	public void run(String... args) throws Exception {
		repository.insert(new Course(1, "Learn AWS Now!", "in28minutes"));
		repository.insert(new Course(2, "Learn Azure Now!", "in28minutes"));
		repository.insert(new Course(3, "Learn DevOps Now!", "in28minutes"));
	}
}

```



---

### Select the data in database using Spring JDBC

```java
// CourseJdbcRepository.java

@Repository
public class CourseJdbcRepository {
  
  @Autowired
  private JdbcTemplate springJdbcTemplate;
  
  // 값을 받아서 넣고 싶으면 특정 값이 아닌 "?" 사용하기!!
  private static String SELECT_QUERY =
			"""
				select * from course
				where id = ?
			""";
        
  public Course findById(long id) {
		//ResultSet -> Bean => Row Mapper를 통해 JSON을 Bean으로 만들어줘야됨
    //queryForObject(query, 받을 객체, 조건)
		return springJdbcTemplate.queryForObject(SELECT_QUERY, 
				new BeanPropertyRowMapper<>(Course.class), id);
	}
}
```

- 주의사항) Course 객체에 Setter를 추가해줘야 됨



---

### JPA

```java
// CourseJpaRepository.java

@Repository
@Transactional		// JPA 사용시 필수!!
public class CourseJpaRepository {
  
  @PersistenceContext
  private EntityManager entityManager;
  
  public void insert(Course course) {
    entityManager.merge(course)		// insert the data
  }
  
  public void deleteById(long id) {
    Course course = entityManager.find(Course.class, id);		// select the data
    entityManager.remove(course);	// delete the data
  }
  
  public Course findById(long id) {
    return entityManager.find(Course.class, id);		// select the data
  }
}
```

```java
// CourseCommandLineRunner.java

@Component
public class CourseCommandLineRunner implements CommandLineRunner {
  @Autowired
  private CourseJpaRepository repository;
  
  @Override
  public void run(String... args) throws Exception {
		repository.insert(new Course(1, "Learn AWS Jpa!", "in28minutes"));
		repository.insert(new Course(2, "Learn Azure Jpa!", "in28minutes"));
		repository.insert(new Course(3, "Learn DevOps Jpa!", "in28minutes"));
		
		repository.deleteById(1);
		
		System.out.println(repository.findById(2));
		System.out.println(repository.findById(3));
	}
}
```

- Show the Queries after excecuted

```properties
spring.jpa.show-sql=true
```



---

### Spring JPA

- `JpaRepository<Entity, Id의 타입>`
- 인터페이스로 확장만 하면 자동 매핑되므로 `EntityManager`를 만들 필요가 없음
- 수많은 메소드들이 이미 구현되어 있으므로 쿼리 작성 및 메소드 작성이 거의 없음

```java
// CourseSpringDataJpaRepository.java

public interface CourseSpringDataJpaRepository extends JpaRepository<Course, Long> {
  
  List<Course> findByAuthor(String author);
  
}
```

```java
// CourseCommandLineRunner.java

@Component
public class CourseCommandLineRunner implements CommandLineRunner {
  @Autowired
  private CourseSpringDataJpaRepository repository;
  
  @Override
  public void run(String... args) throws Exception {
		repository.save(new Course(1, "Learn AWS Jpa!", "in28minutes"));		// insert = save
		repository.save(new Course(2, "Learn Azure Jpa!", "in28minutes"));
		repository.save(new Course(3, "Learn DevOps Jpa!", "in28minutes"));
		
		repository.deleteById(1l);	// id를 인자로 사용할 때는 타입을 맞춰줘야됨 (Long -> 1l)
		
		System.out.println(repository.findById(2l));	// (Long -> 2l)
		System.out.println(repository.findById(3l));	// (Long -> 3l)
    
    System.out.println(repository.findByAuthor("in28minutes"));	// => [Course [id=2, ...]...]
		System.out.println(repository.findByAuthor(""));	// => []
	}
}
```

