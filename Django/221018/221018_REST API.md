# 221018

## REST API

#### HTTP Request Methods

- 리소스에 대한 행위(수행하고자 하는 동작)를 정의
- **GET**
  - 서버에 리소스의 표현을 요청
  - GET을 사용하는 요청은 데이터만 검색해야 함
- **POST**
  - 데이터를 지정된 리소스에 제출
  - 서버의 상태를 변경
- **PUT**
  - 요청한 주소의 리소스를 수정
- **DELETE**
  - 지정된 리소스를 삭



#### [참고] 리소스 (resource)

- HTTP 요청의 대상을 리소스(resource, 자원)라고 함



#### HTTP response status codes

- 특정 HTTP 요청이 성공적으로 완료되었는지 여부를 나타냄
  1. Infromational responses (100-199)
  2. Successful responses (200-299)
  3. Redirection messages (300-399)
  4. Client error responses (400-499)
  5. Server error responses (500-599)



#### URI (Uniform Resource Identifier, 통합 자원 식별자)

- 인터넷에서 하나의 리소스를 가리키는 문자열
- **URL(Uniform Resource Locator, 통합 자원 위치)**
  - 자원의 **위치**로 자원을 식별
  - 웹에서 주어진 리소스의 주소
  - 네트워크 상에 리소스가 어디 있는지(주소)를 알려주기 위한 약속
    - HTML, CSS, 이미지 등이 될 수 있음
- **URN(Uniform Resource Name, 통합 자원 이름)**
  - URL과 달리 자원의 위치에 영향을 받지 않는 유일한 이름 역할을 함 (독립적 이름)
  - URL의 단점을 극복하기 위해 등장했으며 자원이 어디에 위치한지 여부와 관계없이 **이름**만으로 자원을 식별
  - 하지만 이름만으로 실제 리소스를 찾는 방법은 보편화 되어있지 않아 현재는 대부분 URL을 사



#### API (Application Programming Interface)

- 애플리케이션과 프로그래밍으로 소통하는 방법
  - 개발자가 복잡한 기능을 보다 쉽게 만들 수 있도록 프로그래밍 언어로 제공되는 구성
- API를 제공하는 애플리케이션과 다른 소프트웨어 및 하드웨어 등의 것들 사이의 간단한 계약(인터페이스)이라고 볼 수 있음
- API는 복잡한 코드를 추상화하여 대신 사용할 수 있는 몇 가지 더 쉬운 구문을 제공



#### Web API

- 웹 서버 또는 웹 브라우저를 위한 API
- API는 다양한 타입의 데이터를 응답
  - HTML, XML, **JSON** 등



#### REST (Representational State Transfer)

- API Server를 개발하기 위한 일종의 소프트웨어 설계 방법론
  - 2000년 로이 필딩의 박사학위 논문에서 처음으로 소개된 후 네트워킹 문화에 널리 퍼짐
- '소프트웨어 아키텍쳐 디자인 제약 모음' (a group of software architecture design constraints)
- REST 원리를 따르는 시스템을 **RESTful**하다고 부름
- REST의 기본 아이디어는 리소스, 즉 자원.
  - **자원을 정의하고 자원에 대한 주소를 지정하는 전반적인 방법을 서술**



#### REST에서 자원을 정의하고 주소를 지정하는 방법

1. 자원의 **식별**
   - **URI**
2. 자원의 **행위**
   - **HTTP Method**
3. 자원의 **표현**
   - 자원과 행위를 통해 궁극적으로 표현되는 (추상화된) 결과물
   - **JSON**으로 표현된 데이터를 제공



#### JSON

- JSON is a lightweight data-interchange format
- JavaScript의 표기법을 따른 단순 문자열
- 파이썬의 dictionary, 자바스크립트의 object처럼 C 계열의 언어가 갖고 있는 자료구조로 쉽게 변환할 수 있는 **key-value 형태의 구조**
- 사람이 읽고 쓰기 쉽고 기계가 파싱(해석&분석)하고 만들어내기 쉽기 때문에 현재 API에서 가장 많이 사용하는 데이터 타입

---

## Response Json

#### [참고] 'Content-Type' entity header

- 리소스의 media type (MIME type, content type)을 나타내기 위해 사용됨
- 응답 내에 있는 컨텐츠의 컨텐츠 유형이 실제로 무엇인지 클라이언트에게 알려줌



#### Serialization (직렬화)

- 데이터 구조나 객체 상태를 동일 혹은 다른 컴퓨터 환경에 저장하고, 나중에 재구성할 수 있는 포맷으로 변환하는 과정
  - Data --> Serialization --> Serialized data --> json 등 변
  - 즉, 어떠한 언어나 환경에서도 **"나중에 다시 쉽게 사용할 수 있는 포맷으로 변환하는 과정"**
- 변환 포맷은 대표적으로 json, xml, yaml이 있으며 **json**이 가장 보편적으로 쓰임



#### Serializers in Django

- Django의 **serialize()**는 Queryset 및 Model Instance와 같은 복잡한 데이터를 JSON, XML 등의 유형으로 쉽게 변환할 수 있는 Python 데이터 타입으로 만들어 



#### 1. HTML 응답

- 문서(HTML) 한 장을 응답하는 서버 확인하기
- 지금까지 Django로 응답 해오던 방식

```python
# articles/urls.py
urlpatterns = [
    path('html/', views.article_html),
]
```

```python
# articles/views.py
def article_html(request):
    articles = Article.objects.all()
    context = {
        'articles': articles,
    }
    return render(request, 'articles/article.html', context)
```



#### 2. JsonResponse()를 사용한 JSON 응답

- 이제는 문서(HTML) 한 장을 응답하는 것이 아닌 JSON 데이터를 응답해보기
- Django가 기본적으로 제공하는 JsonResponse 객체를 활용하여 Python 데이터 타입을 손쉽게 JSON으로 변환하여 응답 가능

```python
# articles/views.py
from django.http.response import JsonResponse

def article_json_1(request):
    articles = Article.objects.all()
    articles_json = []

    for article in articles:
        articles_json.append(
            {
                'id' : article.pk,
                'title' : article.title,
                'content' : article.content,
                'created_at': article.created_at,
                'updated_at' : article.updated_at,

            }
        )
    return JsonResponse(articles_json, safe=False)
```

- **JsonResponse()**
  - JSON-encoded response를 만드는 클래스
  - '**safe**' parameter
    - 기본 값 True
    - False로 설정 시 모든 타입의 객체를 serialization 할 수 있음
      (그렇지 않으면 dict 인스턴스만 허용됨)



#### 3. Django Serializer를 사용한 JSON 응답

- Django의 내장 **HttpResponse()**를 활용한 JSON 응답
- 이전에는 JSON의 모든 필드를 하나부터 열까지 작성해야 했지만 이제는 그렇지 않음

```python
# articles/views.py

from django.http.response import JsonResponse, HttpResponse
from django.core import serializers

def article_json_2(request):
    articles = Article.objects.all()
    data = serializers.serialize('json', articles)
    return HttpResponse(data, content_type='application/json')
```



#### 4. Django REST framework를 사용한 JSON 응답

- **Django REST framework (DRF)**
  - Django에서 Restful API 서버를 쉽게 구축할 수 있도록 도와주는 오픈소스 라이브러리
  - Web API 구축을 위한 강력한 toolkit을 제공
  - REST framework를 작성하기 위한 여러 기능을 제공
  - DRF의 serializer는 Django의 Form 및 ModelForm 클래스와 매우 유사하게 작동
  - https://www.django-rest-framework.org/

```
$ pip install djangorestframework
```

```python
# settings.py
INSTALLED_APPS = [
    ...,
    'rest_framework',
    ...,
]
```

```python
# aritcles/serializers.py
from rest_framework import serializers
from .models import Article

class ArticleSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Article
        fields = '__all__'
```

```python
# articles/views.py
@api_view(['GET'])
def article_json_3(request):
    articles = Article.objects.all()
    serializer = ArticleSerializer(articles, many=True)
    return Response(serializer.data)
```

---

## Django REST framework - Single Model

#### 사전 준비

- [Postman 설치](https://www.postman.com/downloads/)

  - API를 구축하고 사용하기 위한 플랫폼
  - API를 빠르게 만들 수 있는 여러 도구 및 기능을 제공

- 가상환경 생성, 활성화 및 패키지 목록 설치

- Article 모델 Migration 진행

  ```python
  # articles/models.py
  class Article(models.Model):
      title = models.CharField(max_length=100)
      content = models.TextField()
      created_at = models.DateTimeField(auto_now_add=True)
      updated_at = models.DateTimeField(auto_now=True)
  ```

- 준비된 fixtures 데이터 load

  ```
  $ python manage.py loaddata articles.json
  ```

- DRF 설치, 등록 및 패키지 목록 업데이트

  ```
  $ pip install djangorestframework
  ```

  ```python
  # settings.py
  INSTALLED_APPS = [
      ...,
      'rest_framework',
      ...,
  ]
  ```

  

#### ModelSerializer 작성

```python
from rest_framework import serializers
from .models import Article, Comment

class ArticleListSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Article
        fields = ('id', 'title', 'content', )
```

- ModelSerializer 클래스는 모델 필드에 해당하는 필드가 있는 Serializer 클래스를 자동으로 만들 수 있는 shortcut을 제공
  1. Model 정보에 맞춰 자동으로 필드를 생성
  2. serializer에 대한 유효성 검사기를 자동으로 생성
  3. **.create()** 및 **.update()**의 간단한 기본 구현이 포함됨

- ModelSerializer의 **'many'** option
  - 단일 객체 인스턴스 대신 QuerySet 또는 객체 목록을 serialize 하려면 many=True를 작성해야 함



#### `api_view` decorator

- DRF view 함수가 응답해야 하는 HTTP 메서드 목록을 받음

- DRF에서 **api_view** 데코레이터 작성은 필수
- 기본적으로 GET 메서드만 허용되며 다른 메서드 요청에 대해서는 405 Method Not Allowed로 응답



#### Raising an exception on invalid data

- "유효하지 않은 데이터에 대해 예외 발생시키기"
- is_valid()는 유효성 검사 오류가 있는 경우 ValidationError 예외를 발생시키는 선택적 raise_exception 인자를 사용할 수 있음
- DRF에서 제공하는 기본 예외 처리기에 의해 자동으로 처리되며 기본적으로 HTTP 400 응답을 반

---

## Django REST framework - N:1 Relation

#### Passing Additional attributes to `.save()`

- `save()` 메서드는 특정 Serializer 인스턴스를 저장하는 과정에서 추가적인 데이터를 받을 수 있음

- `CommentSerializer`를 통해 Serialize되는 과정에서 Parameter로 넘어온 `article_pk`에 해당하는 article 객체를 추가적인 데이터를 넘겨 저장

  ```python
  # articles/views.py
  @api_view(['POST'])
  def comment_create(request, article_pk):
      article = Article.objects.get(pk=article_pk)
      serializer = CommentSerializer(data=request.data)
      if serializer.is_valid(raise_exception=True):
          serializer.save(article=article)
          return Response(serializer.data, status=status.HTTP_201_CREATED)
  ```



#### 읽기 전용 필드 설정

- `read_only_fields`를 사용해 외래 키 필드를 **'읽기 전용 필드'**로 설정

- 읽기 전용 필드는 데이터를 전송하는 시점에 **'해당 필드를 유효성 검사에서 제외시키고 데이터 조회 시에는 출력'**하도록 함

  ```python
  # articles/serializers.py
  class CommentSerializer(serializers.ModelSerializer):
      
      class Meta:
          model = Comment
          fields = '__all__'
          read_only_fields = ('article',)
  ```



#### N:1 - 역참조 데이터 조회

1. **PrimaryKeyRelatedField()**

   - 기본 필드 override

   ```python
   # articles/serializers.py
   class ArticleSerializer(serializers.ModelSerializer):
       comment_set = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
       
       class Meta:
           model = Article
           fields = '__all__'
   ```

   - models.py에서 `related_name`을 통해 이름 변경 가능
   - 역참조 시 생성되는 `comment_set`을 override 할 수 있음 --> override시 `comments`로 사용해야함

2. **Nested relationships**

   ```python
   # articles/serializers.py
   class CommentSerializer(serializers.ModelSerializer):
       
       class Meta:
           model = Comment
           fields = '__all__'
           read_only_fields = ('article', )
           
   class ArticleSerializer(serilizers.ModelSerializer):
       comment_set = CommentSerializer(many=True, read_only=True)
       comment_count = serializers.IntegerField(source='comment_set.count', read_only=True)
       
       class Meta:
           model = Article
           fields = '__all__'
   ```

   - 모델 관계 상으로 참조된 대상은 참조하는 대상의 표현에 포함되거나 중첨(nested)될 수 있음
   - 이러한 중첩된 관계는 serializers를 필드로 사용하여 표현할 수 있음
   - 역참조하는 클래스가 밑쪽에 위치해야 함
   - **`source`**
     - serializers field's argument
     - 필드를 채우는 데 사용할 속성의 이름
     - 점 표기법(dotted notation)을 사용하여 속성을 탐색할 수 있음



#### [주의] 읽기 전용 필드 지정 이슈

- 특정 필드를 override 혹은 추가한 경우 `read_only_fields`가 동작하지 않으니 주의!!!!

```python
# 사용 불가능
class ArticleSerializer(serializers.ModelSerializer):
    comment_set = CommentSerializer(many=True)
    comment_count = serializers.IntegerField(source='comment_set.count')
    
    class Meta:
        model = Article
        fields = '__all__'
        read_only_fields = ('comment_set', 'comment_count')
```



#### URL과 HTTP requests methods 설계

|             |     GET      |  POST   |     PUT      |    DELETE    |
| :---------: | :----------: | :-----: | :----------: | :----------: |
|  articles/  | 전체 글 조회 | 글 작성 | 전체 글 수정 | 전체 글 삭제 |
| articles/1/ | 1번 글 조회  |    .    | 1번 글 수정  | 1번 글 삭제  |



```python
# articles/serializers.py
from rest_framework import serializers
from .models import Article, Comment

class ArticleListSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Article
        fields = ('id', 'title', 'content', )

class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ('article', )

class ArticleSerializer(serializers.ModelSerializer):
    # 역참조의 PK만 가져옴
    # comment_set = serializers.PrimaryKeyRelatedField(many=True, read_only=True)       
    
    # 역참조의 모든 정보를 가져옴
    comment_set = CommentSerializer(many=True, read_only=True)
    comment_count = serializers.IntegerField(source='comment_set.count', read_only=True)     

    class Meta:
        model = Article
        fields = '__all__'
```

```python
# aritlces/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('articles/', views.article_list),
    path('articles/<int:article_pk>/', views.article_detail),
    path('comments/', views.comment_list),
    path('comments/<int:comment_pk>/', views.comment_detail),
    path('articles/<int:article_pk>/comments/', views.comment_create),
]
```

```python
# aritcles/views.py
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from django.shortcuts import get_object_or_404, get_list_or_404

from .serializers import ArticleListSerializer, ArticleSerializer, CommentSerializer
from .models import Article, Comment

@api_view(['GET', 'POST'])
def article_list(request):
    if request.method == 'GET':
        # articles = Article.objects.all()
        articles = get_list_or_404(Article)
        serializer = ArticleListSerializer(articles, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'DELETE', 'PUT'])
def article_detail(request, article_pk):
    # article = Article.objects.get(pk=article_pk)
    article = get_object_or_404(Article, pk=article_pk)
    if request.method == 'GET':
        serializer = ArticleSerializer(article)
        return Response(serializer.data)
    
    elif request.method == 'DELETE':
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    elif request.method == 'PUT':
        serializer = ArticleSerializer(article, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)

@api_view(['GET'])
def comment_list(request):
    # comments = Comment.objects.all()
    comments = get_list_or_404(Comment)
    serializer = CommentSerializer(comments, many=True)
    return Response(serializer.data)

@api_view(['GET', 'DELETE', 'PUT'])
def comment_detail(request, comment_pk):
    # comment = Comment.objects.get(pk=comment_pk)
    comment = get_object_or_404(Comment, pk=comment_pk)
    if request.method == 'GET':
        serializer = CommentSerializer(comment)
        return Response(serializer.data)

    elif request.method == 'DELETE':
        comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    elif request.method == 'PUT':
        serializer = CommentSerializer(comment, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)

@api_view(['POST'])
def comment_create(request, article_pk):
    # article = Article.objects.get(pk=article_pk)
    article = get_object_or_404(Article, pk=article_pk)
    serializer = CommentSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(article=article)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
```

---

## Django shortcuts functions

#### shortcuts 목록

- django.shortcuts 패키지는 개발에 도움 될 수 있는 여러 함수와 클래스를 제

- render(), redirect(), **get_object_or_404()**, **get_list_or_404()**
- https://docs.djangoproject.com/en/3.2/topics/http/shortcuts/



#### get_object_or_404()

- 모델 manager objects에서 **get()**을 호출하지만, 해당 객체가 없을 땐 기존 DoesNotExist 예외 대신 Http404를 raise 함

```python
# articles/views.py
from django.shortcuts import get_object_or_404

article = Article.objects.get(pk=article_pk)
comment = Comment.objects.get(pk=comment_pk)

# 위 코드를 모두 다음과 같이 변경
article = get_object_or_404(Article, pk=article_pk)
comment = get_object_or_404(Comment, pk=article_pk)
```



#### get_list_or_404()

- 모델 manager objects에서 **filter()**의 결과를 반환하고 해당 객체 목록이 없을 땐 Http404를 raise 함

```python
# articles/views.py
from django.shortcuts import get_list_or_404

articles = Article.objects.all()
comments = Comment.objects.all()

# 위 코드를 모두 다음과 같이 변경
articles = get_list_or_404(Article)
comments = get_list_or_404(Comment)
```



#### Django shortcuts function 사용 이유

- 클라이언트 입장에서 원인이 정확하지 않은 에러를 마주하기 보다는, 서버가 적절한 예외 처리를 하고 클라이언트에게 올바른 에러를 전달하는 것이 중요



