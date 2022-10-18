# Django-Seed 사용법

1. pip 설치

​		pip install django-seed

​		pip install psycopg2       -->       Mac에서는 추가로 어떤것들 설치해야됨

2. APP 등록

```python
# settings.py
INSTALLED_APPS = [
    ...,
    'django_seed'			# 추가하기
]
```

3. 데이터 등록

```
$ python manage.py migrate
$ python manage.py seed articles --number=20
```

