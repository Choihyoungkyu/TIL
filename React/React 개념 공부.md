## React 개념 공부



#### Create-React-App(CRA)

- 리액트 개발환경을 쉽게 구축해줌 (by 페이스북 리액트팀)

1. webpack(모듈+라이브러리 번들링)
2. babel(jsx 컴파일)
3. jest(테스트)
4. eslint(코드형상관리)
5. polyfill(구형 브라우저 미지원 문법 등 대응)
6. HMR(Hot Module Replacement : 재시작 없이 변경사항 반영)
7. CSS 후처리 (SASS 컴파일, 벤더접두사 prefix 등)



#### React 동작 원리 

- 가상DOM을 통해 변경된 부분만 효율적으로 업데이트
  - 가상DOM : 실제 DOM을 분석하여 만든 JavaScript 객체
  - 컴포넌트의 상태값이 변경되면, 새로운 가상 DOM 객체를 만들고, 이전 가상 DOM 객체와 비교



#### React UI 업데이트 단계

- 렌더 단계
  - 렌더링 할 때마다 매번 새로운 가상 DOM을 만들고, 이전 가상 DOM과 비교하여 바뀐 부분을 탐색하고, 실제 DOM에 반영할 부분을 결정
- 커밋 단계
  - 바꾸기로 결정된 부분만 실제 DOM에 반영
  - 브라우저는 변경된 실제 DOM을 화면에 paint
    - 이 때가 didMount, didUpdate가 완료되어 useEffect가 호출되는 시점



#### React를 JSX로 코딩할 수 있는 이유

- Babel이 JSX를 React.createElemet() 로 변환해준다

- WebPack이 JS, CSS 파일을 번들링하여 모듈화해준다



#### React 컴포넌트 재렌더링 케이스

1. 내부 상태값(state) 변경
2. 부모가 전해준 속성(props) 변경
3. 중앙 상태값(redux store 등) 변경
4. 부모 컴포넌트가 재렌더링되는 경우, 자식 컴포넌트도 재렌더링



#### React 마운트 과정

1. 함수 컴포넌트 호출
2. 구현부 실행
   - props 취득, hook 실행, 내부 변수 및 함수 생성
   - 단, hook에 등록해둔 상태값, 부수함수 효과 등은 별도 메모리에 저장되어 관리
3. return 실행
   - 렌더링 시작
4. 렌더 단계(Render Phase)
   - 가상 DOM을 생성
5. 커밋 단계(Commit Phase)
   - 실제 DOM을 반영
6. useLayoutEffect
   - 브라우저가 화면에 Paint 하기 전에, useLayoutEffect에 등록해둔 effect(부수효과함수)가 '동기'로 실행됨
   - 이 때, state, redux store 등의 변경이 있다면 한번 더 재렌더링 된다
7. Paint
   - 브라우저가 실제 DOM을 화면에 그린다. didMount가 완료된다
8. useEffect
   - Mount되어 화면이 그려진 직후, useEffect에 등록해둔 effect(부수효과함수)가 '비동기'로 실행됨



#### useEffect와 useLayoutEffect

1. **useEffect** (비동기 effect)

   - useEffect에 등록된 effect는 화면이 그려진 직후, "비동기"로 실행됨

   1. (재)렌더링 시작
   2. 실제 DOM에 반영
   3. 화면에 Paint(didMount || didUpdate)
   4. effect 함수 비동기 실행

2. **useLayoutEffect** (동기 effect)

   - useLayoutEffect에 등록된 effect는 실제 DOM 반영 후 화면이 그려지기 직전, "동기"로 실행됨

   1. (재)렌더링 시작
   2. 실제 DOM에 반영
   3. effect 함수 동기 실행 : state 등 변경시, 다시 재렌더링 됨
   4. 화면에 Paint(didMount || didUpdate)



#### Redux Store 변경시, 자동으로 재렌더링 되는 이유

`<Provider store={store}>`로 컴포넌트들을 감싸주면, 스토어 상태가 변경될 때마다 이를 참조하는 컴포넌트들이 재렌더링 되도록 react-redux 라이브러리가 자동으로 컴포넌트들의 렌더 함수들을 subscribe 처리 해줌



#### 자식 컴포넌트의 불필요한 재렌더링 막는 방법

- 부모 컴포넌트가 재렌더링 되면, 자식 컴포넌트들도 모두 자동으로 재렌더링됨
- `React.memo`를 사용하면, 자식이 전달받는 props가 변경되었을 때만 재렌더링 되도록 최적화 가능



#### 재렌더링시, 불필요한 지역변수/함수 재생성 막는 방법

- useMemo or useCallback 훅을 사용하면, 최초 한번 생성 후 재사용 가능
- 훅 사용시, 의존성배열을 추가하여 재생성 여부를 결정할 수 있다



#### 리액트 커스텀 환경변수

- 앞에 REACT_APP_ 을 붙여서 **REACT_APP_환경변수명=값** 형태로 정의
- 등록된 환경변수는 소스코드 상에서 process.env.REACT_APP_환경변수명 으로 참조 가능
  - .env.development : development 환경 (process.env.NODE_ENV == 'development')
  - .env.test : test 환경 (process.env.NODE_ENV == 'test')
  - .env.production : build 환경 (process.env.NODE_ENV == 'production')

---



#### React vs Vue

|        |                            React                             |                             Vue                              |
| :----: | :----------------------------------------------------------: | :----------------------------------------------------------: |
|  정의  |                        UI 라이브러리                         |                          프레임워크                          |
|  특징  | 라이브러리라 참고가 용이<br />리액트 자체만으로는 전역 상태 관리, 라우팅, 빌드 시스템 등 못함<br />사용자가 필요할 때에 가져다 쓰고, 빼며 부분적으로 사용 가능 | 부분적인 사용이 불가하고 프레임워크가 지원해주는 문법에 따라야함<br />라이브러리와 비교해 더 많은 기능을 디폴트로 제공해줌 |
|  개발  | 자바스크립트 문법을 응용해 개발자에 따라 자유롭게 개발 가능  |      프레임워크 사용에 지정된 문법 방식으로만 개발 가능      |
| 차이점 | JSX(JavaScript XML) 형태로 코드를 작성하여 JS만으로 UI 로직과 DOM을 구현 | HTML, JS, CSS 코드 영역을 분리해서 작성해 코드의 가시성과 생산성이 좋다는 평이 있음 |
|  장점  | 컴포넌트의 생성 및 재사용이 간편하다<br />(vue는 template, script, style 모두 작성하고 props도 귀찮음) |                       진입장벽이 낮다                        |
|  추천  | 1. 프로젝트 규모가 크다, 점점 확장될것이다<br />2. JS 문법에 능숙하다<br />3. 컴포넌트를 작은 단위로 나누어 UI 재사용을 많이 할것이다<br />4. 커스터마이징 및 자유도가 높은 개발 환경 선호<br />5. 넓은 커뮤니티 및 개발 인력시장의 혜택을 보고싶다 | 1. 규모가 작고 가벼운 프로젝트를 빠르게 만들고싶다<br />2. 속도 이슈에 매우 민감한 사이트이다<br />3. 회사에 퍼블리셔가 따로 존재한다<br />4. 기존 html css js 구조로 작성된 코드를 SPA로 옮기고 싶다<br />5. 개발자간 코드 통일성을 위한 커뮤니케이션 비용을 줄이고 싶다 |



#### NPM & NPX & YARN

**NPM**

- Node.js의 기본 **패키지 관리자**

**NPX**

- npm에 속해 있는 npm **패키지 실행 도구**
- npx는 해당 패키지를 실행만 되게 해주기 때문에 가볍게 사용 가능
- 개발을 하는 입장이라면 npm과 npx의 차이를 못느낄 수 있지만, 실행하는 입장에서는 크게 다가오는 차이점임

**Yarn**

- npm, npx와는 결이 다른 **패키지 관리자**
- 속도나 안정성에서는 npm과 비슷
- 차이점  : 버전을 어디에서나 같게 만들어 버그를 줄임으로써 보안을 높임
- 단점 : npm 시장점유율이 높아 npm에 대한 자료가 많음