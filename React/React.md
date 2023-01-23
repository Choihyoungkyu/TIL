# React

```
npm install 
npm install npx -g
npm install create-react-app
npm uninstall create-react-app
npm list -g
npx create-react-app {app name} or create-react-app {app name}
create-react-app {app name}
```

```
npm start
npm install react-router-dom
```

```
npm install @reduxjs/toolkit

```



---

### Redux

#### 키워드

- 액션 (Action)

  - `type` 필드를 필수적으로 가지고 있어야 함

  ```js
  {
    type: "ADD_TODO",
    data: {
      id: 0,
      text: "리덕스 배우기"
    }
  }
  ```

- 액션 생성함수 (Action Creator)

  - 파라미터를 받아와서 액션 객체 형태로 만들어줌
  - 컴포넌트에서 더욱 쉽게 액션을 발생시키기 위함

  ```js
  // 액션 선언 (대부분 대문자로 선언)
  const CHANGE_INPUT = 'CHANGE_INPUT';
  
  // 액션 생성 함수
  export const changeInput = (text) => ({ 
    type: "CHANGE_INPUT",					// type: 액션
    text
  });
  ```

- 리듀서 (Reducer)

  - state와 action을 파라미터로 받아와서 state를 변경하는 함수
  - action에는 액션 생성 함수에서 반환하는 객체가 들어감

  ```js
  const reducer = (state=initState, action) => {
    switch (action.type) {
      case Action이름:
        return {
          ...state,				// 다른 state값은 변경되지 않게 하기 위해 전개연산자 사용
          바꿀 state: 지정 값
        }
    }
  }
  ```

  - 여러개의 리듀서를 만들고 이를 합쳐서 루트 리듀서 (Root Reducer)를 만들 수 있음

  ```js
  import { combineReducers } from 'redux';
  import memberDetail from './memberDetail';
  import member from './member';
  
  export default combineReducers({
    memberDetail,
    member,
  });
  ```

- 스토어 (Store)

  - 한 애플리케이션당 하나의 스토어
  - 현재의 앱 상태, 리듀서가 들어가있고, 추가적으로 몇가지 내장 함수가 있음
  - combineReducers()를 통해 통합된 reducer와 initState(state 초기값)를 준비한다.

  ```js
  // store/modules/test.js
  import { createSlice } from "@reduxjs/toolkit";
    
  const toDos = createSlice({
    name: "toDosReducer",
    initialState: [],
    reducers: {
      addToDo: (state, action) => {
        state.push({ text: action.payload, id: Date.now() });
      },
      deleteToDo: (state, action) =>
        state.filter((toDo) => toDo.id !== action.payload),
    },
  });
  
  export const { addToDo, deleteToDo } = toDos.actions;
  
  export default toDos.reducer;   // 이렇게 export 하면 toDosReducer로 됨
  
  
  // store/modules/index.js
  import { combineReducers } from 'redux';
  // toDos.reducer가 자동으로 toDosReducer로 바뀜
  import toDosReducer from './modules/test';
  
  const rootReducer = combineReducers({
    // Reducer로 끝나는 것들은 이름 설정해주기!! 아니면 에러남
    toDos: toDosReducer,
  });
  
  export default rootReducer;
  
  
  // store/index.js
  import { configureStore } from '@reduxjs/toolkit';
  import rootReducer from './modules/index';
  
  const store = configureStore({ 
    reducer: rootReducer,
  });
  
  export const store;
  ```

  - store 옵션을 설정한 `<Provider>` 태그로 App component를 감싸준다.

- 디스패치 (dispatch)

  - 스토어의 내장함수
  - 액션을 발생 시키는 것 `dispatch(action)`

- 구독 (subscribe)

  - 스토어의 내장함수
  - subscibe 함수에 특정 함수를 전달해주면, 액션이 디스패치 되었을 때마다 전달해준 함수가 호출됨
  - react-redux 라이브러리에서 제공하는 `connect` 함수 또는 `useSelector` Hook을 사용하여 리덕스 스토어의 상태에 구독



#### useSelector

- connect 함수를 이용하지 않고 리덕스의 state를 조회 가능

```js
import { useSelector } from 'react-redux';
const user = useSelector(state => state.user);
```



#### useDispatch

- 생성한 action을 useDispatch를 통해 발생시킬 수 있다
- 만들어둔 액션생성 함수를 import 한다

```js
import { change_user } from '../modules/user';
import { useDispatch } from 'react-redux';

const User = () => {
  ...
  const dispatch = useDispatch();
  dispatch(change_user(user));
  ...
}
  
// 위에서 dispatch한 change_user는 아래와 같이 정의된 액션 생성 함수이다.
export const change_user = createAction(CHANGE_USER, user => user);
```

- `createAction` : 액션 생성 함수를 만들어주는 함수



#### handleActions

- 리듀서를 더 간단하게 작성 가능

```js
// 원래 버전
const reducer = (state = initState, action) => {
  switch (action.type) {
    case CHANGE_USER:
      return {
        ...state,
        user: action.user
      }
  }
}

// handleActions를 사용했을 때
import { handleActions } from 'redux-actions';
const reducer = handleActions({
  [CHANGE_USER]: (state, action) => ({...state, user: action.user})
})
```



#### 활용 예시 (useSelector, useDispatch)

```js
import React from 'react';
import { useSelector, useDispatch } from 'react-redux';
import { increment, decrement } from './Actions/Action';

function App() {
  const counter = useSelector(state => state.counter.count)
  const isLogged = useSelector(state => state.logged.isLogged)
  const dispatch = useDispatch();

  return (
    <div className="App">
      <h1>Counter: {counter}</h1>
      {isLogged && <h3>Valuable Information I shouldn't see.</h3>}

      <button onClick={() => dispatch(increment(1))}>+</button>
      <button onClick={() => dispatch(decrement(1))}>-</button>
    </div>
  );
}

export default App;
```



---

### redux-saga

- **비동기 작업**을 하는 **미들웨어**가 필요할 때 사용
- 액션을 모니터링하고 있다가, 특정 액션이 발생하면 이에 따라 특정 작업을 하는 방식으로 사용
- redux-thunk로 못하는 작업 처리 가능
  1. 비동기 작업을 할 때 기존 요청을 취소 처리 가능
  2. 특정 액션이 발생했을 때 이에 따라 다른 액션이 디스패치되게끔 하거나, 자바스크립트 코드를 실행할 수 있음
  3. 웹소켓을 사용하는 경우 Channel 이라는 기능을 사용하여 더욱 효율적으로 코드 관리 가능 [[링크](https://medium.com/@pierremaoui/using-websockets-with-redux-sagas-a2bf26467cab)]
  4. API 요청이 실패했을 때 재요청하는 작업 가능
- redux-thunk에 비해 일관적으로 액션객체를 반환한다는 장점이 있음



#### generator 함수

- generator 함수는 일반 함수와는 다르게 함수 코드 실행을 일시 중지했다가 필요한 시점에 재시작할 수 있는 함수
- yield는 중단점을 만든다
- yield 뒤에 값이 있으면 그걸 객체의 value에 담아 return하고 멈춤
- `function*` 로 선언
- `next()` 를 통해 다음 중단점까지 실행시킬 수 있다



#### 자주 쓰이는 effects

`import {all, fork, take, call, put} from 'redux-saga/effects';`

- effect 는 yield 뒤에 오는 함수로, 각자의 역할을 수행

- **take**

  - 해당 액션이 dispatch 되면 제너레이터를 next 한다.

  ```js
  function* watchLogIn() {
    yield take('LOG_IN', logIn);	// 'LOG_IN'이 들어오면 logIn 함수 실행
  }
  ```

- **put**

  - 특정 action을 dispatch 시켜준다.
  - 파라미터로는 액션 객체가 들어간다.

  ```js
    yield put({
      type: 'LOG_IN_SUCCESS',	// action
      data: result.data
    });
  ```

- **takeEvery**

  - 모든 해당 액션을 처리

- **takeLatest**

  - 가장 마지막으로 dispatch 된 액션을 처리

- **all**

  - 여러 사가를 합쳐주는 역할
  - all은 파라미터로 배열을 받는데, 배열 내에 있는 것을 모두 실행시킨다

- **call**

  - 함수를 동기적으로 실행시켜준다
  - 첫번째 파라미터는 함수, 두번째 파라미터는 해당 함수에 넣을 인수

  ```js
    yield call(request, action.payload)
  ```

- **fork**

  - call과 파라미터가 같고 마찬가지로 함수를 실행시키는 역할
  - 비동기이기 때문에 결과값을 기다려 주지 않는다

  ```js
    export default function* rootSaga() {
      yield all([
        fork(함수),
        fork(함수)
      ])
    }
  ```

  

#### 기초 구현 코드

```js
import {all, fork, take, call, put} from 'redux-saga/effects';
import axios from 'axios';

function logInAPI(data) {
    return axios.post('url/api/login', data);
}

function* logIn(action) {
    try {
        const result = yield call(logInAPI, action.data);
				// logInAPI에 전달할 파라미터를 call의 두번째 파리미터로 지정해준다. 
				// action이 login에 대한 액션이니까 action.data에 내가 넣어둔 데이터가 들어있다.
        yield put({
            type: 'LOG_IN_SUCCESS',
            data: result.data
        });
    } catch (err) {
        yield put({
            type: 'LOG_IN_FAILURE',
            data: err.response.data
        });
    }
}

function* watchLogIn() {
    yield take('LOG_IN', logIn); // login에 대한 액션 자체가 logIn에 매개변수로 전달된다.
}


// (a) 액션을 발생시키고 싶은 시점에서 아래와 같이 dispatch! 
dispatch(login({data: user}));
```

- 예를 들어 내가 LOG_IN 액션에 대한 액션 생성함수를 login으로 만들었을 때
- 해당 액션을 발생시키고 싶은 시점에서 (a) 같이 dispatch하면
- watchLogIn함수 내의 take에서 받아서 logIn generator함수를 실행시킨다.
- 이때, logIn의 파라미터 action으로는 내가 dispatch한 액션 자체가 들어온다. (즉 action.data는 내가 넣은 user)
- 그 값으로 axios요청을 하고 성공하면 LOG_IN_SUCCESS put
- 실패하면 LOG_IN_FAILURE을 put한다.
- 각각 LOG_IN_SUCCESS와 LOG_IN_FAILURE에 대해서 성공 시 state를 바꾸는 등의 코드를 리듀서로 작성해야 한다.
