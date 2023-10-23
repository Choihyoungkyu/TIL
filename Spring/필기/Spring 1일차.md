# Spring 1일차

---

> start.spring.io : 스프링 프로젝트를 만들어주는 사이트

### Summary - Important Terminology

- **@Component(..)** : An instance of class will be managed by Spring framework
- **Dependency** : GameRunner needs GamingConsole implement!
  - GamingConsole Impl (Ex. MarioGame) is a dependency of GameRunner
- **Component Scan** : How does Spring Framework find component classes?
  - It scans **packages**! (`@ComponentScan("com.in28minutes")`)
- **Dependency Injection** : Identify beans, their dependencies and wire them together (provides **IOC** - Inversion of Control)
  - **Spring Beans** : An object managed by Spring Framework
  - **IoC container** : Manages the lifecycle of beans and dependencies
    - Types: ApplicationContext (complex), BeanFactory (simpler features - rarely used)
  - **Autowiring** : Process of wiring in dependencies for a Spring Bean



### Autowiring 과정

```java
class YourBusinessClass {
 	Dependency1 dependency1;
  
  Dependency2 dependency2;

  public YourBusinessClass(Dependency1 dependency1, Dependency2 dependency2) {
    super();
    System.out.println("Constructor Injection - YourBusinessClass");
    this.dependency1 = dependency1;
    this.dependency2 = dependency2;
  }
}
```

1. 생성자 안에 `Dependency1 dependency1, Dependency2 dependency2`가 있는 것을 보고 2개의 의존성이 필요하다는 것을 파악
2. 이것들을 찾아서 생성자 주입을 통해 자동 연결(Autowiring) 수행



---

### 결합(Coupling)

- 무언가를 변경하는 데 얼마나 많은 작업이 관련되어 있는지에 대한 측정



---

### Spring Bean

- Spring Bean은 Spring Framework가 관리하는 Java 객체
- Spring은 IOC Container(Bean Factory or Application Context)를 사용해 이러한 객체를 관리
- 즉, Spring에서 관리하는 객체들

```java
// HelloWorldConfiguration.java
@Configuration
public class HelloWorldConfiguration {
	
	@Bean
	public String name() {
		return "Ranga";
	}
}
```

```java
// App02HelloWorldSpring.java

// 1: Launch a Spring Context
// JVM 내에서 해당 Spring이 관리하는 컨테이너와 연결
var context = 
  new AnnotationConfigApplicationContext(HelloWorldConfiguration.class);

// 2: Configure the things that we want Spring to manage - 
// HelloWorldConfiguration - @Configuration
// name - @Bean
// @Bean 데코레이션을 통해 스프링빈을 생성 후 사용

// 3: Retrieving Beans managed by Spring
System.out.println(context.getBean("name"));
```

---

### record

- JDK 16에서 추가된 새로운 기능
- Spring Bean을 만드는 번거로움을 없애기 위해 도입된 기능
- `getter`, `setter`를 자동으로 생성해줌



---

### Bean 설정 방법

```java
record Person (String name, int age, Address address) {};
record Address (String firstLine, String city) {};

@Configuration
public class HelloWorldConfiguration {
  @Bean
  public String name() {
    return "Ranga";
  }
  
  @Bean
  public int age() {
    return 15;
  }
  
  // 하드 코딩으로 Person 객체 만들기
  @Bean
  public Person person() {
    var person = new Person("Ravi", 20, new Address("main street", "London"));
    return person;
  }
  
  // 메소드로 Person 객체 만들기
  @Bean
  public Person person2MethodCall() {
    return new Person(name(), age(), address());
  }
  
  // 파라미터로 Person 객체 만들기
  // 주의) Bean 이름을 파라미터로 설정해야됨
  // 한 개의 Spring Bean을 만드는 데 다른 기존의 Spring Bean을 사용
  @Bean
  public Person person3Parameters(String name, int age, Address address2) {
    return new Person(name, age, address2);
  }
  
  // 사용자 지정 이름 사용 가능!!
  @Bean(name = "address2")
  public Address address() {
    var address = new Address("sub street", "London");
    return address;
  }
}
```



---

### Spring Questions

- Q1: Spring Container vs Spring Context vs IOC Container vs Application Context
- Q2: POJO vs Java Bean vs Spring Bean
- Q3: How Can I list all beans managed by Spring Framework?
- Q4: What if multiple matching beans are available?
- Q5: Spring is managing objects and performing auto-wiring
  - But, aren't we writing the code to create objects?
  - How do we get Spring to create objects for us?



### Q1. Spring Container vs Spring Context vs IOC Container vs Application Context

- Spring Container (= Spring Context = Spring IOC Container)
  - Manages Spring Beans & their lifecycle
- 1 - Bean Factory : Basic Spring Container (거의 사용 X, 메모리 제약이 중요한 IoT 경우에만 사용)
- 2 - Application Context : Advanced Spring Container with enterprise-specific features
  - Easy to use in web applications
  - Easy internationalization(국제화)
  - Easy integration with Spring AOP
- Which one to use? : Most enterprise applications use Application Context
  - Recommanded for web applications, web services, REST API and microservices



### Q2. POJO vs Java Bean vs Spring Bean

- **POJO(Plain Old Java Object)**
  - No constraints
  - Any Java Object is a POJO! (모든 자바 객체는 POJO!)
- **Java Bean** : Classes adhering to 3 contraints
  - 1: Have public default (no argument) constructors
  - 2: Allow access to their properties using getter and setter methods
  - 3: Implements java.io.Serializable
- **Spring Bean** : Any Java object that is managed by Spring
  - Spring uses IOC Container (Bean Factory or Application Context) to manage these objects

```java
class Pojo {
  private String text;
  private int number;
  public String toString() {
    return text + ":" + number;
  }
}

              // 3: implements Serializable
class JavaBean implements Serializable {	// EJB(Enterprise Java Bean)
  // 1: public no-arg contructor
  public JavaBean() {}
  
  private String text;
  
  // 2: getters and setters
  public String getText() {
    return text;
  }
  
  public void setText(String text) {
    this.text = text;
  }
}
```



### Q3. How can I list all beans managed by Spring Framework?

(Spring이 관리하는 Bean을 모두 나열하려면 어떻게 할까요?)

- `getBeanDefinitionNames()` 메소드 사용

```java
var context = new AnnotationConfigApplicationContext(HelloWorldConfiguration.class);

Arrays.stream(context.getBeanDefinitionNames()).forEach(System.out::println);
// helloWorldConfiguration
// name
// ...
// address3
```



### Q4. What if multiple matching beans are available?

- `@Primary` 를 사용해 우선순위를 부여하는 방법
- `@Qualifier("원하는 이름")` 를 사용해 결정자를 부여하는 방법

```java
// HelloWorldConfiguration.java
@Bean
public Person person5Qualifier(String name, int age, @Qualifier("address3qualifier") Address address3) {
  return new Person(name, age, address3);	// name, age, address
}

@Bean(name = "address3")
@Qualifier("address3qualifier")
public Address address3() {
  var address = new Address("Main Street", "London");
  return address;
}

// ---------------
// App02HelloWorldSpring.java
var context = new AnnotationConfigApplicationContext(HelloWorldConfiguration.class);

System.out.println(context.getBean("person5Qualifier"));
```



**`@Primary` vs `@Qualifier` - Which one to use?**

```java 
@Component @Primary
class QuickSort implements SortingAlgorithm {}

@Component
class BubbleSort implements SortingAlgorithm {}

@Component @Qualifier("RadixSortQualifier")
class RadixSort implements SortingAlgorithm {}

@Component
class ComplexAlgorithm
    @Autowired
    private SortingAlgorithm algorithm;

@Component
class AnotherComplexAlgorithm
  	@Autowired @Qualifier("RadixSortQualifier")
  	// @Autowired @Qualifier("RadixSort")  -->  (Qualifier가 없을 경우 Bean 이름으로 연결 가능)
  	private SortingAlgorithm iWantToUseRadixSortOnly;
```

- `@Primary` - A bean should be given preference when multiple candidates are qualified
- `@Qualifier` - A specific bean should be auto-wired (name of the bean can be used as qualifier)
- **ALWAYS** think from the perspective of the class using the SortingAlgorithm:
  - 1: **Just @Autowired**: Give me (preffered) SortingAlgorithm
  - 2: **@Autowired + @Qualifier**: I only want to use specific SortingAlgorithm - RadixSort
  - (REMEMBER) `@Qualifier` has higher priority then `@Primary`



### Q5. Spring is managing objects and performing auto-wiring

- `@Component`를 통해 스프링이 자동으로 Bean을 만들게 할 수 있음
- `@ComponentScan(패키지명)`을 통해 해당 패키지 내의 Bean들을 자동으로 연결시켜줌
- `@Component(..)` : An instance of class will be managed by Spring framework

```java
// App03GamingSpringBeans.java
@Configuration
@ComponentScan("com.in28minutes.learnspringframework.game")
public class App03GamingSpringBeans {

	public static void main(String[] args) {
		
		try (var context = 
				new AnnotationConfigApplicationContext
					(App03GamingSpringBeans.class)) {
			
			context.getBean(GamingConsole.class).up();
			
			context.getBean(GameRunner.class).run();
		}
	}
}

// ----------------
// GameRunner.java
@Component
public class GameRunner {
   private GamingConsole game;

   public GameRunner(GamingConsole game) {
      this.game = game;
   }

   public void run() {
      System.out.println("Running game: " + String.valueOf(this.game));
      this.game.up();
      this.game.down();
      this.game.left();
      this.game.right();
   }
}

// ----------------
// PacmanGame.java
@Component
@Primary
public class PacmanGame implements GamingConsole {
   public PacmanGame() {
   }

   public void up() {
      System.out.println("up");
   }

   public void down() {
      System.out.println("down");
   }

   public void left() {
      System.out.println("left");
   }

   public void right() {
      System.out.println("right");
   }
}
```



---

### 의존성 주입(Dependency Injection)

**Types**

- **Constructor-based** : Dependencies are set by creating the Bean using its Constructor
- **Setter-based** : Dependencies are set by calling setter methods on your beans
- **Field** : No setter or constructor. Dependency is injected using reflection.
- Question : **Which one should you use?**
  - Spring team recommands **Constructor-based injection** as dependencies are automatically set when an object is created!
  - 모든 초기화가 하나의 메소드에서 발생하기 때문에 생성자 기반 주입을 추천함!
  - 초기화가 완료되면 Bean을 사용할 준비가 끝났다는 말

```java
@Component
class YourBusinessClass {
  // 방법 1: Field
  @Autowired
	Dependency1 dependency1;
	
  @Autowired
	Dependency2 dependency2;
	
  // 방법 2: Setter-based
	@Autowired
	public void setDependency1(Dependency1 dependency1) {
		this.dependency1 = dependency1;
		System.out.println("Setter Injection - setDependency1");
	}

	@Autowired
	public void setDependency2(Dependency2 dependency2) {
		this.dependency2 = dependency2;
		System.out.println("Setter Injection - setDependency2");
	}

  // 방법 3: Constructor-based
	// @Autowired	// 없애도 됨
	public YourBusinessClass(Dependency1 dependency1, Dependency2 dependency2) {
		super();
		System.out.println("Constructor Injection - YourBusinessClass");
		this.dependency1 = dependency1;
		this.dependency2 = dependency2;
	}

	public String toString() {
		return "Using " + dependency1 + " and " + dependency2;
	}
}
```



---

### @Component vs @Bean

| Heading            | @Component                                                   | @Bean                                                        |
| ------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| Where?             | Can be used on any Java class                                | Typically used on methods in Spring Configuration classes    |
| Ease of use        | Very easy. Just add an annotation                            | You write all the code                                       |
| Autowiring         | Yes - Field, Setter or Constructor Injection                 | Yes - method call or method parameters                       |
| Who creates beans? | Spring Framework                                             | You write bean creation code                                 |
| Recommended For    | Instantiating Beans for Your Own Application Code: `@Component` | 1: Custom Business Logic<br />2: Instantiating Beans for 3rd-party libraries: `@Bean` (ex. spring security) |



---

### Why do we have a lot of Dependencies?

- In **Game Runner** Hello World App, we have very few classes
- But, **Real World** applications are much more complex:
  - Multiple Layers (Web, Business, Data etc)
  - Each layer is **dependent** on the layer below it!
    - ex) Business Layer class talks to a Data Layer class ==> Data Layer class is a dependency of Business Layer class
    - There are thousands of such dependencies in every application!
- With Spring Framework:
  - Instead of Focusing on objects, their dependencies and wiring
    - You can focus on the business logic of your application!
  - **Spring Framework manages the lifecycle** of objects:
    - Mark components using annotations: `@Component` (and others..)
    - Mark dependencies using `@Autowired`
    - Allow Spring Framework to do its magic!
  - 즉, 스프링 프레임워크는 객체를 생성, 의존성을 자동 연결 등 전체 시스템의 준비를 갖춰줌

