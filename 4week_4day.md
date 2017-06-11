##장고 초기 설정

- 폴더 만드는 법 -
- django / (djang-project-name) 여기에서 1.2번을 설정한다

1. pyenv설정
 - 버전에 맞게 설정
 - pyenv virtualenv (version) (name)
 - pyenv local (name)
 - 가상만든것을 활성화
 - pip list로 확인
 - pip install django설치
 - 설치 후 pip freeze > requirements.txt로 설치한 파일들을 리스트로 만든다
 - (유지보수시에 어떤 환경으로 설치하고 사용을 하지는 알수있다.)

2. 장고 설치
 - django/(django-project-name) 여기서 진행
 - django-admin startproject mysite 만들면 (django-project)안에 mysite/ 가 생성이되며 이 폴더아래에 또 mysite가 동일하게 만들어진다
 - 안쪽의 mysite는 장고 앱에서 수행이되는 폴더로 건들이지 않는다.
 - 바깥쪽(django-project)/mysite 이름을 django-app으로 변경
 - django-app으로 들어와서 manage.py를 확인
 - ./manage.py startapp (만들 앱이름) 생성

3. git추가
 - git은 (django-project-name) 안에서 설정
 - git init 을 실행
 - .gitignore 작성하여 현재폴더에 생성
 - https://www.gitignore.io/api/vim%2Cmacos%2Cdjango%2Cpython%2Cpycharm(macOS, Django, Pycharm,Python,Vim으로 생성)
 - git remote oring (git 에서 생성한 주소)
 - git push oring (git생성주소) master 

4. pycharm 설정
 - (django-procjet-name)폴더에서 charm .으로 pycharm실행
 - django-app을 루트 폴더로 지정
 - 환경설정 - 인터프리터를 지정 1.에서 생성한것을 지정


## 장고 시작
startapp으로 만든 폴더이름으로 polls생성
모든 코딩은 작성하고나면 리포메팅을 해주세요 (command + l로 설정해둠)

1. polls/view.py
 - from django.http import HttpResponse 직접 입력을 해주세요
 - 같은 단어로 되어있는것들이 많이 있어서 이런것들은 직접 선택입력
2. polls/urls.py를 생성
 - 기본적인 플랫폼 입력아래와 같다
 
```from django.conf.urls import url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
]
```
 - polls/url.py안에 작성이 되면 루트를 polls로 잡고 이안에 이동이 되면 매번 url를 생성을 해줘야되는데 비효율적이다
 - 일단은 polls로 가는 url을 mysite/urls에 polls로 가는 url을 지정해준다

3. mystie/urls
 - include를 하면 문자열로 넣을수있다.
 - from import로 as명칭을 지정하여 넣을수도있다.

4. polls/models.py
 - 필드에 사람이 읽을수있는 이름을 지정할수있다.
 - 변수이름으로 할수있지만 뒤에 ('한글')입력하여 변경할수도있다
 - max_lenght에는 반드시 숫자를 입력해주어야한다.

##DB
1. ./manage migrate로 생성
2. setting/instll_app에 polls앱을 추가
3. ./manage makemigration
4. db에 반영하기위해서 다시 migrate를 한다

