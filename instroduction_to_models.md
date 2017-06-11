##models

테이블을 만드는곳이라고 보면될거같다

class로 만들면 테이블이 되고 이 안에 필드를 생성할수있다

```
class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
```

위와 같이 테이블을 만들어지고 필드가 각각 생성이 되는것이다

이렇게 작성이 된것은 DB로 데이타를 저장 , 수정 ,삭제를 할수있다.

데이타 값을 넣어주기위해서는 shell에서 가능하며
방법은

Person.objects.create(first_name=' xx',last_name='yyy')로 입력가능하고

xxx = Person(first_name='xxx')로도 가능함 두개의 차이는

create를 했을경우 DB에 바로 저징이 되며 xxx변수에 테이블이 직접추가하되 shell안에서만 가지고있는 데이타로 DB에는 반영이 되지 않는다 반영을 시켜주기위해서는 xxx.save()를 해주어야한다.

tip. dir(xxx) 를 했을때 xxx. 뒤에 어떤 것들이 사용할수있는지 목록을 보여준다.


- 필드에는 옴셥을 줄수가있다. 여러가지 있지만 null, blank가 대표적이며 사용하는이유는 항목에 null값을 줄수가있으며 공백으로 생성할수가있다.

- 필드에서 레코드를 생성할때 미리 지정되어있는 값들로 받아서 저장할수가있다.( choice)

- 기본키는 자동으로 생성이 되며 직접설정도 가능하다 하지만 뭐 쓸필요가 크게 없을거같다

- 필드이름은 변수명을 기본으로 하지만 내가 직접 정의가 가능하다
 model.CharField('이름',max_length=30) 이렇게 지정이 가능하다
 model.Foreignkey(verbose_name='이름',poll,on_delete=models.CASCADE)로 verbose_name로 지정해야한다
 
지금까지 db에서 사용되는것들의 대해서 알아봤으면 아래에서 부터는 RDB를 설명한다

서로의 DB를 연결하여 사용할수있게 해주는것으로 기본키와 외래키를 사용한다

1. many to one
 - 기본적인 구조로 일대 다 관계로 1테이블에서 2테이블연관지어 사용할수있게해준다.
 - 1번 테이블의 기본키를 불러와 사용함
 - 사용시에는 반드시 필드값은 들어가야되며 models.ForeignKey(테이블명,on_delete=CASCADE)로 지정한다
 - 옵션으로 on_delet=CASCADE는 이 키가 삭제될때 다 삭제가 된다라는것을 명시해준다
 - shell에서 사용방법 : s = 1테이블.objects.create(~~~)
   	2테이블.objects.create(name='xxx',foreign=s)
   이런식으로 사용한다
2. many to many
 - 다 대 다 관계로 사용할때 두개의 테이블중 models.ManyToManyField를 더 큰그룹에 사용?
 - 무튼 사용을 하게되면 두개 테이블이 아닌 또 다른 테이블이 DB에서 생기기된다 이때 테이블 명은 두개를 합친 이름으로
 - 각각의 id 값으로 이뤄진 테이블이 한개 생성이된다./Users/jeong-eui-jin/Desktop/FC-Lecture/field_types.md
 - 이렇게 생성이된 테이블은 양쪽을 이어주는 중간자역할을 하게된다
 - 중간자가 생성이되면 중간자를 사용을 할수는 있지만 추가나 변경을 하지 못한다
 - 중간자를 내마음대로 변경을 하기위해서 through로 지정하여 클래스 생성해준다
 - 생성한 클래스가 중간자로 되며 변경이 가능하게된다
3. one to one

모델 상속

1. abstract로 상속(ABC)
 - class Meta:에 abstract=True로 주게되면 해당 테이블은 자식테이블에 상속이되며 DB에존재하지 않고 자식테이블에서 필드를 사용할수가있다.
 - abstract = 옵션을 주면 테이블이 생성되지않는다
그렇지만 상속받은 자식에서는 부모의 것을 상속받는다
또한 meta클래스안에 있는것들은 abstract와 db_table는 상속이 되지않고 나머지는 상속이 가능하다
ordering상속가능

 - ```
related_name="%(app_label)s_%(class)s_related"
```
app_label 지금 동작하는 app이름
class 자식클래스의 이름
역참조
m.car_set 요거를 바꿈


 - ```
related_query_name="%(app_label)s_%(class)ss",
```
정방향으로 들어가면서 역첨자로르 할때

2. o2o으로 직접 상속하는 방법


모르는 부분 
proxy, multiple 상속,
