# Decorator

---

```json
// tsconfig.json
{
  "target": "es6",
  "experimentalDecorators": true
}
```

- 데코레이터는 함수다
- 데코레이터는 실체화되기 전 클래스가 정의만 돼도 실행됨
  - 즉, 클래스 및 `constructor` 함수가 실체화되지 않고 정의만 입력되면 데코레이터가 실행됨
- **데코레이터는 메타프로그래밍에 사용되어 추가적인 구성과 추가적인 로직을 더해 코드를 실행함**

```typescript
function Logger(constructor: Function) {
  console.log("Logging...");
  console.log(constructor);
}

@Logger
class Person {
  name = "Max";

  constructor() {
    console.log("Creating person object...");
  }
}

const pers = new Person();

console.log(pers);

// Logging...
// class Person {
//     constructor() {
//         this.name = "Max";
//         console.log("Creating person object...");
//     }
// }
// Creating person object...
// Person {name: 'Max'}
```

---

### 데코레이터 팩토리 생성

- 데코레이터 함수와 같은 걸 반환해 줄 함수를 만들어

```typescript
function Logger(logString: string) {
  return function (constructor: Function) {
    console.log(logString);
    console.log(constructor);
  };
}

@Logger("LOGGING - PERSON")
class Person {
  name = "Max";

  constructor() {
    console.log("Creating person object...");
  }
}
```

---

### 여러 데코레이터 추가하기

- **데코레이터 팩토리는 먼저 호출된 것부터 실행됨!**
  - 자바스크립트는 위에서 아래로 읽어나가기 때문
- **데코레이터는 아래에 있는 것부터 실행됨!**
  - 즉, 아래 예시에서는 `WithTemplate` > `Logger` 순으로 실행됨

```typescript
function Logger(logString: string) {
  console.log("LOGGER FACTORY");
  return function (constructor: Function) {
    console.log("LOGGER FUNCTION");
  };
}

function Damm() {
  console.log("DAMM FACTORY");
  return function (_: Function) {
    console.log("DAMM FUNCTION");
  };
}

function WithTemplate(template: string, hookId: string) {
  console.log("TEMPLATE FACTORY");
  return function (_: Function) {
    console.log("TEMPLATE FUNCTION");
    const hookEl = document.getElementById(hookId);
    if (hookEl) {
      hookEl.innerHTML = template;
    }
  };
}

@Damm()
@Logger("LOGGING - PERSON")
@WithTemplate("<h1>My Person Object</h1>", "app")
class Person {
  name = "Max";

  constructor() {
    console.log("Creating person object...");
  }
}

// DAMM FACTORY
// LOGGER FACTORY
// TEMPLATE FACTORY

// TEMPLATE FUNCTION
// LOGGER FUNCTION
// DAMM FUNCTION
```

---

### Property, Access, Method, Parameter 데코레이터

- 자바스크립트가 처음에 코드를 읽을 때 데코레이터도 같이 실행됨
- 즉, 이벤트리스너처럼 동작하는 것이 아니라 정의될 때 실행됨

```typescript
// 속성 데코레이터
function Log(target: any, propertyName: string | Symbol) {
  console.log("Property decorator!");
  console.log(target, propertyName);
}

// 접근 데코레이터
function Log2(target: any, name: string, descriptor: PropertyDescriptor) {
  console.log("Accessor decorator!");
  console.log(target);
  console.log(name);
  console.log(descriptor);
}

// 메소드 데코레이터
function Log3(
  target: any,
  name: string | Symbol,
  descriptor: PropertyDescriptor
) {
  console.log("Method decorator!");
  console.log(target);
  console.log(name);
  console.log(descriptor);
}

// 파라미터 데코레이터
function Log4(target: any, name: string | Symbol, position: number) {
  console.log("Parameter decorator!");
  console.log(target);
  console.log(name);
  console.log(position);
}

class Product {
  // 속성 데코레이터
  @Log
  title: string;
  private _price: number;

  // 접근 데코레이터
  @Log2
  set price(val: number) {
    if (val > 0) {
      this._price = val;
    } else {
      throw new Error("Invalid price - should be positive!");
    }
  }

  constructor(t: string, p: number) {
    this.title = t;
    this._price = p;
  }

  // 메소드 데코레이터
  @Log3
  getPriceWithTax(@Log4 tax: number) {	// 파라미터 데코레이터
    return this._price * (1 + tax);
  }
}
```

---

### 클래스 데코레이터에서 클래스 반환 및 변경

- 주의사항 : Person 객체를 만들지 않으면 custom한 constructor가 실행되지 않아 렌더링이 안됨!

```typescript
function WithTemplate(template: string, hookId: string) {
  return function <T extends { new (...args: any[]): { name: string } }>(
    originalConstructor: T
  ) {
    return class extends originalConstructor {
      constructor(..._: any[]) {
        super();
        const hookEl = document.getElementById(hookId);
        if (hookEl) {
          hookEl.innerHTML = template;
          hookEl.querySelector("h1")!.textContent = this.name;
        }
      }
    };
  };
}

@WithTemplate("<h1>My Person Object</h1>", "app")
class Person {
  name = "Max";

  constructor() {
    console.log("Creating person object...");
  }
}

const pers = new Person();

console.log(pers);
```

---

### Autobind

- 데코레이터를 통해 클래스의 메서드 내의 `this`를 항상 해당 클래스로 자동 바인딩 가능

```typescript
function Autobind(_: any, _2: string, descriptor: PropertyDescriptor) {
  const originalMethod = descriptor.value;
  const adjDescriptor: PropertyDescriptor = {
    configurable: true,
    enumerable: false,
    get() {
      // getter에서 propertyDescriptor의 객체로 바인딩을 해줘야됨!!
      const boundFn = originalMethod.bind(this);
      return boundFn;
    },
  };
  return adjDescriptor;
}

class Printer {
  message = "This works!";

  @Autobind		// 자동 바인딩
  showMessage() {
    console.log(this.message);
  }
}

const p = new Printer();

const button = document.querySelector("button");
button?.addEventListener("click", p.showMessage);
```

---

### 유효성 검사

- 데코레이터를 활용해 유효성 검사를 할 수 있음

```typescript
interface ValidatorConfig {
  [property: string]: {
    [validatableProp: string]: string[]; // ['required', 'positive']
  };
}

const registeredValidators: ValidatorConfig = {};

// 참고: constructor는 해당 클래스의 이름을 항상 가지고 있음! - 여기서는 Course
function Required(target: any, propName: string) {
  registeredValidators[target.constructor.name] = {
    ...registeredValidators[target.constructor.name],
    [propName]: [
      ...(registeredValidators[target.constructor.name]?.[propName] ?? []),
      "required",
    ],
  };
}

function PositiveNumber(target: any, propName: string) {
  registeredValidators[target.constructor.name] = {
    ...registeredValidators[target.constructor.name],
    [propName]: [
      ...(registeredValidators[target.constructor.name]?.[propName] ?? []),
      "positive",
    ],
  };
}

function validate(obj: any) {
  const objValidatorConfig = registeredValidators[obj.constructor.name];
  if (!objValidatorConfig) {
    return true;
  }

  let isValid = true;

  for (const prop in objValidatorConfig) {
    for (const validator of objValidatorConfig[prop]) {
      switch (validator) {
        case "required":
          // !!는 해당 값을 true or false로 바꿔줌
          isValid = isValid && !!obj[prop];
          break;
        case "positive":
          isValid = isValid && obj[prop] > 0;
          break;
      }
    }
  }
  return isValid;
}

// ---

class Course {
  @Required
  title: string;
  @PositiveNumber
  price: number;

  constructor(t: string, p: number) {
    this.title = t;
    this.price = p;
  }
}

const courseForm = document.querySelector("form")!;
courseForm.addEventListener("submit", (event) => {
  event.preventDefault();
  const titleEl = document.getElementById("title") as HTMLInputElement;
  const priceEl = document.getElementById("price") as HTMLInputElement;

  const title = titleEl.value;
  const price = +priceEl.value;

  const createdCourse = new Course(title, price);
  if (!validate(createdCourse)) {
    alert("Invalid input, please try again!");
    return;
  }
  console.log(createdCourse);
});
```

