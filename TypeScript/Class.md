# TypeScript

---

### Public, Private, Protected

|      | Public  | Private              | Protected                       |
| ---- | ------- | -------------------- | ------------------------------- |
| 범위 | 모든 곳 | 해당 클래스 안에서만 | 해당 클래스의 확장까지(상속 등) |

---

### Class

#### 기본형

```typescript
class Department {
  private employees: string[] = [];		// 기본값으로 빈 배열
  private readonly id: string;
  private name: string;
  
  // 생성자
  constructor(id: string, name: string) {
    this.id = id;
    this.name = name;
  }
}

const department = new Department("d1", "Accounting");
```



#### 축약형

```typescript
class Department {
  private employees: string[] = [];		// 기본값으로 빈 배열
  
  // 생성자
  constructor(private readonly id: string, private name: string) {}
}

const department = new Department("d1", "Accounting");
```

---

### Class 상속

```typescript
class ITDepartment extends Department {
	constructor(id: string, private admins: string[]) {
    super(id, "IT");
  }
}

const IT = new ITDepartment("d2", ["Max"]);
```

---

### Getter, Setter

- 로직을 캡슐화하고 속성을 읽거나 설정하려 할 때 실행되어야 하는 추가적인 로직을 추가하는데 유용

```typescript
class AccountingDepartment extends Department {
  private lastReport: string;
  
  // getter
  get mostRecentReport() {
    if (this.lastReport) {
      return this.lastReport
    }
    throw new Error('No report found.');
  }
  
  // setter
  set mostRecentReport(value: string) {
    if (!value) {
      throw new Error('Please pass in a valid value!');
    }
    this.addReport(value);
  }
  
  constructor(id: string, private reports: string[]) {
    super(id, 'Accounting');
    this.lastReport = reports[0];
  }
  
  addReport(text: string) {
    this.reports.push(text);
    this.lastReport = text;
  }
}

const accounting = new AccountingDepartment('d3', []);
// setter 사용 -> 메서드처럼 사용하는 것이 아니라 아래처럼 사용해야함!!!!
accounting.mostRecentReport = 'Year End Report'

// getter 사용 -> 메서드처럼 호출하는 것이 아니라 () 없이 사용해야됨!!!!
console.log(accounting.mostRecentReport)	// 'Year End Report'
```

