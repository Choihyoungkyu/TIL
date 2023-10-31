# Spring 5일차

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

