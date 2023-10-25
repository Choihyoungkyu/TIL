# Spring 2일차

---



### Lazy Initialization(지연 초기화)

- 기본적으로 스프링은 즉시 초기화를 사용 -> 시작할 때 즉시 초기화됨
- `@Lazy` 를 사용해 Bean이 사용될 때 초기화를 진행할 수 있음
  - `@Component`를 사용하는 모든 클래스나 Bean에 어노테이션을 적용한 모든 메서드에서 `@Lazy`를 사용 가능
  - `@Configuration` 클래스에 `@Lazy`를 적용하면 해당 클래스 내의 모든 Bean 메서드가 지연 초기화됨
- 지연 초기화 사용을 추천하지는 않음
  - 이유 : 애플리케이션이 시작될 때 Spring 구성 오류가 발견되지 않음 -> 런타임시 발견되어 런타임 에러가 발생
  - 자주 사용되지 않는 것에만 지연 초기화를 사용하는 것이 좋음!

| Heading                                           | Lazy Initialization                                          | Eager Initialization                             |
| ------------------------------------------------- | ------------------------------------------------------------ | ------------------------------------------------ |
| Initialization time                               | Bean initialized when it is first made use of in the application | Bean initialized at startup of the application   |
| Default                                           | NOT Default                                                  | Default                                          |
| Code Snippet                                      | `@Lazy` or `@Lazy(value=true)`                               | `@Lazy(value=false)` or (Absence of `@Lazy`)     |
| What happens if there are errors in initializing? | Errors will result in runtime exceptions                     | Errors will prevent application from starting up |
| Usage                                             | Rarely used                                                  | Very frequently used                             |
| Memory Consumption                                | Less (until bean is initialized)                             | All beans are initialized at startup             |
| Recommended Scenario                              | Beans very rarely used in your app                           | Most of your beans                               |

---



### Spring Bean Scope

- Spring Beans are defined to be used in a specific scope:
  - **Singleton** - One object instance per Spring IoC container
  - **Prototype** - Possibly many object instances per Spring IoC container
  - Scopes applicable ONLY for web-aware Spring ApplicationContext (웹 관련 어플리케이션에서만 사용가능한 것들)
    - **Request** - One object instance per single HTTP request
    - **Session** - One object instance per user HTTP Session
    - **Application** - One object instance per web application runtime
    - **WebSocket** - One object instance per WebSocket instance
- Java Singleton (GOF) vs Spring Singleton
  - **Java Singleton (GOF)** - One object instance per JVM
  - **Spring Singleton** - One object instance per Spring IoC container
  - 보통 JVM 내에 한 개의 IoC container를 만들기 때문에 99.99%의 확률로 둘이 똑같음

```java
@Component
class NormalClass {
}

@Scope(value=ConfigurableBeanFactory.SCOPE_PROTOTYPE)
@Component
class PrototypeClass {
}

@Configuration
@ComponentScan
public class BeanScopesLauncherApplication {
	public static void main(String[] args) {
		try (var context = 
				new AnnotationConfigApplicationContext
					(BeanScopesLauncherApplication.class)) {
			
			System.out.println(context.getBean(NormalClass.class));	// NormalClass@7c1e2a9e
      System.out.println(context.getBean(NormalClass.class));	// NormalClass@7c1e2a9e
			
			System.out.println(context.getBean(PrototypeClass.class));	// PrototypeClass@fa36558
      System.out.println(context.getBean(PrototypeClass.class));	// PrototypeClass@672872e1
		}
	}
}

```

- 기본적으로 Spring Framework에서 생성되는 모든 Bean은 싱글톤(Singleton)임
- `@Scope(value=ConfigurableBeanFactory.SCOPE_PROTOTYPE)`을 통해서 프로토타입으로 만들 수 있음
  - 프로토타입 : Bean을 참조할 때마다 매번 다른 인스턴스 생성

| Heading              | Prototype                                                    | Singleton                                                    |
| -------------------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| Instances            | Possibly Many per Spring IoC Container                       | One per Spring IoC Container                                 |
| Beans                | New bean instance created every time the bean is referred to | Same bean instance reused                                    |
| Default              | NOT Default                                                  | Default                                                      |
| Code Snippet         | `@Scope(value=ConfigurableBeanFactory.SCOPE_PROTOTYPE`)      | `@Scope(value=ConfigurableBeanFactory.SCOPE_SINGLETON`)<br />or<br />Default |
| Usage                | Rarely used                                                  | Very frequently used                                         |
| Recommended Scenario | Stateful beans                                               | Stateless beans                                              |



---

### @PostConstruct, @PreDestroy

- `@PostConstruct` - 의존성을 연결하는 대로 초기화 논리를 실행할 때 사용
  - ex) 데이터베이스 등에서 데이터를 가져오려는 경우 사용
- `@PreDestroy` - 컨테이너에서 Bean이 삭제되기 전에(=애플리케이션 컨텍스트에서 삭제되기 전에) cleanup 논리를 수행하려는 경우 사용
  - ex) 데이터베이스 등의 활성화된 연결을 닫을 경우 사용

```java
@Component
class SomeClass {
	private SomeDependency someDependency;
	
	public SomeClass(SomeDependency someDependency) {
		super();
		this.someDependency = someDependency;
		System.out.println("All dependencies are ready!");
	}
	
	@PostConstruct	// 의존성이 연결된 후 초기화 실행
	public void initialize() {
		someDependency.getReady();
	}
	
	@PreDestroy		// Bean이 삭제되기 전에 cleanup 실행
	public void cleanup() {
		System.out.println("Cleanup");
	}
}

@Component
class SomeDependency {
	public void getReady() {
		System.out.println("some logic using SomeDependency");
	}
}

@Configuration
@ComponentScan
public class PrePostAnnotationsContextLauncherApplication {
	public static void main(String[] args) {
		try (var context = 
				new AnnotationConfigApplicationContext
					(PrePostAnnotationsContextLauncherApplication.class)) {
			
			Arrays.stream(context.getBeanDefinitionNames())
				.forEach(System.out::println);
		}
	}
}
```





---

### Evolution of Jakarta EE: vs J2EE vs Java EE

- Enterprise capabilities were **initially built into JDK**
- With time, they were separated out:
  - **J2EE** - Java 2 Platform Enterprise Edition
  - **Java EE** - Java Platform Enterprise Edition (Rebranding)
  - **Jakarta EE** - Oracle gave Java EE rights to the Eclipse Foundation
    - **Important Specifications**:
      - Jakarta Server Pages (JSP, =Java Server Pages)
      - Jakarta Standard Tag Library (JSTL) - 웹 페이지에 동적 정보를 나타내는 데 사용할 수 있는 태그 라이브러리
      - Jakarta Enterprise Beans (EJB)
      - Jakarta RESTful Web Services (JAX-RS)
      - Jakarta Bean Validation
      - Jakarta Contexts and Dependency Injection (CDI) - 의존성 주입 방법과 관련된 규격
      - Jakarta Persistence API (JPA) - 관계형 데이터베이스와 상호작용하는 방법을 다룸
    - Supported by **Spring 6 and Spring Boot 3**
      - That's why we use Jakarta.packages (instead of javax.)
- 결국, J2EE, Java EE, Jakarta EE는 규격 그룹을 나타내는 것이고, 3개는 같음



---

### Jakarta Contexts & Dependency Injection (CDI)

- Spring Framework V1 was released in 2004
- **CDI specification**(CDI 규격) introduced into Java EE 6 platform in December 2009
- Now called **Jakarta Contexts and Dependency Injection (CDI)**
- CDI is a **specification (interface)**
  - Spring Framework **implements** CDI
- **Important** Injection API Annotations:
  - Inject (@Autowired in Spring)
  - Named (@Component in Spring)
  - Qualifier
  - Scope
  - Singleton
- CDI Annotation으로 Spring Annotation을 대체할 수 있음
  - `@Named` = `@Component`
  - `Inject` = `@Autowired`

```java
//@Component
@Named
class BusinessService {
	DataService dataService;

	public DataService getDataService() {
		return dataService;
	}

//	@Autowired
	@Inject
	public void setDataService(DataService dataService) {
		System.out.println("Setter Injection");
		this.dataService = dataService;
	}
}
```



---

### Java Spring XML

- `ClassPathXmlApplicationContext("xml 파일")` 을 통해 xml 설정을 불러올 수 있음
- 이후 사용은 Java Bean과 똑같음

```java
try (var context = new ClassPathXmlApplicationContext("contextConfiguration.xml")) {
  Arrays.stream(context.getBeanDefinitionNames())
				.forEach(System.out::println);
}
```

- Xml 설정 파일

```xml
<?xml version="1.0" encoding="UTF-8"?>
<beans xmlns="http://www.springframework.org/schema/beans"
    xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
    xmlns:context="http://www.springframework.org/schema/context" xsi:schemaLocation="
        http://www.springframework.org/schema/beans http://www.springframework.org/schema/beans/spring-beans.xsd
        http://www.springframework.org/schema/context http://www.springframework.org/schema/context/spring-context.xsd">
	
  <!-- Bean 생성 --> 
	<bean id="name" class="java.lang.String">
		<constructor-arg value="Ranga" />
	</bean>
	
  <!-- Bean 생성 --> 
	<bean id="age" class="java.lang.Integer">
		<constructor-arg value="35" />
	</bean>
	
  <!-- componentScan --> 
	<context:component-scan base-package="com.in28minutes.learnspringframework.game" />
 	 
  <!-- Bean 불러오기 --> 
 	 <bean id="game" 
 	 	class="com.in28minutes.learnspringframework.game.PacmanGame" />
 	 
  <!-- Bean 불러오면서 생성자 주입하기 --> 
 	 <bean id="gameRunner" 
 	 	class="com.in28minutes.learnspringframework.game.GameRunner">
 	 	<constructor-arg ref="game" />
 	</bean>
  
</beans>
```

| Heading              | Annotations                                                  | XML Configuration           |
| -------------------- | ------------------------------------------------------------ | --------------------------- |
| Ease of use          | Very Easy (defined close to source - class, method and/or variable) | Cumbersome(장황함)          |
| Short and concise    | Yes                                                          | No                          |
| Clean POJOs          | No. POJOs are polluted with Spring Annotations               | Yes. No change in Java code |
| Easy to Maintain     | Yes                                                          | No                          |
| Usage Frequency      | Almost all recent projects                                   | Rarely                      |
| Recommendation       | Either of them is fine, But be consistent                    | Do NOT mix both             |
| Debugging difficulty | Hard                                                         | Medium                      |



---

