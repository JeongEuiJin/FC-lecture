##Making Quires
filter 일치하는것을 찾아라

exclude 일치하지않는것을 찾아라

1. p = Person(name = 'Fred Flintstione',shirt_size = 'L')
       p.save()

2. p2 = Person.objects.create(name= 'Lux', shirt_size = 'S')
두개 차이는 shell안에서 만 데이타를 가지고있다가 세이브를 하면 데이타베이스에 기록이 되고 아래 것은 만들면서바로 등록이 되는것이다.

 - filter사용
 - 변수를불러온다 변수내용을 찾기위해서 __두개를 사용해서 매개변수를 다시 불러온다음 = 찾는다
 - 다중필터 가능
```
 >>> Entry.objects.filter(
...     headline__startswith='What'
... ).exclude(
...     pub_date__gte=datetime.date.today()
... ).filter(
...     pub_date__gte=datetime(2005, 1, 30)
... )
```
 - 2005,1,30부터 현재까지 사이의 What로 시작하느것을 찾느것이다
- gte gt lte 이런게 머지?
 - gte = 크거나 같을때
 - gt = 초과
 - lt = 미만
 - lte = 작거나 같을때
- get은 한가지를 가지고온다.
- querysets.offset
 - 슬라이스로 사용가능하지만 -1과같은 값은 사용이되지않는다
 - Enty.objects.all()[:10:2]
 - 몇번째를 가지고오는가를 설정할수있다.
- exact :일치하는것 Entry.objects.get(headline__exact='xxxx')
- iexact 대소문자를 가리지않고 검색
- contains : sql에서 like와 같음
- 외래키로 연결되어있으면 서로 다른 테이블의 내용을 가지고올수있다.
 - Blog.objects.filter(entry__authors__name='lennon'
 - 개체를 찾을 때 오류없이 반환을 하고싶을때 필터링에 옵션을 지정한다
 - Blog.objects.filter(entry__authors__name__isnull=True)
 -  필터안에서 또 필터를 걸수가있다.
 -  이때 
  - ```Blog.objects.filter(entry__headline__contains='Lennon',entry__pub_date__year=2008)```
  - 과
  - ```Blog.objects.filter(entry__headline__contains='Lennon').filter(entry__pub_date__year=2008)```
  - 는 차이가 있다. 위에것은 필터를 앞서한것에대해 또한번 필터를 하고
  - 두번째는 각각 필터를 하고 and연산을 한다
- F 쿼리를 사용
 - 필더안의 값을 꺼내와서 비교할때 사용한다
- PK에 바로가기
 - id , pk , id_exact를 사용한다
- caching and querysets	
 - 미리 선택할것을 저장해둔다
- Q object
 - 원하는 연사자를 사용을 할수있다.
 - , and연산
 - | or연산
- object 비교하기
 - == 표현한다
- 삭제 object
- copying model
 -  id값이 중복이 되지 않는다는것을 이용하여 복제
 - update로 할수도있다.
- Related objects
 -  