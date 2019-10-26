# Django 

## (1) Django 설치하기

1. python version 확인
```
python --version
```

2. python의 가상환경(Virtual Environment)을 간단하게 사용할 수 있는 virtualenv 모듈 설치
```
pip install virtualenv pylint autopep8
```

3. Django를 사용하기 위한 환경 셋팅
```
mkdir server
cd server
virtualenv venv
```
위의 코드를 실행했을 때 아래와 같은 글이 나오면 성공
Installing setuptools, pip, wheel...
done. 

4. 가상환경 활성화
```
source venv/bin/activate
```

5. Django 설치
```
pip install django
```

5. +) 잘 설치되었는지 확인
```
django-admin --version
```

6. 설치된 개발환경 파일로 저장
```
pip freeze > requirements.txt
```

7. 설치가 완료되면 가상환경 종료
```
deactivate
```


## (2) Django 셋팅

1. 프로젝트 생성
```
django-admin startproject django_exercise
```

2. Django 구조 
(생성한 프로젝트는 django_exercise의 하위 파일)
* settings.py : 전반적인 장고의 설정을 가지고 있는 파일
* urls.py : 프로젝트의 url을 관리하는 파일
* wsgi.py : 웹서버와 연동하기 위한 파일
* manage.py : 프로젝트 관리 (DB의 migration 생성 및 실행, 로컬에서 웹서버 가동 등)

3. settings.py 파일 수정 (108, 114 line)
```
TIME_ZONE = 'Asia/Seoul'
USE_TZ = False
```

4. static 파일을 다루기 위해 STATIC_ROOT 파일 추가
```
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
```

5. Django 테스트 웹서버 실행
```
python manage.py runserver
```

## (3) Django 어플리케이션 생성

1. 경로 (/Users/gimbogyeong/server/django_exercise)
```
python manage.py startapp blog
```

2. 어플리케이션 등록
- 장고 어플리케이션을 생성하였으니, 장고 프로젝트에 새로 생성한 어플리케이션을 등록해야한다.
- 장고 프로젝트를 관리하는 django_exercise/settings.py를 열고 어플리케이션 등록
```
INSTALLED_APPS = [
.
.
.
'blog'
]
```
제일 밑에 새로 만든 어플리케이션인 blog를 추가해준다.



