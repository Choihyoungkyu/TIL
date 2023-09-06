### Interface

- **순수 타입스크립트의 기능으로 컴파일되지 않음**
- 객체의 구조를 설명하기 위해서만 사용
- 주로 구체적인 구현이 아닌 서로 다른 클래스 간의 기능을 공유하기 위해 사용됨



#### Interface와 추상 클래스의 차이점

- 추상 클래스는 추가적으로 구현해야하는 부분과 구체적 구현 부분을 따로 설정할 수 있음
- Interface는 세부 설정을 못하고 전부 다 추가적으로 구현해야됨

```typescript
interface Greetable {
  name: string;

  greet(phrase: string): void;
}

class Person implements Greetable {
  name: string;

  constructor(n: string) {
    this.name = n;
  }

  greet(phrase: string) {
    console.log(phrase + " " + this.name);
  }
}

// let user1: Greetable;
// user1 = {
//   name: "Max",
//   greet(phrase: string) {
//     console.log(phrase + " " + this.name);
//   },
// };

const user1: Greetable = new Person("Max"); // Greetable 타입에 Person 객체 할당 가능
user1.greet("Hi there -");
```



#### `readonly`

- 모든 객체의 속성이 한 번만 설정되어야 하며 이후에는 읽기 전용으로 설정하여 객체가 초기화되면 변경할 수 없도록 할 수 있음

```typescript
interface Greetable {
  readonly name: string;
  
  greet(phrase: string): void;
}
```



#### Interface 확장

- `extends` 키워드로 확장 가능 (상속 느낌)
  - `class`랑 다른 점은 여러 개를 상속받을 수 있음

```typescript
interface Named {
  readonly name: string;
}

interface Greetable {
  greet(phrase: string): void;
}

class Person implements Greetable, Named {
  name: string;
  age = 30;
  
  constructor(n: string) {
    this.name = n;
  }
}
```

```typescript
interface Named {
  readonly name: string;
}

interface Greetable extends Named {
  greet(phrase: string): void;
}

class Person implements Greetable {
  name: string;
  age = 30;
  
  constructor(n: string) {
    this.name = n;
  }
}
```



#### 함수 Interface

```typescript
// type AddFn = (a: number, b: number) => number; // 아래랑 같음
interface AddFn {
  (a: number, b: number): number;
}

let add: AddFn;

add = (n1: number, n2: number) => {
  return n1 + n2;
};
```



#### `?`

- optional 키워드

```typescript
interface Named {
  readonly name?: string;
}

interface Greetable extends Named {
  greet(phrase: string): void;
}

class Person implements Greetable {
  name?: string;
  age = 30;

  constructor(n: string) {
    if (n) {
      this.name = n;
    }
  }

  greet(phrase: string): void {
    console.log(phrase + " " + this.name);
  }
}

```

