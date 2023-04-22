# Flutter



#### 앱 디자인

- `Material` : AOS 디자인 -> 구글이 만들었기 때문에 더 좋다고 생각함
- `Cupertino` : IOS 디자인
- root widget에서는 둘 중 하나를 정해줘야함!!



#### `Life Cycle`

- `initState` : 빌드 이전에 호출되는 메서드로, 변수를 초기화하고 API 업데이트를 구독
- `dispose` : 위젯이 위젯 트리에서 제거될 때 호출되는 메서드로, 이벤트 리스너 같은 것들을 구독 취소
- `build` : 위젯에서 UI를 만듦

```dart
// initState는 항상 build 전에 사용되어야함!!
@override
void initState() {
	super.initState(); 
}

@override
void dispose() {
	super.dispose();
}

@override
Widget build(BuildContext context) {
	return 
}
```





#### `Transform`

```dart
Transform.scale()	// 아이콘 스케일 키우기
Transform.translate()	// 아이콘 이동시키기
```





