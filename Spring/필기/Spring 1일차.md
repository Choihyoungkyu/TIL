# Spring 1일차

---

> start.spring.io : 스프링 프로젝트를 만들어주는 사이트



### 결합(Coupling)

- 무언가를 변경하는 데 얼마나 많은 작업이 관련되어 있는지에 대한 측정



### Spring Bean

- Spring에서 관리하는 것들

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

