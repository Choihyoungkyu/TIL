# Spring 7일차 - Professional REST API

---



### REST API Documentation

- Your REST API consumers need to understand your REST API :
  - Resources
  - Actions
  - Request / Response Structure (Constraints / Validations)
- **Challenges** :
  - Accuracy : How do you ensure that your documentation is upto date and correct?
  - Consistency : You might have 100s of REST API in an enterprise. How do you ensure consistency?
- **Options** :
  1. Manually Maintain Documentation
     - Additional effort to keep it in sync with code
  2. **Generate from code**
     - Swagger and Open API



### Swagger and Open API

- 2011 : Swagger Specification and Swagger Tools were introduced
- 2016 : Open API Specification created based on Swagger Spec.
  - Swagger Tools (ex: Swagger UI) continue to exist
- **OpenAPI Specification** : Standard, language-agnostic interface
  - Discover and understand REST API
  - Earlier called Swagger Specification
- **Swagger UI** : Visualize and interact with your REST API

```xml
<dependency>
  <groupId>org.springdoc</groupId>
  <artifactId>springdoc-openapi-starter-webmvc-ui</artifactId>
  <version>2.0.0</version>
</dependency>
```

- http://localhost:8080/swagger-ui/index.html



### Content Negotiation

- **Same Resource** - Same URI
  - However, **Different Representations** are possible
    - ex: Different Content Type - XML or JSON or ...
    - ex: Different Language - English or Dutch or ...
- How can a consumer tell the REST API provider what they want?
  - **Content Negotiation**
- ex: Accept header (MIME types application/xml, application/json, ...)
- ex: Accept-Language header (en, nl, fr, ...)

```xml
<!-- xml 형식의 데이터 반환할 수 있도록 해줌 -->
<dependency>
  <groupId>com.fasterxml.jackson.dataformat</groupId>
  <artifactId>jackson-dataformat-xml</artifactId>
</dependency>
<!-- 의존성 추가 후 header의 Accept에 application/xml을 추가하면 바로 xml 형식 반환 -->
```



### Internationalization - i18n

- Your REST API might have consumers from around the world
- How do you customize it to users around the world?
  - **Internationalization - i18n**
- Typically **HTTP Request Header - Accept-Language** is used
  - Accept-Language : indicates natural language and locale that the consumer prefers
  - ex: en, nl, fr, ...
- messages.properties를 application.properties와 같은 위치에 만들어 기본 언어를 설정
- messages_kr.properties와 같이 언더바(_)를 통해 국제화 실현

```java
// Controller.java
@GetMapping(path="/hello-world-internationalized")
public String helloWorldInternationalized() {

  Locale locale = LocaleContextHolder.getLocale();
  return messageSource.getMessage("good.morning.message", null, "Default Message", locale);
}
```

```properties
# messages.properties
good.morning.message=Good Morning
```

```properties
# messages_kr.properties
good.morning.message=좋은 아침입니다
```



### Versioning REST API

- You have built an amazing REST API
  - You have 100s of consumers
  - You need to implement a breaking change
    - ex: Split name into firstName and lastName
- **SOLUTION** : Versioning REST API
  - **Variety of options**
    - URL
    - Request Parameter
    - Header
    - Media Type

```java
// VersioningPersonController.java
@RestController
public class VersioningPersonController {
	
	// URI Versioning - Twitter
	@GetMapping("/v1/person")
	public PersonV1 getFirstVersionOfPerson() {
		return new PersonV1("Bob Charlie");
	}
	
	@GetMapping("/v2/person")
	public PersonV2 getSecondVersionOfPerson() {
		return new PersonV2(new Name("Bob", "Charlie"));
	}
	
	
	// Request Parameter Versioning - Amazon
	@GetMapping(path="/person", params="version=1")
	public PersonV1 getFirstVersionOfPersonRequestParameter() {
		return new PersonV1("Bob Charlie");
	}
	
	@GetMapping(path="/person", params="version=2")
	public PersonV2 getSecondVersionOfPersonRequestParameter() {
		return new PersonV2(new Name("Bob", "Charlie"));
	}
	
	
	// (Custom) headers versioning - Microsoft
	@GetMapping(path="/person/header", headers="X-API-VERSION=1")
	public PersonV1 getFirstVersionOfPersonRequestHeader() {
		return new PersonV1("Bob Charlie");
	}
	
	@GetMapping(path="/person", headers="X-API-VERSION=2")
	public PersonV2 getSecondVersionOfPersonRequestHeader() {
		return new PersonV2(new Name("Bob", "Charlie"));
	}
	
	
	// Media type versioning (a.k.a "content negotiation" or "accept header") - Github
  // (in header) Accept=application/vnd.company.app-v1+json
	@GetMapping(path="/person/accept", produces="application/vnd.company.app-v1+json")
	public PersonV1 getFirstVersionOfPersonAcceptHeader() {
		return new PersonV1("Bob Charlie");
	}
	
	@GetMapping(path="/person/accept", produces="application/vnd.company.app-v2+json")
	public PersonV2 getSecondVersionOfPersonAcceptHeader() {
		return new PersonV2(new Name("Bob", "Charlie"));
	}
}
```



### HATEOAS

- Hypermedia as the Engine of Application State (HATEOAS)
- Websites allow you to :
  - See **Data** AND Perform **Actions** (using links)
- How about enhancing your REST API to tell consumers how to perform subsequent actions?
  - **HATEOAS**
- **Implementation Options** : 
  1. Custom Format and Implementation
     - Difficult to maintain
  2. Use Standard Implementation
     - **HAL (JSON Hypertext Application Language)** : Simple format that gives a consistent and easy way to hyperlink between resources in your API
     - **Spring HATEOAS** : Generate HAL responses with hyperlinks to resources
- ex)

```json
{
  "name": "Adam",
  "birthDate": "2022-08-16",
  "_links": {
    "all-users": {
      "href": "http://localhost:8080/users"
    }
  }
}
```

```java
// UserResource.java
import static org.springframework.hateoas.server.mvc.WebMvcLinkBuilder.*;
import org.springframework.hateoas.EntityModel;
import org.springframework.hateoas.server.mvc.WebMvcLinkBuilder;

@GetMapping("/users/{id}")
public EntityModel<User> retrieveUser(@PathVariable int id) {
  User user = service.findOne(id);

  if(user == null) {
    throw new UserNotFoundException("id : "+id);
  }

  // EntityModel 생성
  EntityModel<User> entityModel = EntityModel.of(user);

  // 데이터와 관련된 링크 생성 후 추가 
  // (주의사항 : linkTo와 methodOn을 사용하기 위해서는 import를 static으로 해야됨)
  WebMvcLinkBuilder link = linkTo(methodOn(this.getClass()).retrieveAllUsers());
  entityModel.add(link.withRel("all-users"));

  return entityModel;
}
```



### Customizing REST API Response - Filtering and more..

- **Serialization** : Covert object to steam (ex: JSON)
  - Most popular JSON Serialization in Java : Jackson
- How about customizing the REST API response returned by Jackson framework?
  1. Customize field names in response
     - `@JSONProperty`
  2. Return only selected fields
     - **Filtering** (ex: Filter out Password)
     - **Two types** :
       - **Static Filtering** : Same filtering for a bean across different REST API
         - `@JsonIgnoreProperties`, `@JsonIgnore`
       - **Dynamic Filtering** : Customize filtering for a bean for specific REST API
         - `@JsonFilter` with FilterProvider



### Static Filtering

- `@JsonIgnoreProperties({"field1", "field2", ...})` : Class Annotation
- `@JsonIgnore` : Field Annotation

```java
// SomeBean.java
@JsonIgnoreProperties("field1")		// field1을 JSON 응답에 나타내지 않음
public class SomeBean {
	private String field1;
	@JsonIgnore
	private String field2;	// field2를 JSON 응답에 나타내지 않음
	private String field3;
	...
}
```

```java
// FilteringController.java
@RestController
public class FilteringController {
	
	@GetMapping("/filtering")
	public SomeBean filtering() {
		return new SomeBean("value1", "value2", "value3");
	}
  // field3만 나옴 (위에서 field1, field2는 나오지 않도록 해놨으므로)
	
	@GetMapping("/filtering-list")
	public List<SomeBean> filteringList() {
		return Arrays.asList(new SomeBean("value1", "value2", "value3"),
				new SomeBean("value4", "value5", "value6"));
	}
}
```



### Dynamic Filtering

- `@JsonFilter` & Definition filter in controller

```java
// SomeBean.java
@JsonFilter("SomeBeanFilter")		// controller에서 정의한 SomeBeanFilter에 맞게 동적 필터링
public class SomeBean {
	private String field1;
	private String field2;
	private String field3;
	...
}
```

```java
// FilteringController.java
@RestController
public class FilteringController {
  // 필터 정의 메서드 -> 나중에 Service로 빼면 될듯?
	private FilterProvider filter(String[] filterList) {
		SimpleBeanPropertyFilter filter = SimpleBeanPropertyFilter.filterOutAllExcept(filterList);
		
		FilterProvider filters = new SimpleFilterProvider().addFilter("SomeBeanFilter", filter);
		return filters;
	}
	
  // 아래 로직에서 필터를 정의해서 동적으로 필터링 가능
	@GetMapping("/filtering")
	public MappingJacksonValue filtering() {
		SomeBean someBean = new SomeBean("value1", "value2", "value3");
		
		MappingJacksonValue mappingJacksonValue = new MappingJacksonValue(someBean);
		
		FilterProvider filters = filter(new String[]{"field1", "field3"});
		
		mappingJacksonValue.setFilters(filters);
		
		return mappingJacksonValue;
	}
	
  // 여러 개를 반환할때도 적용되고, url이 다를 때 다른 값을 필터링 하도록 설정 가능
	@GetMapping("/filtering-list")
	public MappingJacksonValue filteringList() {
		List<SomeBean> list = Arrays.asList(new SomeBean("value1", "value2", "value3"),
				new SomeBean("value4", "value5", "value6"));
		
		MappingJacksonValue mappingJacksonValue = new MappingJacksonValue(list);
		
		FilterProvider filters = filter(new String[] {"field2", "field3"}); 
		
		mappingJacksonValue.setFilters(filters);
		
		return mappingJacksonValue;
	}
}
```



### Get Production - ready with Spring Boot Actuator

- **Spring Boot Actuator** : Provides Spring Boot's production-ready features
  - Monitor and manage your application in your production
- **Spring Boot Starter Actuator** : Starter to add Spring Boot Actuator to your application
  - **spring-boot-starter-actuator**
- Provides a number of endpoints :
  - **beans** - Complete list of Spring beans in your app
  - **health** - Application health information
  - **metrics** - Application metrics
  - **mappings** - Details around Request Mappings

```xml
<dependency>
  <groupId>org.springframework.boot</groupId>
  <artifactId>spring-boot-starter-actuator</artifactId>
</dependency>
```

- http://localhost:8080/actuator
- how to see all features?

```properties
# application.properties
management.endpoints.web.exposure.include=*
```



### Explore REST API using HAL Explorer

1. **HAL (JSON Hypertext Application Language)**
   - Simple format that gives a consistent and easy way to hyperlink between resources in your API
2. **HAL Explorer**
   - An API explorer for RESTful Hypermedia APIs using HAL
   - Enable your non-technical teams to play with APIs
3. **Spring Boot HAL Explorer**
   - Auto-configures HAL Explorer for Spring Boot Projects

```xml
<dependency>
  <groupId>org.springframework.data</groupId>
  <artifactId>spring-data-rest-hal-explorer</artifactId>
</dependency>
```



### Connection between user and post

```java
// User.java
@Entity(name="user_details")
public class User {
  @Id
  @GeneratedValue
  private Integer id;
  
  @JsonProperty("user_name")
  private String name;
  
  @JsonProperty("birth_date")
  private LocalDate birthDate;
  
  @OneToMany(mappedBy = "user")
  @JsonIgnore
  private List<Post> posts
}

// USER_DETAILS -> Table
// fields : ID, BIRTH_DATE, NAME
```

```java
// Post.java
@Entity
public class Post {
  @Id
  @GeneratedValue
  private Integer id;
  
  private String description;
  
  @ManyToOne(fetch = FetchType.LAZY)
  @JsonIgnore
  private User user;
}

// POST -> Table
// fields : ID, DESCRIPTION, USER_ID	=>	USER_ID 필드가 자동으로 생성됨
```

- Retrieve All Posts For User

```java
// UserJpaResource.java
@GetMapping("/jpa/users/{id}/posts")
public List<Post> retrievePostsForUser(@PathVariable int id) {
  // 1. find user
  Optional<User> user = repository.findById(id);

  // 2. null check
  if(user.isEmpty()) {
    throw new UserNotFoundException("id : " + id);
  }

  // 3. return all posts (.getPosts() -> defined by setter)
  return user.get().getPosts();
}
```



### Spring Security

- Basic Setting

```xml
<dependency>
  <groupId>org.springframework.boot</groupId>
  <artifactId>spring-boot-starter-security</artifactId>
</dependency>
```

```properties
spring.security.user.name=username
spring.security.user.password=password
```

- Spring Security 원리
  - 요청을 보낼 때마다 Spring Security가 해당 요청을 가로챔
  - 가로챈 요청에 대해 일련의 필터를 실행 (Filter Chains)
    1. All requests should be authenticated
    2. If a request is not authenticated, a web page is shown
    3. CSRF 필터 때문에 POST, PUT 요청에 영향을 주게 됨
- 기존 필터 체인을 오버라이드하려면 체인 전체를 다시 정의해야함
  - Configuration : Spring 설정 파일
  - Bean FilterChain : 필터 체인을 정의할 Bean

```java
// SpringSecurityConfiguration.java
import static org.springframework.security.config.Customizer.withDefaults;

@Configuration
public class SpringSecurityConfiguration {
	
	@Bean
	public SecurityFilterChain filterChain(HttpSecurity http) throws Exception {
//		1. All requests should be authenticated -> 인증이 없으면 페이지 자체를 안띄움
		http.authorizeHttpRequests(
				auth -> auth.anyRequest().authenticated()
			);
		
//		2. If a request is not authenticated, a web page is shown -> 로그인 페이지 팝업 띄우기
		http.httpBasic(withDefaults());
		
//		3. CSRF 필터 때문에 POST, PUT 요청에 영향을 주게 됨 -> disable
		http.csrf().disable();
		
		return http.build();
	}
}
```

