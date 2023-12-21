# Spring 9일차 - 

---



### CORS (Cross-Origin Resource Sharing)

- In Eclipse, `command + shift + T` -> typing `WMC` -> `WebMvcConfigurer.class`

```java
import org.springframework.web.servlet.config.annotation.WebMvcConfigurer

public class Application {
  public static void main(String[] args) {
    SpringApplication.run(Application.class, args);
  }

  @Bean
  public WebMvcConfigurer corsConfigurer() {
    return new WebMvcConfigurer() {
      void addCorsMappings(CorsRegistry registry) {
        registry.addMapping("/**")
          .allowedMethods("*")
          .allowedOrigins("http://localhost:3000");
      }
    };
  }
}
```

