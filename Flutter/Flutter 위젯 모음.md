# Flutter 위젯 모음



#### 화면 새로고침 하는 방법

```dart
setState() {}
```



#### Scaffold -> AppBar

```dart
elevation: 		// box-shadow
backgroundColor: // 배경색
foregroundColor: // 글자색
```



#### 화면 로딩

```dart
Center(
  child: CircularProgressIndicator(),
);
```



#### 데이터 요청 (FutureBuilder)

```dart
FutureBuilder(
  future: webtoons,
  builder: (context, snapshot) {
    if (snapshot.hasData) {
      return ListView.builder(
        scrollDirection: Axis.horizontal,
        itemCount: snapshot.data!.length,
        itemBuilder: (context, index) {
          var webtoon = snapshot.data![index];
          return Text(webtoon.title);
        }
      )
    }
  }
)
// ListView.builder : 필요한 부분을 화면에 띄울 때에 맞춰서 아이템을 만들어줌 => 최적화 굳
    
// ListView.separated : 필요한 부분을 화면에 띄울 때에 맞춰서 아이템을 만들어주고, 각각 간격을 설정할 수 있음
'''
ex)
separatorBuilder: (context, index) => const SizedBox(
  width: 20,
),
'''
```



#### Expanded

```dart
// 화면의 남는 공간을 차지하는 widget
Expanded(child: child)
```



#### Container

```dart
// 화면을 꾸밀때 사용
Container(
  width: 250,
  margin: EdgeInsets.only(bottom: 10),		// 마진 속성!!
  clipBehavior: Clip.hardEdge, // 자식이 부모의 영역을 침범해서 스타일이 안먹을때 사용
  decoration: BoxDecoration(
    borderRadius: BorderRadius.circular(10),
    boxShadow: [
      BoxShadow(
        blurRadius: 5,
        offset: const Offset(0, 0),
        color: Colors.black.withOpacity(0.5),
      )
    ]
  ),
  child: Image.network(webtoon.thumb),
)
```



#### GestureDetector

```dart
// 버튼 클릭 느낌 : onTap
// Navigator.push : StatelessWidget을 애니메이션 효과로 감싸서 스크린처럼 보이게 해줌
// MaterialPageRoute : StatelessWidget을 라우트로 감싸서 다른 스크린처럼 보이게 만들어줌
GestureDetector(
  onTap: () {
    Navigator.push(
      context, MaterialPageRoute(
        builder: (context) =>
            DetailScreen(title: title, thumb: thumb, id: id),
        ));
  },
)
```



#### Hero

```dart
// tag로 매칭된 요소를 가지고 오는 듯한 느낌의 애니메이션을 줌
Hero(
  tag: id,
  child: Container(
    width: 250,
    clipBehavior: Clip.hardEdge,
    ...
  )
)
```



#### SingleChildScrollView : 스크롤 만들기

```dart

```



#### Padding

```dart
Padding(
  padding: EdgeInsets.symmetric(
    horizontal: 50,
    vertical: 50,
  )
)
```



#### launchUrlString : 다른 url로 보내버리기

```dart
// 웹의 a 태그와 유사
onButtonTap() async {
  await launchUrlString(
    "https://google.com"
  );
}
```

