# NestJS



#### 비즈니스 로직과 서비스 로직을 분리

Controller : URL을 가져오는 역할 (function을 실행하는 정도의 역할)

Service : 비즈니스 로직 담당 (실제로 function을 가지는 부분)



#### DTO (Data Transfer Object, 데이터 전송 객체)

```typescript
// create-movie.dto.ts
export class CreateMovieDto {
  readonly title: string;
  readonly year: number;
  readonly genres: string[];
}
```



#### DTO 유효성 검사

- [**class-validator**](https://github.com/typestack/class-validator)

```typescript
// main.ts
async function bootstrap() {
  const app = await NestFactory.create(AppModule);
  // 파이프 : 데이터 통로 (유효성 검사)
  app.useGlobalPipes(
  	new ValidationPipe({
      // 어떠한 decorator도 없는 어떠한 property의 object를 거름
      whitelist: true,
      // Dto에 없는 property를 거름
      forbidNonWhitelisted: true,
      // Dto에 맞는 타입으로 변환해줌 => 엄청난 기능
      transform: true,
    }),
  );
  await app.listen(3000);
}
bootstrap();
```



```
// class의 유효성 검사
npm i class-validator class-transformer
```

```typescript
// create-movie.dto.ts
import { IsString, IsNumber } from 'class-validator';

export class CreateMovieDto {
  @IsString()
  readonly title: string;

  @IsNumber()
  readonly year: number;

  @IsString({ each: true })
  readonly genres: string[];
}
```



#### mapped-types

- 타입을 변환시키고 사용할 수 있게 하는 패키지

```
npm i @nestjs/mapped-types
```

```typescript
// 기존 코드
import { IsString, IsNumber } from 'class-validator';

export class UpdateMovieDto {
  @IsString()
  readonly title?: string;

  @IsNumber()
  readonly year?: number;

  @IsOptional()
  @IsString({ each: true })
  readonly genres?: string[];
}

// mapped-types 코드
import { PartialType } from '@nestjs/mapped-types';
import { CreateMovieDto } from './create-movie.dto';

export class UpdateMovieDto extends PartialType(CreateMovieDto) {}
```



#### Dependency Injection (의존성 주입)

- `controller`에서 `this.movieService`라는 property를 만들고 타입을 지정해줘서 사용 가능
  - typescript가 아니었다면 뭔가를 import 해줘야됨
- `movies.module`에서 `providers: [MovieService]`를 함으로써 `MovieService`를 import 하고 `Controller`에 injection(주입) 하기 때문에 타입만 지정해줘도 사용 가능
- `MovieService`에`Injectable`이라는 decorator로 의존성 주입

```
MoviesController는 MoviesService를 필요로 하고, 이를 의존성 주입으로 제공하고 있음

  =>  알아서 필요한 것들을 import
```



#### NestJS

- 두개의 프레임워크 위에서 동작
  - Express
    - 기본적으로는 Express 위에서 동작
  - Fastify
    - Express보다 2배 정도 빠름
    - NestJS가 알아서 Express와 Fastify 사이를 전환
- 플랫폼이나 어플리케이션에 Req, Res 같은 decorator를 이용해 Express에 접근 가능
  - 하지만 Fastify와는 연동이 안되기 때문에 추천하지 않음



#### 테스트

- **유닛 테스팅**

  ```
  npm run test:cov
  ```

  - 모든 function을 따로 테스트
  - 서비스에서 분리된 유닛을 테스트
  - ex) `getAll()` function 하나만 테스트하고 싶을 때 사용
  - `~~.spec.ts` 파일은 전부 유닛 테스트용 파일
  - `afterAll()` 함수의 경우 데이터베이스를 정리해주는 (모두 지우는) function을 넣을 수 있음
  - `beforeEach, afterEach, beforeAll, afterAll` 등 여러 Hook이 존재

- **end-to-end (e2e) 테스트**

  ```
  npm run test:e2e
  ```

  - 모든 시스템을 테스팅
  - ex) 이 페이지로 가면 특정 페이지가 나와야하는 경우 사용 => 사용자 스토리(=관점) 같은 느낌
    - = 사용자가 특정 링크를 클릭하면 이 링크를 볼 수 있어야 하는 걸 테스트
    - = 사용자가 취할만한 액션들을 처음부터 끝까지 테스트
  - test 폴더가 있어야 `e2e` 테스트 가능