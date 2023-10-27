# Spring 3일차 - Spring Boot 개념

---



### Before Spring Boot

- Setting up Spring Projects **before Spring Boot was NOT easy!**
  - 1: Dependency Management (pom.xml) - 의존성 관리
  - 2: Define Web App Configuration (web.xml) - 많은 설정
  - 3: Manage Spring Beans (context.xml)
  - 4: Implement Non Functional Requirements (NFRs) - 비기능 요구사항을 수동으로 구현
- AND repeat this for every new project!
- Typically takes a **few days** to setup for each project (and countless hours to maintain)



---

### Spring Boot의 목표

- 프로덕션 환경에서 사용 가능한 애플리케이션을 빠르게 빌드할 수 있도록 돕는 것
  - Build **QUICKLY**
    - Spring Initializer (spring.start.io)
    - Spring Boot Starter Projects
    - Spring Boot Auto Configuration
    - Spring Boot DevTools
  - Be **PRODUCTION-READY**
    - Logging
    - Different Configuration for Different Environments
      - Profiles, ConfigurationProperties
    - Monitoring (Spring Boot Actuator)

---

### Spring Boot Starter Projects

- 애플리케이션을 빌드하려면 많은 feature들이 필요함
  - **Build a REST API** : Spring, Spring MVC, Tomcat, JSON conversion, ...
  - **Write Unit Tests** : Spring Test, Unit, Mockito, ...
- How can I group them and make it easy to build applications?
  - **Starters** : Convenient **dependency descriptors** for diff. features
- **Spring Boot** provides variety of starter projects :
  - **Web Application & REST API** - Spring Boot Starter Web (spring-webmvc, spring-web, spring-boot-starter-tomcat, spring-boot-starter-json)
  - **Unit Tests** - Spring Boot Starter Test
  - **Talk to database using JPA** - Spring Boot Starter Data JPA
  - **Talk to database using JDBC** - Spring Boot Starter JDBC
  - **Secure your web application or REST API** - Spring Boot Starter Security



---

### Spring Boot Auto Configuration

- I need **lot of configuration** to build Spring app :
  - ComponentScan, DispatcherServlet, Data Sources, JSON Conversion, ...
- How can I simplify this?
  - **Auto Configuration : Automated configuration** for your app
    - **Decide** based on :
      - Which frameworks are in the Class Path?
      - What is the existing configuration (Annotations etc)?
- **Example** : Spring Boot Starter Web
  - Dispatcher Servlet (`DispatcherServletAutoConfiguration`)
  - Embedded Servlet Container - Tomcat is the default
    (`EmbeddedWebServerFactoryCustomizerAutoConfiguration`)
  - Default Error Pages (`ErrorMvcAutoConfiguration`)
  - Bean <-> JSON (`JacksonHttpMessageConvertersConfiguration`)



---

### Spring Boot DevTools

- Increase developer productivity
- **Hot Reload**
- **Remember** : For pom.xml dependency changes, you will need to restart server manually

```xml
<dependency>
  <groupId>org.springframework.boot</groupId>
  <artifactId>spring-boot-devtools</artifactId>
</dependency>
```



---

### Managing App. Configuration using Profiles

- Applications have different environments: **Dev, QA, Stage, Prod, ...**
- Different environments need **different configuration** :
  - Different Databases
  - Different Web Services
- How can you provide different configuration for different environments?
  - **Profiles** : Environment specific configuration
- Level : `trace > debug > info > warning > error > off`

```properties
# application.properties

#spring.profiles.active=prod
spring.profiles.active=dev	->	profile 사용
```

```properties
# application-prod.properties -> profile-prod

logging.level.org.springframework=info
```

```properties
# application-dev.properties -> profile-dev

logging.level.org.springframework=trace
```



---

### Configuration Properties

- application.properties 파일에 숨겨놓을 때 사용 (ex. key)
- `@ConfigurationProperties(prefix = "사용할 이름")` 을 통해서 접근 가능
  - 해당 값 접근 시 Getter / Setter를 통해서만 접근 가능 (생성자 불가)

```java
// CurrencyConfigurationController.java

@RestController
public class CurrencyConfigurationController {
	
	@Autowired
	private CurrencyServiceConfiguration configuration;
	
	@RequestMapping("/currency-configuration")
	public CurrencyServiceConfiguration retrieve() {
		return configuration;
	}
  
  // 아래 JSON 파일 반환
  // {
  // 		"url"="http://default.in28minutes.com",
  // 		"username"="defaultusername",
  // 		"key"="defaultkey"
  // }
}
```

```java
// CurrencyServiceConfiguration.java

@ConfigurationProperties(prefix = "currency-service")
@Component
public class CurrencyServiceConfiguration {
	
	private String url;
	private String username;
	private String key;
	
	public String getUrl() {
		return url;
	}
	
	public void setUrl(String url) {
		this.url = url;
	}
	
	public String getUsername() {
		return username;
	}
	
	public void setUsername(String username) {
		this.username = username;
	}
	
	public String getKey() {
		return key;
	}
	
	public void setKey(String key) {
		this.key = key;
	}
}
```

```properties
# application.properties

logging.level.org.springframework=debug
spring.profiles.active=dev

currency-service.url=http://default.in28minutes.com
currency-service.username=defaultusername
currency-service.key=defaultkey
```

- 참고로 application-dev.properties 파일에서 currency-service 관련 로직을 오버라이딩 하지 않으면 상위 파일의 값이 그대로 사용됨!



---

### Spring Boot Embedded Servers

- How do you deploy your application before Spring Boot?
  - Step 1: Install Java
  - Step 2: Install Web/Application Server
    - Tomcat / WebSphere / WebLogic etc
  - Step 3: Deploy the application **WAR** (Web ARchive)
    - This is the old WAR Approach
    - Complex to setup!
- **Embedded Server** - Simpler alternative
  - Step 1: Install Java
  - Step 2: Run **JAR** file
    - **Make JAR not WAR** (Credit: Josh Long!)
  - Embedded Server **Examples** :
    - spring-boot-starter-tomcat
    - spring-boot-starter-jetty
    - spring-boot-starter-undertow



---

### Spring Boot Actuator (Monitor Applications)

- Provides a number of endpoints : 
  - **beans** - Complete list of Spring beans in your app
  - **health** - Application health information
  - **metrics** - Application metrics
  - **mappings** - Details around Request Mappings

```xml
<!-- pom.xml -->
<dependency>
  <groupId>org.springframework.boot</groupId>
  <artifactId>spring-boot-starter-actuator</artifactId>
</dependency>
```

```properties
management.endpoints.web.exposure.include=*
#management.endpoints.web.exposure.include=beans, health
```



---

### Spring vs Spring MVC vs Spring Boot

- **Spring Framework** : Only Dependency Injection
  - `@Component`, `@Autowired`, `@ComponentScan` etc
  - Just Dependency Injection is NOT sufficient (You need other frameworks to build apps)
    - **Spring Modules and Spring Projects** : Extend Spring Eco System
      - Provide good integration with other frameworks (Hibernate/JPA, Unit & Mockito for Unit Testing)
- **Spring MVC** (Spring Module) : Simplify building web apps and REST API
  - Building web applications with Struts was very complex
  - `@Controller`, `@RestController`, `@RequestMapping("address")`
- **Spring Boot** (Spring Project) : Build **PRODUCTION-READY** apps **QUICKLY**
  - **Starter Projects** - Make it easy to build variety of applications
  - **Auto configuration** - Eliminate configuration to setup Spring, Spring MVC and other frameworks(DispatcherServlet, JSON converter, etc)!
  - Enable non functional requirements (NFRs) :
    - **Actuator** : Enables Advanced Monitoring of applications
    - **Embedded Server** : No need for separate application servers!
    - Logging and Error Handling
    - Profiles and ConfigurationProperties

