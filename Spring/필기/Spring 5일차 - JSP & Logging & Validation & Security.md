# Spring 5일차 - JSP & Logging & Validation & Security

---



### JSP(Java Server Page)

- 특정 경로에 저장돼야 함 - `/src/main/resources/META-INF/resources/WEB-INF/jsp/sayHello.jsp`
- JSP를 사용하려면 의존성을 추가해줘야 됨

```xml
<dependency>
  <groupId>org.apache.tomcat.embed</groupId>
  <artifactId>tomcat-embed-jasper</artifactId>
  <scope>provided</scope>
</dependency>
```



### Request Param

- url에 값을 넣고 해당 값을 읽어올 수 있음
- url : http://localhost:8080/login?name=Ranga

```java
@Controller
public class LoginController {
  @RequestMapping("login")
  public String goToLoginPage(@RequestParam String name, ModelMap model) {
    model.put("name", name);
    return "login";
  }
}
```

```jsp
<html>
	<head>
		Login Page
	</head>
	<body>
		Welcome to the login page ${name}!
	</body>
</html>
```



### ModelMap

- RequestParam에 있는 값을 jsp로 넘겨줄 때 사용
- `model.put("변수 이름", 변수);` 로 사용



### Understanding Logging

```properties
logging.level.some.path=debug
logging.level.some.other.path=error
logging.file.name=logfile.log

logging.level.org.springframework=info																	# 전체 로깅 수준
logging.level.com.in28minutes.springboot.mifirsewebapp=debug						# 해당 path만 debug 로깅
```

```java
@Controller
public class LoginController {
	private Logger logger = LoggerFactory.getLogger(getClass());

	@RequestMapping("login")
	public String goToLoginPage(@RequestParam String name, ModelMap model) {
		model.put("name", name);
		logger.debug("Request param is {}", name);		// debug 단계에서만 나타남
		logger.info("info : {}", name);								// info 단계에서만 나타남
		return "login";
	}
}
```

- **Default** : Logback with SLF4j (imported by this)



### Spring MVC Front Controller - Dispatcher Servlet

- 모든 요청을 Dispatcher Servlet에서 받은 뒤 뿌림

1. Receives HTTP Request
2. Processes HTTP Request
   1. Identifies correct Controller method
      - Based on request URL
   2. Executes Controller method
      - Returns Model and View Name
   3. Identifies correct View
      - Using ViewResolver (View Resolver : prefix와 suffix를 통해 적절한 jsp 파일을 찾도록 도와주는 것)
   4. Executes view
3. Returns HTTP Response



### @RequestMapping

- 특정 요청(ex. GET, POST)만 처리할 수 있게 만들 수 있음
- `@RequestMapping(value="login", method=RequestMethod.POST)`



### Session vs Request Scopes

- All requests from browser are handled by our web application deployed on a server
- **Request Scope** : Active for a single request **ONLY**
  - Once the response is sent back, the request attributes will be removed from memory
  - These cannot be used for future requests
  - Recommended for most use cases
- **Session Scope** : Details stored across multiple requests
  - Be careful about what you store in session (Takes additional memory as all details are stored on server)

```java
@Controller
@SessionAttributes("name")					// 어노테이션 추가 후 세션에 저장할 변수 이름 등록
public class TodoController {
	
	private TodoService todoService;
	
	public TodoController(TodoService todoService) {
		super();
		this.todoService = todoService;
	}


	// /list-todos
	@RequestMapping("list-todos")
	public String listAllTodos(ModelMap model) {
		List<Todo> todos = todoService.findByUsername("in28minutes");
		model.addAttribute("todos", todos);
		
		return "listTodos";
	}
}
```

```java
@Controller
@SessionAttributes("name")				// 다른 곳에서도 사용 가능
public class LoginController {
}
```



### JSTL

- JSP 파일 안에서 다양한 기능을 사용할 수 있게 만들어줌

```xml
<dependency>
  <groupId>jakarta.servlet.jsp.jstl</groupId>
  <artifactId>jakarta.servlet.jsp.jstl-api</artifactId>
</dependency>

<dependency>
  <groupId>org.eclipse.jetty</groupId>
  <artifactId>glassfish-jstl</artifactId>
</dependency>
```



### BootStrap & Jquery

```xml
<dependency>
  <groupId>org.webjars</groupId>
  <artifactId>bootstrap</artifactId>
  <version>5.1.3</version>
</dependency>

<dependency>
  <groupId>org.webjars</groupId>
  <artifactId>jquery</artifactId>
  <version>3.6.0</version>
</dependency>
```



### Validations with Spring Boot

1. Spring Boot Starter Validation

   - pom.xml

   ```xml
   <dependency>
     <groupId>org.springframework.boot</groupId>
     <artifactId>spring-boot-starter-validation</artifactId>
   </dependency>
   ```

2. Command Bean (Form Backing Object)

   - 2-way binding (todo.jsp & TodoController.java) - 양방향 바인딩

   ```jsp
   <!-- todo.jsp -->
   <%@ taglib prefix="form" uri="http://www.springframework.org/tags/form" %>
   
   <form:form method="post" modelAttribute="todo">
     Description: <form:input type="text" path="description" required="required" />
     <form:input type="hidden" path="id" />
     <form:input type="hidden" path="done" />
     <input type="submit" class="btn btn-success" />
   </form:form>
   ```

   ```java
   // TodoController.java
   @RequestMapping(value="add-todo", method=RequestMethod.GET)
   public String showNewTodoPage(ModelMap model) {
     String username = (String)model.get("name");
     Todo todo = new Todo(0, username, "", LocalDate.now().plusYears(1), false);
     model.put("todo", todo);
     return "todo";
   }
   
   @RequestMapping(value="add-todo", method=RequestMethod.POST)
   public String addNewTodo(ModelMap model, Todo todo) {
     String username = (String)model.get("name");
     todoService.addTodo(username, todo.getDescription(), LocalDate.now().plusYears(1), false);
     return "redirect:list-todos";
   }
   ```

   ```java
   // TodoService.java
   public void addTodo(String username, String description,
       LocalDate targetDate, boolean done) {
     Todo todo = new Todo(++todosCount, username, description, targetDate, done);
     todos.add(todo);
   }
   ```

3. Add Validations to Bean

   - Todo.java

   ```java
   // Todo.java
   @Size(min=10, message="Enter at least 10 characters")
   private String description;
   ```

   - 검증 대상의 속성에 어노테이션 추가

   ```java
   // TodoController.java
   @RequestMapping(value="add-todo", method=RequestMethod.POST)
   public String addNewTodo(ModelMap model, @Valid Todo todo, BindingResult result) {
     if(result.hasErrors()) {
       return "todo";
     }
     String username = (String)model.get("name");
     todoService.addTodo(username, todo.getDescription(), LocalDate.now().plusYears(1), false);
     return "redirect:list-todos";
   }
   ```

   - 검증 대상에 `@Valid` 어노테이션 추가
   - `BindingResult`로 에러 핸들링 가능

4. Display Validation Errors in the View

   - todo.jsp



### JSP Fragment

- jspf 파일을 만들어서 컴포넌트로 사용 가능
- `<%@ include file="경로" %>` 로 임포트해서 사용 가능

```java
// listTodos.jsp
<%@ include file="common/navigation.jspf" %>
```

```java
// navigation.jspf
<nav class="navbar navbar-expand-md navbar-light bg-light mb-3 p-1">
	<a class="navbar-brand m-1" href="https://courses.in28minutes.com">in28minutes</a>
	<div class="collapse navbar-collapse">
		<ul class="navbar-nav">
			<li class="nav-item"><a class="nav-link" href="/">Home</a></li>
			<li class="nav-item"><a class="nav-link" href="/list-todos">Todos</a></li>
		</ul>
	</div>
	<ul class="navbar-nav">
		<li class="nav-item"><a class="nav-link" href="/logout">Logout</a></li>
	</ul>	
</nav>
```



### Spring Security

- pom.xml에 다음과 같이 추가

```xml
<dependency>
  <groupId>org.springframework.boot</groupId>
  <artifactId>spring-boot-starter-security</artifactId>
</dependency>
```

- Spring Security Configuration 파일 만들기
  - Bean을 직접 만들어야 됨

```java
@Configuration
public class SpringSecurityConfiguration {
	// LDAP or Database
	// In Memory --> 아래는 이 방법으로 만든거
	
	@Bean
	public InMemoryUserDetailsManager createUserDetailsManager() {
		// 지역변수로 pw input을 encoding 하기 
		Function<String, String> passwordEncoder
				= input -> passwordEncoder().encode(input);
				
		// user 객체 생성 후 build 하기
		UserDetails userDetails = User.builder()
									.passwordEncoder(passwordEncoder)
									.username("in28minutes")
									.password("dummy")
									.roles("USER", "ADMIN")
									.build();
		
		return new InMemoryUserDetailsManager(userDetails);
	}
	
  // 비밀번호 인코딩 함수
	@Bean
	public PasswordEncoder passwordEncoder() {
		return new BCryptPasswordEncoder();
	}
}
```

- Spring Security 에서 값을 가지고 오는 방법 : `SecurityContextHolder.getContext().getAuthentication()`

```java
private String getLoggedInUsername(ModelMap model) {
  Authentication authentication = SecurityContextHolder.getContext().getAuthentication();
  return authentication.getName();
}
```



### Connect the data using JPA

- Repository Interface 파일 생성
- Create, Update - `save()`
- Read - `findBy..()`
- Delete - `deleteBy..()`

```java
// TodoRepository.java
package com.in28minutes.springboot.mifirsewebapp.todo;

import java.util.List;
import org.springframework.data.jpa.repository.JpaRepository;

public interface TodoRepository extends JpaRepository<Todo, Integer>{
	public List<Todo> findByUsername(String username);
}
```

```java
// TodoController.java
@Controller
public class TodoController {
  private TodoRepository todoRepository;
  
  public TodoController(TodoRepository todoRepository) {
    super();
    this.todoRepository = todoRepository;
  }
  
  // Spring Security에서 값 가져오기
  public String getLoggedInUsername(ModelMap model) {
    Authentication authentication = SecurityContextHolder.getContext().getAuthentication();
    return authentication.getName();
  }
  
  // 모든 할 일 목록 가져오기
  @RequestMapping(value="list-todos", method=RequestMethod.GET)
  public String listAllTodos(ModelMap model) {
    String username = getLoggedInUsername(model);
    
    List<Todo> todos = todoRepository.findByUsername(username);	// ID가 아닌 값으로 찾을 때는 Repository에 따로 메소드를 등록해야됨
    model.addAttribute("todos", todos);
    
    return "listTodos";
  }
}
```



### Spring Boot Auto Configuration Magic - Data JPA

- We added Data JPA and H2 dependencies:
  - Spring Boot Auto Configuration does some magic:
    - Initialize JPA and Spring Data JPA frameworks
    - Launch an in memory database (H2)
    - Setup connection from App to in-memory database
    - Launch a few scripts at startup (ex. data.sql)
- **Remember** - H2 is in memory database
  - Does NOT persist data
  - Great for learning
  - BUT NOT so great for production



### Connect the data using MySQL

- Docker에 MySQL 설치하기

```shell
docker run --detach 
--env MYSQL_ROOT_PASSWORD=dummypassword 
--env MYSQL_USER=todos-user 
--env MYSQL_PASSWORD=dummytodos 
--env MYSQL_DATABASE=todos 
--name mysql 
--publish 3306:3306 
mysql:8-oracle
```

- application.properties 작성하기

```properties
# 코드가 실행된 후 테이블이 만들어져서 에러가 발생하는 것을 방지
spring.jpa.defer-datasource-initialization=true

# true로 설정시 쿼리가 다 로그에 남음
spring.jpa.show-sql=true

# 데이터베이스 주소
spring.datasource.url=jdbc:mysql://localhost:3306/todos

# 데이터베이스 주인(?) 이름(ID)
spring.datasource.username=todos-user

# 데이터베이스 비밀번호
spring.datasource.password=dummytodos

# JPA의 Hibernate 구현체를 사용해서 대화하겠다고 설정
spring.jpa.properties.hibernate.dialect=org.hibernate.dialect.MySQL8Dialect

# 프로젝트 실행시 MySQL에 있는 값들 자동으로 생성
spring.jpa.hibernate.ddl-auto=update
```

- Shell 에서 MySQL 확인하기

```shell
\connect todos-user@localhost:3306		# mysql 서버의 todos-user(MYSQL_USER)에 접속하기

\use todos														# 스키마 연결 (MYSQL_DATABASE)

\sql																	# 해당 스키마에서 sql 구문 사용한다고 선언
```



