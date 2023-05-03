# Tanstack Query



### Tanstack Query (=React Query)

- 서버 상태(server state)를 관리하는 라이브러리
- 서버 상태
  - 원격에 위치한 공간에 저장되며 앱이 소유하거나 제어하지 않는다
  - 데이터를 가져오고 업데이트하기 위해선 비동기 API가 필요하다
  - 다른 사람과 함께 사용하며, 내가 모르는 사이에 업데이트 될 수 있다
  - 앱에서 사용하는 데이터가 "유효 기간이 지난" 상태가 될 가능성을 가진다



#### Tanstack Query의 역할

- 캐싱
- 서버 데이터 중복 호출 제거
- 만료된 데이터를 백그라운드에서 제거하기
- 데이터가 언제 만료되는지 알고 있기
- 만료된 데이터는 가능한 빨리 업데이트하기
- 페이지네이션, 레이지 로딩 데이터의 성능 최적화
- 서버 상태의 메모리 관리 및 가비지 컬렉션
- 쿼리 결과의 구조 공유를 통한 메모이제이션



### Tanstack Query 사용 방법

#### 라이프사이클

- **fetching** - 요청 중인 쿼리
- **fresh** - 만료되지 않은 쿼리. 컴포넌트가 마운트, 업데이터 되어도 데이터를 다시 요청하지 않는다
- **stale** -  만료된 쿼리. 컴포넌트가 마운트, 업데이트되면 데이터를 다시 요청한다
- **inactive** - 사용하지 않는 쿼리. 일정 시간이 지나면 가비지 컬렉터가 캐시에서 제거한다
- **delete** - 가비지 컬렉터에 의해 캐시에서 제거된 쿼리



#### Important Defaults

- `useQuery`(, `useInfiniteQuery`)로 가져온 데이터는 기본적으로 **stale** 상태
  - `staleTime` 옵션으로 데이터가 **stale** 상태로 바뀌는데 걸리는 시간을 늘릴 수 있다.
- **stale** 쿼리는 다음 경우에 백그라운드에서 다시 가져온다
  - 새로운 쿼리 인스턴스가 마운트되었을 때
  - 브라우저 윈도우가 다시 포커스되었을 때
  - 네트워크가 다시 연결되었을 때
  - `refetchInterval` 옵션이 있을 때
- 활성화된 `useQuery`, `useInfiniteQuery` 인스턴스가 없는 쿼리 결과는 **inactive** 라벨이 붙으며 다음에 사용될 때까지 남아있는다.
  - **inactive** 쿼리는 300초(5분) 후에 메모리에서 해제된다.
- 백그라운드에서 3회 이상 실패한 쿼리는 에러 처리된다.
  - `retry` 옵션으로 쿼리 함수에서 오류 발생시 재시도할 횟수, `retryDelay` 옵션으로 재시도 대기 시간을 설정
- 쿼리 결과는 memoization을 위해 structure sharing을 사용하며 데이터 reference는 변경되지 않는다
  - immutable.js에서 사용하는 기술
  - 99.9% 케이스에서는 이 옵션을 끌 필요가 없음
  - structural sharing은 JSON 호환 데이터에만 적용되며, 다른 타입의 쿼리 결과는 항상 변경되었다고 판단



#### `QueryClientProvider` 설정

- 캐시 관리를 위해 `QueryClient` 인스턴스를 사용
- 컴포넌트가 `useQuery` 훅 안에서 `QueryClient` 인스턴스에 접근할 수 있도록 `QueryClientProvider`를 컴포넌트 트리 상위에 추가해줘야 한다

```react
import { QueryClient, QueryClientProvider } from 'react-query'

const queryClient = new QueryClient()	// 인스턴스 생성

function App() {
  return <QueryClientProvider client={queryClient}>...</QueryClientProvider>
}
```



#### `useQuery`로 서버 데이터 가져오기

- 서버에서 데이터를 가져오고 캐싱을 하는데 사용하는 기본이며 가장 많이 사용하게 되는 훅

```react
const { data, isLoading } = useQuery(queryKey, queryFunction, options)
```

- `queryFunction`에는 서버에서 데이터를 요청하고 Promise를 리턴하는 함수를 전달
  - 즉, `axios.get(...)`, `fetch(...)` 등을 리턴하는 함수
- `queryKey`에는 문자열과 배열을 넣을 수 있다.
  - 쿼리 키가 가지는 유연함이 곧 캐싱 처리를 쉽게 만듦
  - 쿼리 키가 다르면 캐싱도 별도로 관리하기 때문

```react
// 객체 필드의 순서가 달라도 내용이 같으면 같은 키로 취급
useQuery(['todo', { preview: true, status: 'done' }], ...)
useQuery(['todo', { status: 'done', preview: true }], ...)
```

- 리턴 데이터
  - `data` - 쿼리 함수가 리턴한 Promise에서 resolve된 데이터
  - `isLoading` - 저장된 캐시가 없는 상태에서 데이터를 요청중일때 `true`
  - `isFetching` -  캐시가 있거나 없거나 데이터가 요청중일때 `true`
- 옵션
  - `cacheTime` - unused 또는 inactive 캐시 데이터가 메모리에서 유지될 시간. 기본값은 5분이며 설정한 시간을 초과하면 메모리에서 제거됨
    - `Infinity`로 설정하면 쿼리 데이터는 직접 캐시를 무효화할때까지 fresh 상태로 유지됨
    - 캐시는 메모리에서 관리되므로 브라우저 새로고침 후에는 다시 가져온다
  - `enabled` - `false` 값이 전달되면 쿼리가 비활성화된다
    - 데이터 요청에 사용할 파라미터가 유효한 값일 때만 `true`를 할당하는 식으로 활용 가능!!
  - `onSuccess` - 쿼리 함수가 성공적으로 데이터를 가져왔을 때 호출되는 함수
  - `onError` - 쿼리 함수에서 오류가 발생했을 때
  - `onSettled` - 쿼리 함수의 성공, 실패 두 경우 모두 실행
  - `keepPreviousData` - 쿼리 키(ex. 페이지 번호)가 변경되어서 새로운 데이터를 요청하는 동안에도 마지막 `data`값을 유지
    - 페이지네이션을 구현할 때 유용하다. 캐시되지 않은 페이지를 가져올 때 화면에서 목록이 사라지는 깜빡임 현상을 방지할 수 있다.
    - `isPreviousData` 값으로 현재의 쿼리 키에 해당하는 값인지 확인 가능
  - `initialData` - 캐시된 데이터가 없을 때 표시할 초기값. `placeholder`로 전달한 데이터와 달리 캐싱이 된다. 브라우저 로컬 스토리지에 저장해 둔 값으로 데이터를 초기화할 때 사용가능
  - `refetchOnWindowFocus` - 윈도우가 다시 포커스되었을 때 데이터를 호출할 것인지 여부. 기본값은 `true`



#### `useMutaion`으로 서버 데이터 업데이트

- 서버 데이터를 가져오는 것은 reactive하게 동작하는 `useQuery`훅을 사용
- 서버 데이터 업데이트(생성/수정/삭제)는 `useMutaion`훅을 사용

```react
const mutaion = useMutation(newTodo => axios.post('/todos', newTodo))

const handleSubmit = useCallback(
  (newTodo) => {
    mutation.mutate(newTodo)
  },
  [mutaion],
)
```

- `onSuccess`, `onError`, `onSettled` 콜백을 전달 가능하며 mutate를 호출했을 때 실행할 `onMutate` 콜백도 사용 가능
- Redux를 사용한다면 리퀘스트 성공 액션을 미들웨어에서 확인하여 추가 액션을 실행 가능
  - `useMutation`을 사용한다면 `onSuccess` 콜백을 사용해도 되지만, 코드 가독성을 위해 `mutateAsync` 함수를 사용 가능

```react
const muation = useMutation(newTodo => axios.post('/todos', newTodo))

const handleSubmit = useCallback(
  async (newTodo) => {
    await mutaion.mutateAsync(newTodo)
    setAnotherState()
    dispatch(createAnotherAction())
  },
  [mutation]
)
```



#### 쿼리 무효화(Invalidation)

- 쿼리 데이터가 stale 상태로 바뀌기만을 기다릴 수 없는 경우 사용
- 예시)
  - 게시글에 댓글을 작성한 후 서버에서 댓글 목록을 다시 가져올 필요가 있음
  - 이와 같이 지정한 `staleTime`이 지나기 전에 직접 쿼리를 무효화해서 데이터를 새로 가져오도록 해야함

```react
const queryClient = useQueryClient();

// 캐시에 있는 모든 쿼리를 무효화
queryClient.invalidateQueries()

// todo로 시작하는 모든 쿼리를 무효화 ex) ['todos', 1], ['todos', 2], ...
queryClient.invalidateQueries('todos')

// ['todos', 1] 키를 가진 쿼리를 무효화
queryClient.invalidateQueries(['todos', 1])
```

- `predicate` 옵션을 사용하면 무효화할 쿼리를 더 자세하게 설정 가능

```react
// 쿼리 키 배열의 두번째 객체의 version 필드의 값이 10 이상인 쿼리만 무효화
queryClient.invalidateQueries({
  predicate: query =>
    query.queryKey[0] === 'todos' && query.queryKey[1]?.version >= 10,
})

// 위의 코드로 무효화된다
const todoListQuery = useQuery(['todos', { version: 20 }], fetchTodoList)

// 위의 코드로 무효화되지 않는다
const todoListQuery = useQuery(['todos', { version: 5 }], fetchTodoList)
```

















#### 출처

https://blog.rhostem.com/posts/2021-02-01T00:00:00.000Z

