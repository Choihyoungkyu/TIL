# Interface와 Type



## 공통점

- `interface`와 `type`은 객체의 이름과 타입을 지정하는 방법

```typescript
interface PeopleInterface {
  name: string;
  age: number;
}

const me1: PeopleInterface = {
  name: 'yc',
  age: 34,
}

type PeopleType = {
  name: string;
  age: number;
}

const me2: PeopleType = {
  name: 'yc',
  age: 31,
}
```



## 차이점

#### 확장하는 방법

```typescript
interface PeopleInterface {
  name: string;
  age: number;
}

interface StudentInterface extends PeopleInterface {
  school: string;
}
```

```typescript
type PeopleType = {
  name: string;
  age: number;
}

type StudentType = PeopleType & {
  school: string;
}
```



#### 선언적 확장

- `interface`에서 할 수 있는 대부분의 기능들은 `type`에서 가능
- 한 가지 중요한 차이점은 `type`은 새로운 속성을 추가하기 위해서 다시 같은 이름으로 선언 불가
- `interface`는 항상 선언적 확장이 가능

```typescript
interface Window {
  title: string;
}

interface Window {
  ts: TypeScriptAPI
}

// 같은 interface 명으로 Window를 다시 만든다면, 자동으로 확장이 됨

const src = 'const a = "Hello World"';
window.ts.transpileModule(src, {})
```

```typescript
type Window = {
  title: string;
}

type Window = {
  ts: TypeScriptAPI
}

// Error: Duplicate identifier 'Window'.
// 타입은 안된다.
```



#### interface는 객체에만 사용이 가능

```typescript
interface FooInterface {
  value: string;
}

type FooType = {
  value: string;
}

type FooOnlyString = string;
type FooTypeNumber = number;

// 불가능
interface X extends string {}
```



#### computed value의 사용

- `type`은 가능하지만 `interface`는 불가능

```typescript
type names = 'firstName' | 'lastName';

type NameTypes = {
  [key in names]: string;
}

const yc: NameTypes = { firstName: 'hi', laseName: 'yc' };

interface NameInterface {
  // error
  [key in names]: string;
}
```



#### 성능을 위해서는 interface 사용이 좋다

- `interface` 들을 합성할 경우 이는 캐시가 됨
- `type` 합성의 경우, 합성 자체에 대한 유효성을 판단하기 전에 모든 구성요소에 대한 타입을 체크하므로 컴파일 시에 상대적으로 성능이 좋지 않다



#### 참고 사이트

- https://yceffort.kr/2021/03/typescript-interface-vs-type