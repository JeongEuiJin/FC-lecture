##Field tpyes(models)

###Field options
 1. null
  - 널값이 true 일때 db에 널값을 넣고 기본으로는 false로되어있다.
 2. blank
  - 널과는다르게 빈공간을 만든다
 3. choices
  - 미리 튜플로 db에 저장될 값을 지정을 해두고 사용자에게 선택을 할수있게 해준다
  - 실제 db에 저장될때는 뒤에 value을 저장이된다
 4. db_column
  - 열필드의 이름을 지정해준다 지정하지 않을때는 필드이름을 그대로 따라간다
 5. db_index
  - true일때 db에 목차를 만든다
 6. db_tablespace
  - 테이블 명이 중복이 될때 사용할수있다
  - class Meta: db_tablespace = 'new_table_name'
 7. default
  - 기본값을 지정할수있다.
 8. editable
  - 모델 유효성을 건너뛴다...(모델 유효성 아직 잘모름)
 9. error_message
  - 에러가 발생했을때 나타내는 옵션(실습을 못해서 어려움)
 10. help_text
  - 도움말표시로 필드의 아래에 타나나서 도움을 준다
 11. primary_text
  - 기본키 기본적으로 자동생성을 해주며 true로 해서 따로 지정도 가능하다
 12. unique
  - true가되면 인덱스생성을 의미하며 이 필드는 고유한 필드가되어 중복될수없다
 13. unique_for_date
  - DateField, DateTimeField로 설정하는값으로 고유한 값이 지정이된다
 14. unique_for_month
  - 13.번과 같은데 달만 고유하다
 15. unique_for_year
  - 14.번과 같다
 16. verbose_name
  - 필드의 이름을 지정할수있다. 지정하지않으면 변수이름으로 지정된다
 17. validators
  - 필드의 유효성 검사기
###Field tpyes
 1. AutoField
  - 자동으로 생성이되는 필드로 기본키가 생성이된다.
 2. BigAutoField
  - 64비트 정수 필드 기본키와 유사하다
 3. BigIntergerField
  - 64비트 정수필드로 기본양식위젯은 TextInput(먼말인지...)
 4. BinaryField
  - 바이트 단위만 지원(왜쓰지..?)
 5. BooleanFiled
  - 참,거짓 필드
  - Null을 사용하고싶다면 NullBoolField로 사용
  - 기본값으로는 None값이다
 6. CharField
  - 받드시 안에 max_length를 지정
  - 문자열을 받는 필드 TextInput으로 받으며
  - 더 큰 글을 받기위해서는 TextField를 사용
 7. CommaSeparatedIntergerField
  - CharField와 마찬가지로 max_length를 받는 정수 필드이다
  - (나머지 는 잘모르겠음.....)
 8. DateField
  - 날짜를 표기해주는것
  - DateField.auto_now : 수정되는 시간을 저장
  - DateField.auto_now_add : 생성되는 시간을 저장
  - blank=True로 빈값을 넣을수도있다.
 9. DateTimeField
  - 8.번과 같다
 10. DecimalField
  - 십진수로 소수점을 나타내는 필드로보임
  - 매개변수에 max_digits,decimal_pleaces가 있음
  - max_digits : 십진수로 몇자리를 나타냄
  - decimal_pleaces : 소수점자리 몇자리를 나타냄
 11. DurationField
  - 일정시간간격으로 모델링한 데이타를 저장(??)
 12. EmailField
  - 이메일 형식으로 데이타필드 작성
 13. FileField(upload_to = None,max_lengh=100)
  - 파일 업로드필드
  - uploade_to : 파일경로를 적어주면되고 뒤에 날짜 형식을 지원하지만 적어주지 않으면 업로드한 날짜/시간으로로 대체
  - 
 14. FilePathField
  - 파일 경로 설정
 15. FloatField
  - 부동소주점 설정 필드
 16. ImageField
  - 이미지 업로드를 할수잇고 길이와 폭을 지정할수있다
 17. IntergerFiled
  - 정수 타입필드
 18. GenericIPAddressField
  - 아이피를지정할수잇는 필드
  - IPv4,v6모두 지원
 19. NullBooleanFiled
  - 불필드작성할때는 null값을 이 형식을 사용해야된다.
 20. PositiveIntegerField
  - 0~2146483647정수만 받는다
 21. PostiveSmallIntegerField
  - 0~32767사이의 정수만 받는다
 22. SlugField
  - 글의 밑줄을 그어서 보통 URL을 사용할때 한다
 23. SmallIntergerField
  - -32768~32676	 값을 받는다
 24. textField
  - 텍스트 필드로 긴 문자열을 받을 사용
 25. TimeField
  - datefield와 유사함
 26. URLField
  - charfield에서 URL을 위해 사용한다
 27. UUIDField
  - (어떤타입같은데 예제를 봐도 잘모르겟다..._

###Relationship Fields
 1. ForeignKey
  - 일대 다 를 구현할때 사용
  - 옵션 :
  - CASCADE : 계단식으로 하위 삭제
  - PROTECT : 삭제를 방지할때 사용
  - SET_NULL : 외래키에 null값을 사용할때 설정
  - SET_DEFAULT : 외래키를 기본으로 지정
  - SET : 다른 모듈의 외래키를 사용하고싶을때 사용
  - DO_NOTHING: 아무것도 하지 않을때
  - related_name="%(app_label)s_%(class)s_related",
app_label 지금 동작하는 app이름
class 자식클래스의 이름
역참조
m.car_set 요거를 바꿈


related_query_name="%(app_label)s_%(class)ss",
정방향으로 들어가면서 역첨자로르 할때
 2. ManyToManyField
  - 
 3. OneToOneFiled
  - 

###Field Attribute reference
 1. Attributes for fields
  - 
 2. Attributes for fields with relations
  - 