# 221026. Asynchronous JS



## 동기 (Synchronous)

- 모든 일을 **순서대로 하나씩** 처리하는 것
- 순서대로 처리한다 == 이전 작업이 끝나면 다음 작업을 시작한다
- 우리가 작성했던 Python 코드가 모두 동기식
- 요청과 응답을 동기식으로 처리한다면 비효율적



## 비동기 (Asynchronous)

- 작업을 시작한 후 **결과를 기다리지 않고** 다음 작업을 처리하는 것 (병렬적 수행)
- 시간이 필요한 작업들은 요청을 보낸 뒤 응답이 빨리 오는 작업부터 처리
- ex) Gmail에서 메일 전송을 누르면 목록 화면으로 전환되지만 실제로 메일을 보내는 작업은 병렬적으로 뒤에서 처리됨



#### 비동기를 사용하는 이유

- **사용자 경험**
  - 예를 들어 아주 큰 데이터를 불러온 뒤 실행되는 앱이 있을 때, 동기로 처리한다면 데이터를 모두 불러온 뒤에야 앱의 실행 로직이 수행되므로 사용자들은 마치 앱이 멈춘 것과 같은 경험을 겪게 됨
  - **비동기로 처리한다면 먼저 처리되는 부분부터 보여줄 수 있으므로,** 사용자 경험에 긍정적인 효과를 볼 수 있음
    이와 같은 이유로 많은 웹 기능은 비동기 로직을 사용해서 구현되어 있음

---



## JavaScript의 비동기 처리

#### Single Thread 언어, JavaScript

- **JavaScript는 한 번에 하나의 일만 수행할 수 있는 Single Thread 언어**로 동시에 여러 작업을 처리할 수 없음
- **[참고] Thread란?**
  - 작업을 처리할 때 실제로 작업을 수행하는 주체로, multi-thread라면 업무를 수행할 수 있는 주체가 여러 개라는 의미



#### JavaScript Runtime

- JavaScript 자체는 Single Thread이므로 비동기 처리를 할 수 있또록 도와주는 환경이 필요함
- 특정 언어가 동작할 수 있는 환경을 **런타임(Runtime)**이라 함
- JavaScript에서 **비동기와 관련한 작업은 *브라우저* 또는 *Node 환경*에서 처리**
- 이중에서 브라우저 환경에서의 비동기 동작은 크게 아래의 요소들로 구성됨
  1. JavaScript Engine의 **Call Stack**
  2. **Web API**
  3. **Task Queue**
  4. **Event Loop**



#### 비동기 처리 동작 방식

- 브라우저 환경에서의 JavaScript의 비동기 처리 동작 방식
  1. 모든 작업은 **Call Stack**(LIFO)으로 들어간 후 처리된다.
  2. 오래 걸리는 작업이 **Call Stack**으로 들어오면 **Web API**로 보내서 처리하도록 한다.
  3. Web API에서 처리가 끝난 작업들은 **Task Queue**(FIFO)에 순서대로 들어간다.
  4. **Event Loop**가 **Call Stack**이 비어 있는 것을 체크하고, **Task Queue**에서 가장 오래된 작업을 **Call Stack**으로 보낸다.

1. **Call Stack**
   - 요청이 들어올 때마다 순차적으로 처리하는 Stack(LIFO)
   - 기본적인 JavaScript의 Single Thread 작업 처리
2. **Web API**
   - JavaScript 엔진이 아닌 브라우저에서 제공하는 runtime 환경으로 시간이 소요되는 작업을 처리 (setTimeout, DOM Event, AJAX 요청 등)
3. **Task Queue**
   - 비동기 처리된 Callback 함수가 대기하는 Queue(FIFO)
4. **Event Loop**
   - Call Stack과 Task Queue를 지속적으로 모니터링
   - Call Stack이 비어 있는지 확인 후 비어 있다면 Task Queue에서 대기 중인 오래된 작업을 Call Stack으로 Push



#### 정리

JavaScript는 한 번에 하나의 작업만 수행하는 Single Thread 언어로 동기적 처리를 하지만, 브라우저 환경에서는 Web API에서 처리된 작업이 지속적으로 Task Queue를 거쳐 Event Loop에 의해 Call Stack에 들어와 순차적으로 실행됨으로써 비동기 작업이 가능한 환경이 된다.

---



## Axios 라이브러리

#### Axios

- JavaScript의 HTTP 웹 통신을 위한 라이브러리
- 확장 가능하나 인터페이스와 쉽게 사용할 수 있는 비동기 통신 기능을 제공
- node 환경은 npm을 이용해서 설치 후 사용할 수 있고, browser 환경은 CDN을 이용해서 사용할 수 있음
- Axios 공식 문서 및 github
  - https://axios-http.com/kr/docs/intro
  - https://github.com/axios/axios



#### Axios 사용해보기

```html
<script src="https://cdn.jsdelivr.net/npm/axios/dist/axios.min.js"></script>
<script>
  axios.get('요청할 URL')
    .then(성공하면 수행할 콜백함수)
    .catch(실패하면 수행할 콜백함수)
</script>
```

- get, post 등 여러 method 사용가능
- **then**을 이용해서 성공하면 수행할 로직을 생성
- **catch**를 이용해서 실패하면 수행할 로직을 작성



#### 고양이 사진 가져오기

- The Cat API (https://api.thecatapi.com/v1/images/search)
  - 이미지를 요청해서 가져오는 작업을 비동기로 처리
- response 구조

```json
// https://api.thecatapi.com/v1/images/search
[
    {
        "id": "d6n",
        "url": "https://cdn2.thecatapi.com/images/d6n.jpg",
        "width": 333,
        "height": 500
    }
]
```

- Python으로 요청해보기 (동기)

```python
import requests

print('고양이는 야옹')

cat_image_search_url = 'https://api.thecatapi.com/v1/images/search'
response = requests.get(cat_image_search_url)

if response.status_code == 200:
    print(response.json())
else:
    print('실패했다옹')
    
print('야옹야옹')

# 고양이는 야옹
# [{'id': 'cir', 'url': 'https://cdn2.thecatapi.com/images/cir.jpg', 'width': 500, 'height': 667}]
# 야옹야옹
```

- Axios로 요청해보기 (비동기)

```html
<script src="https://cdn.jsdelivr.net/npm/axios/dist/axios.min.js"></script>
<script>
  console.log('고양이는 야옹')
    const catImageSearchURL = 'https://api.thecatapi.com/v1/images/search'
    
    axios.get(catImageSearchURL)
      .then((response) => {
        console.log(response.data)
      })
      .catch((error) => {
        console.log('실패했다옹')
      })
      console.log('야옹야옹')
</script>

// 고양이는 야옹
// 야옹야옹
// {id: '2so', url: 'https://cdn2.thecatapi.com/images/2so.jpg'}
```



#### 고양이 사진 가져오기 (결과 비교)

- 동기식 코드(python)는 위에서부터 순서대로 처리가 되기 때문에 첫번째 print가 출력되고 이미지를 가져오는 처리를 기다렸다가 다음 print가 출력됨
- 비동기식 코드(JavaScript)는 바로 처리가 가능한 작업(console.log)은 바로 처리하고, 오래 걸리는 작업인 이미지를 요청하고 가져오는 일은 요청을 보내놓고 기다리지 않고 다음 코드로 진행 후 완료가 된 시점에 결과 출력이 진행됨



#### 정리

- axios는 비동기로 데이터 통신을 가능하게 하는 라이브러리
- 같은 방식으로 우리가 배운 Django API로 요청을 보내서 데이터를 받아온 후 처리할 수 있음

---



## Callback과 Promise

#### 비동기 처리의 단점

- 비동기 처리의 핵심은 Web API로 들어오는 순서가 아니라 **작업이 완료되는 순서에 따라 처리**한다는 것!
- 그런데 이는 개발자 입장에서 코드의 실행 순서가 불명확하다는 단점이 있음
  - 해결 방법 -> **콜백 함수**를 사용하자 !



### 콜백 함수 (Callback Function)

- 특별한 함수가 아님! **다른 함수의 인자로 전달되는 함수**를 콜백 함수라고 한다.
- 비동기에만 사용되는 함수가 아니며 동기, 비동기 상관없이 사용 가능
- 시간이 걸리는 **비동기 작업이 완료된 후 실행할 작업을 명시하는데 사용**되는 콜백 함수를 **비동기 콜백(asynchronous callback)**이라 부름



#### 콜백 함수를 사용하는 이유

- 명시적인 호출이 아닌 특정한 조건 혹은 행동에 의해 호출되도록 작성할 수 있음
- "요청이 들어오면", "이벤트가 발생하면", "데이터를 받아오면" 등의 조건으로 이후 로직을 제어할 수 있음
- **비동기 처리를 순차적으로 동작할 수 있게 함**
- 비동기 처리를 위해서는 콜백 함수의 형태가 반드시 필요함



#### 콜백 지옥 (Callback Hell)

- 콜백 함수는 연쇄적으로 발생하는 비동기 작업을 순차적으로 동작할 수 있게 함
- 비동기 처리를 위한 콜백을 작성할 때 마주하는 문제를 콜백 지옥(Callback Hell)이라 하며, 그때의 코드 작성 형태가 마치 "피라미드와 같다"고 해서 "Pyramid of doom(파멸의 피라미드)"라고도 부름



#### 정리

- 콜백 함수는 비동기 작업을 순차적으로 실행할 수 있게 하는 반드시 필요한 로직
- 비동기 코드를 작성하다보면 콜백 함수로 인한 콜백 지옥(Callback hell)은 반드시 나타나는 문제
  - 코드의 가독성을 해침
  - 유지 보수가 어려워짐



### 프로미스(Promise)

- Callback Hell 문제를 해결하기 위해 등장한 비동기 처리를 위한 객체
- "작업이 끝나면 실행 시켜줄게"라는 약속(promise)
- **비동기 작업의 완료 또는 실패를 나타내는 객체**
- Promise 기반의 클라이언트가 바로 이전에 사용한 **Axios** 라이브러리 !
  - "Promise based HTTP client for the browser and node.js"
  - 성공에 대한 약속 **then(callback)**
    - 요청한 작업이 성공하면 callback 실행
    - callback은 **이전 작업의 성공 결과를 인자로 전달 받음**
  - 실패에 대한 약속 **catch(callback)**
    - then()이 하나라도 실패하면 callback 실행
    - callback은 이전 작업의 실패 객체를 인자로 전달 받음

- then과 catch 모두 항상 promise 객체를 반환 --> 계속해서 chaining을 할 수 있음
- **axios로 처리한 비동기 로직이 항상 promise 객체를 반환**
  - 그래서 then을 계속 이어 나가면서 작성할 수 있었던 것

```js
axios.get('요청할 URL').then(...).then(...).catch(...)
```

```js
axios.get('요청할 URL')	// Promise 객체 return
  .then(성공하면 수행할 1번 콜백함수)
  .then(1번 콜백함수가 성공하면 수행할 2번 콜백함수)
  ...
  .catch(실패하면 수행할 콜백함수)		// error handling --> 마지막에만 쓸 수 있는게 아니라 중간에 섞어도 상관 없음 -> 중간에 섞으면 그 위에서 error가 났을 때만 해당 catch로 감
```

- promise 방식은 비동기 처리를 마치 우리가 일반적으로 위에서 아래로 적는 방식처럼 코드를 작성할 수 있음
- 항상 **return**으로 넘겨줘야됨!!!!!!!!!!



#### Promise가 보장하는 것 (vs 비동기 콜백)

- 비동기 콜백 작성 스타일과 달리 Promise가 보장하는 콜백

1. callback 함수는 JavaScript의 Event Loop가 현재 실행 중인 Call Stack을 완료하기 이전에는 절대 호출되지 않음
   - Promise callback 함수는 Event Queue에 배치되는 엄격한 순서로 호출됨
2. 비동기 작업이 성공하거나 실패한 뒤에 .then() 메서드를 이용하여 추가한 경우에도 1번과 똑같이 동작
3. .then()을 여러 번 사용하여 여러 개의 callback 함수를 추가할 수 있음 (Chaining)
   - 각각의 callback은 주어진 순서대로 하나하나 실행하게 됨
   - Chaining은 Promise의 가장 뛰어난 장점

---



## AJAX

- 비동기 통신을 이용하면 화면 전체를 새로고침 하지 않아도 서버로 요청을 보내고, 데이터를 받아 화면의 일부분만 업데이트 가능
- 이러한 '비동기 통신 웹 개발 기술'을 Asynchronous Javascript And XML(AJAX)'라 함
- **AJAX의 특징**
  1. 페이지 새로고침 없이 서버에 요청
  2. 서버로부터 응답(데이터)을 받아 작업을 수행
- 이러한 비동기 웹 통신을 위한 라이브러리 중 하나가 Axios



### 비동기(Async) 적용하기

(04_db 활용)

#### 팔로우 (follow)

- 각각의 템플릿에서 sciprt 코드를 작성하기 위한 block tag 영역 작성

```html
<!-- base.html -->
<body>
  ...
  {% block script %}
  {% endblock script %}
</body>
</html>
```

- axios CDN 작성

```html
<!-- accounts/profile.html -->

{% block script %}
  <script src="https://cdn.jsdelivr.net/npm/axios/dist/axios.min.js"></script>
  <scrtip>
  </scrtip>
{% endblock script %}
```

- form 요소 선택을 위해 id 속성 지정 및 선택
- 불필요해진 action과 method 속성은 삭제 (요청은 axios로 대체되기 때문)

```html
<!-- accounts/profile.html -->

<form id="follow-form">
  ...
</form>

<script>
  const form = document.querySelector('#follow-form')
</script>
```

- form 요소에 이벤트 핸들러 작성 및 submit 이벤트 취소

```html
<!-- accounts/profile.html -->

<script>
  const form = document.querySelector('#follow-form')
  form.addEventListener('submit', function (event) {
      event.preventDefault()
  })
</script>
```

- axios 요청 준비

```html
<!-- accounts/profile.html -->

<script>
  const form = document.querySelector('#follow-form')
  form.addEventListener('submit', function (event) {
    event.preventDefault()
    
    axios({
      method: 'POST',
      url: `/accounts/${???}/follow`,
    })
  })
</script>
```

- 현재 axios로 POST 요청을 보내기 위해 필요한 것

  1. url에 작성할 user pk는 어떻게 작성해야 할까?
     - url에 작성할 user pk 가져오기 (HTML -> JavaScript)

  ```html
  <!-- accounts/profile.html -->
  
  <form id="follow-form" data-user-id="{{ person.pk }}">
    ...
  </form>
  
  <script>
    const form = document.querySelector('#follow-form')
    form.addEventListener('submit', function (event) {
      event.preventDefault()
      
      const userId = event.target.dataset.userId
      ...
    })
  </script>
  ```

  - url 작성 마치기

  ```html
  <!-- accounts/profile.html -->
  
  <script>
    const form = document.querySelector('#follow-form')
    form.addEventListener('submit', function (event) {
      event.preventDefault()
      
      const userId = event.target.dataset.userId
      axios({
        method: 'post',
        url: `/accounts/${userId}/follow/`,
      })
    })
  </script>
  ```

  





2. csrftoken은 어떻게 보내야 할까?

   - 먼저 hidden 타입으로 숨겨져있는 csrf 값을 가진 input 태그를 선택해야함
     https://docs.djangoproject.com/en/3.2/ref/csrf/

   ```html
   <!-- accounts/profile.html -->
   
   <script>
     const form = document.queryselector('#follow-form')
     const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value
   </script>
   ```

   - AJAX로 csrftoken을 보내는 방법
     https://docs.djangoproject.com/en/3.2/ref/csrf/#setting-the-token-on-the-ajax-request

   ```html
   <!-- accounts/profile.html -->
   
   <script>
     const form = document.queryselector('#follow-form')
     const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value
     form.addEventListener('submit', function (event) {
       event.preventDefault()
       const userId = event.target.dataset.userId
       axios({
           method: 'post',
           url: `/accounts/${userId}/follow/`,
           headers: {'X-CSRFToken': csrftoken,}
       })
     })
   </script>
   ```

   

#### data-* attributes

- 사용자 지정 데이터 특성을 만들어 임의의 데이터를 HTML과 DOM사이에서 교환할 수 있는 방법
- 사용 예시

```html
<div data-my-id="my-data"></div>
<script>
  const myId = event.target.dataset.myId
</script>
```

- 모든 사용자 지정 데이터는 dataset 속성을 통해 사용할 수 있음
  https://developer.mozilla.org/ko/docs/Web/HTML/Global_attributes/data-*

- 예를 들어 data-test-value라는 이름의 특성을 지정했다면 JavaScript에서는 element.dataset.testValue로 접근할 수 있음
- 속성명 작성 시 주의사항
  - 대소문자 여부에 상관없이 xml로 시작하면 안됨
  - 세미콜론을 포함해서는 안됨
  - 대문자를 포함해서는 안됨



#### 팔로우 (follow)

- 팔로우 버튼을 토글하기 위해서는 현재 팔로우가 된 상태인지 여부 확인이 필요
- axios 요청을 통해 받는 response 객체를 활용해 view 함수를 통해서 팔로우 여부를 파악할 수 있는 변수를 담아 JSON 타입으로 응답하기

```python
# accounts/views.py
from django.http import JsonResponse

@require_POST
def follow(request, user_pk):
    if request.user.is_authenticated:
        User = get_user_model()
        me = request.user
        you = User.object.get(pk=user_pk)
        if me != you:
            if you.followers.filter(pk=me.pk).exists():
                # 언팔로우
                you.followers.remove(me)
                is_followed = False
            else:
                # 팔로우
                you.followers.add(me)
				is_followed = True
            context = {
                'is_followed': is_followed,
                'followers_count': you.followers.count(),
                'followings_count': you.followings.count(),
            }
            return JsonResponse(context)
        return redirect('accounts:profile', you.username)
    return redirect('accounts:login')
```

- view 함수에서 응답한 is_followed를 사용해 버튼 토글하기

```html
<!-- accounts/profile.html -->

<script>
...
  axios({
    method: 'post',
    url: `/accounts/${userId}/follow`,
    headers: {'X-CSRFToken': csrftoken,}
  })
  .then((response) => {
    const isFollowed = response.data.is_followed
    const followBtn = document.querySelector('#follow-form > input[type=submit]')
    if (isFollowed === true) {
      followBtn.value = '언팔로우'
    } else {
      followBtn.value = '팔로우'
    }
  })  
</script>
```



#### [참고] XHR

- "XMLHttpRequest"
- AJAX 요청을 생성하는 JavaScript API
- XHR의 메서드로 브라우저와 서버 간 네트워크 요청을 전송할 수 있음
- Axios는 손쉽게 XHR을 보내고 응답 결과를 Promise 객체로 반환해주는 라이브러리



#### 팔로워 & 팔로잉 수 비동기 적용

- 해당 요소를 선택할 수 있도록 span 태그와 id 속성 작성

```html
<!-- accounts/profile.html -->
{% extends 'base.html' %}

{% block content %}
  <h1>{{ person.username }}님의 프로필</h1>
  <div>
    팔로워 : <span id="followers-count">{{ person.followers.all|length }}</span> / 
    팔로잉 : <span id="followings-count">{{ person.followings.all|length }}</span>
  </div>
```

- 직전에 작성한 span 태그를 각각 선택

```html
<!-- accounts/profile.html -->
<script>
  ...
    axios({
      method: 'post',
      url: `/accounts/${userId}/follow`,
      headers: {'X-CSRFToken': csrftoken,}
    })
    .then((response) => {
      ...
      const followersCountTag = document.querySelector('#followers-count')
      const followingsCountTag = document.querySelector('#followings-count')
    })  
</script>
```

- 팔로워, 팔로잉 인원 수 연산은 view 함수에서 진행하여 결과를 응답으로 전달

```python
# accounts/views.py
from django.http import JsonResponse

@require_POST
def follow(request, user_pk):
    ...
    	context = {
            'is_followed': is_followed,
            'followers_count': you.followers.count(),
            'followings_count': you.followings.count(),
        }
        return JsonResponse(context)
    return redirect('accounts:profile', you.username)
return redirect('accounts:login')
```

- view 함수에서 응답한 연산 결과를 사용해 각 태그의 인원 수 값 변경하기

```html
<!-- accounts/profile.html -->
<script>
  ...
    axios({
      method: 'post',
      url: `/accounts/${userId}/follow`,
      headers: {'X-CSRFToken': csrftoken,}
    })
    .then((response) => {
      ...
      const followersCountTag = document.querySelector('#followers-count')
      const followingsCountTag = document.querySelector('#followings-count')
      const followersCount = response.data.followers_count
      const followingsCount = response.data.followings_count
      followersCountTag.innerText = followersCount
      followingsCountTag.innerText = followingsCount
    })  
</script>
```

---



### 좋아요 (like)

- 좋아요 비동기 적용은 "팔로우와 동일한 흐름 + `forEach()` & `querySelectorAll()`"
  - index 페이지 각 게기슬에 좋아요 버튼이 있기 때문

















