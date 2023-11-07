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















