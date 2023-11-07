# Spring 6일차 - Basic REST API & Exception Handler

---



### What's Happening in the Background?

- Let's explore some **Spring Boot Magic** : Enable Debug Logging

1. How are our requests handled?
   - **DispatcherServlet** - Front Controller Pattern
     - Mapping servlets : dispatcherServlet urls = [ / ]
     - **Auto Configuration** (DispatcherServletAutoConfiguration)
2. How does **HelloWorldBean** object get converted to JSON?
   - `@ResponseBody` + `JacksonHttpMessageConverters`
     - **Auto Configuration** (JacksonHttpMessageConvertersConfiguration)
3. Who is configuring error mapping?
   - **Auto Configuration** (`ErrorMvcAutoConfiguration`)
4. How are all jars available (Spring, Spring MVC, Jackson, Tomcat)?
   - **Starter Projects** - Spring Boot Starter Web (spring-webmvc, spring-web, spring-boot-starter-tomcat, spring-boot-starter-json)



### Social Media Application - Resources & Methods

```java
// User.java
public class User {
	
	private Integer id;
	private String name;
	private LocalDate birthDate;
	
	public User(Integer id, String name, LocalDate birthDate) {
		super();
		this.id = id;
		@Size(min=2, message="Name should have at least 2 characters")
    private String name;

    @Past(message="Birth Date should be in the past")
    private LocalDate birthDate;
	}

	public Integer getId() {
		return id;
	}

	public void setId(Integer id) {
		this.id = id;
	}

	public String getName() {
		return name;
	}

	public void setName(String name) {
		this.name = name;
	}

	public LocalDate getBirthDate() {
		return birthDate;
	}

	public void setBirthDate(LocalDate birthDate) {
		this.birthDate = birthDate;
	}

	@Override
	public String toString() {
		return "User [id=" + id + ", name=" + name + ", birthDate=" + birthDate + "]";
	}	
}
```

```java
// UserDaoService.java
@Component
public class UserDaoService {
	private static List<User> users = new ArrayList<>();
	
	private static Integer userCount = 0;
	
	static {
		users.add(new User(++userCount, "Adam", LocalDate.now().minusYears(30)));
		users.add(new User(++userCount, "Eve", LocalDate.now().minusYears(25)));
		users.add(new User(++userCount, "Jim", LocalDate.now().minusYears(20)));
	}
	
	 public List<User> findAll() {
		 return users;
	 }
	
	 public User save(User user) {
		 user.setId(++userCount);
		 users.add(user);
		 return user;
	 }
	
	 public User findOne(int id) {
		Predicate<? super User> predicate = user -> user.getId().equals(id); 
		return users.stream().filter(predicate).findFirst().get();
	}	
}
```

```java
// UserResource.java
@RestController
public class UserResource {
	
	private UserDaoService service;
	
	public UserResource(UserDaoService service) {
		this.service = service;
	}
	
	// GET /users
	@GetMapping("/users")
	public List<User> retrieveAllUsers() {
		return service.findAll();
	}
	
	// GET /users
	@GetMapping("/users/{id}")
	public User retrieveUser(@PathVariable int id) {
		return service.findOne(id);
	}
	
	// POST /users
	@PostMapping("/users")
	public ResponseEntity<User> createUser(@RequestBody User user) {
		User savedUser = service.save(user);
		
		URI location = ServletUriComponentsBuilder
                    .fromCurrentRequest()
                    .path("/{id}")
                    .buildAndExpand(savedUser.getId())
                    .toUri();
    // location = "http://localhost:8080/users/4"
		
		return ResponseEntity.created(location).build();	// 201 created
	}
}
```



### Response Status for REST API

- Return the **correct response status**

  - Resource is not found => 404

  - Server exception => 500
  - Validation error => 400

- **Important Response Statues**

  - 200 - Success
  - 201 - Created
  - 204 - No Content : Update할 때나 Unauthorized와 같이 콘텐츠가 없음을 응답 상태로 보내야 할 경우
  - 401 - Unauthorized (when authorization fails)
  - 400 - Bad Request (such as validation error)
  - 404 - Resource Not Found
  - 500 - Server Error



### Error Page for All Resources

- `@ControllerAdvice`를 통해 모든 컨트롤에 대해 적용시켜줌
- 보여줄 항목들을 ErrorDetails 에 나타낸 뒤 ResponseEntity 에 적용시켜주면 됨
- `@ExceptionHandler(Exception.class)` : 모든 예외 상황에 대한 처리
- `@ExceptionHandler(UserNotFoundException.class)` : 유저가 없는 상황에서만 예외 처리
  - -> 모든 경우에 대해 처리한 뒤 오버라이딩 하는 방식으로 쓰면 될 듯!

```java
// ErrorDetails.java
public class ErrorDetails {
	private LocalDateTime timestamp;
	private String message;
	private String details;
	
	public ErrorDetails(LocalDateTime timestamp, String message, String details) {
		super();
		this.timestamp = timestamp;
		this.message = message;
		this.details = details;
	}

	public LocalDateTime getTimestamp() {
		return timestamp;
	}

	public String getMessage() {
		return message;
	}

	public String getDetails() {
		return details;
	}
}
```

```java
// CustomizedResponseEntityExceptionHandler.java
@ControllerAdvice
public class CustomizedResponseEntityExceptionHandler extends ResponseEntityExceptionHandler {

  // 모든 상황에 대한 예외 처리
	@ExceptionHandler(Exception.class)
	public final ResponseEntity<ErrorDetails> handleAllException(Exception ex, WebRequest request) throws Exception {
		ErrorDetails errorDetails = new ErrorDetails(LocalDateTime.now(),
				ex.getMessage(), request.getDescription(false));
		
		return new ResponseEntity<ErrorDetails>(errorDetails, HttpStatus.INTERNAL_SERVER_ERROR);	// 500
	}
	
  // 유저가 없는 경우에 대한 예외 처리
	@ExceptionHandler(UserNotFoundException.class)
	public final ResponseEntity<ErrorDetails> handleUserNotFoundException(Exception ex, WebRequest request) throws Exception {
		ErrorDetails errorDetails = new ErrorDetails(LocalDateTime.now(),
				ex.getMessage(), request.getDescription(false));
		
		return new ResponseEntity<ErrorDetails>(errorDetails, HttpStatus.NOT_FOUND);	// 404
	}
  
  // 유효성 검사에 대한 에러 처리
  @Override
	protected ResponseEntity<Object> handleMethodArgumentNotValid(
			MethodArgumentNotValidException ex, HttpHeaders headers, HttpStatusCode status, WebRequest request) {
		ErrorDetails errorDetails = new ErrorDetails(LocalDateTime.now(),
				"Total Errors: " + ex.getErrorCount() + ", First Error : " + ex.getFieldError().getDefaultMessage(), request.getDescription(false));
		
		return new ResponseEntity(errorDetails, HttpStatus.BAD_REQUEST);	
	
	}
}
```



