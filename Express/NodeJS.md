# NodeJS

### 기본 구조

```javascript
const express = require('express');
const app = express();

app.listen();
```

```javascript
// port 연결
app.listen(port, () => {
  console.log(`listening on port ${port}`);
})
```

```javascript
// HTTP 메서드, 라우팅, 콜백 함수
app.get('/', (req, res) => {
  res.send('Hello World');
})
```



### GET

```javascript
// GET: params, query
app.get('/user/:id', (req, res) => {
  const p = req.pa003040rams;
  const q = req.query;
  
  res.send({'message': 'Hello World'});
})
```



### POST

```javascript
// POST: params, body
app.use(express.json());
app.post('/user/:id', (req, res) => {
  const p = req.params;
  const b = req.body;
  
  res.send({'message': 'Hello World'});
})
```



### CORS

```
sudo npm install cors
```

```javascript
var cors = require('cors')

app.use(cors())	// 비워놓으면 모든 요청 허용
```



### Nodemon

```
// Hot Loading
sudo npm i nodemon
```

---



## Node.js 서버 장점

- Non-blocking I/O
  - 요청이 많거나 오래걸리는 요청이 있어도 멈추거나 요청 대기시간 X (병렬 처리(?))
  - 일반 서버는 서버 스케일링 혹은 멀티쓰레딩으로 처리 가능
  - 채팅/SNS에 자주 사용
- 코드가 매우 짧고 쉬워서 빠른 개발 가능
- Event Driven





