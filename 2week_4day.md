## pyhton

설치

- pyenv : 버전을 따로 분리해서 사용할수있게 해주는 도구
			버전을 관리
- virtualenv : 파이썬 패키지 설치 환경을 따로 관리
- ipython : 셸의 다양한 기능 패치

※ python -v 에서 system은 절대 건들면안됌
그래서 위의 pyenv , virtrualenv를 사용해서 관리

## 변수의 이름 제한

사용 가능한 문자

- 소문자 
- 대문자
- 숫자
- 언더스코어(__)

__ :는 잘 사용하지않는다

예약어로 지정되어있는 것은 변수로 사용할수없다.
-
False
class
finally
is
return
None
continue
for
lambda
try
True
def
from
nonlocal
while
and
del
global
not
with
as
elif
if
or
yield
assert
else
import
pass
break
except
in
raise
-

## 수학연산자
<br>

|연산자|	 설명  |예|	결과|
|----|------|---|---|
|  + | 더하기 |32 + 7|39|
|  - | 빼기	82| - 2|80|
|  * |	곱하기|	3 * 7|21|
|  / |	나누기|	7 / 2|	3.5|
|  //|	정수나누기|	7 // 2	3|
|  % |	나머지|	7 % 3|	1|
| ** |	지수	|2**10|1024|



## 슬라이스 연산자


[start:end:step]

-(숫자) : 왼쪽기준으로 뒷쪽으로 지정
사용방법 -> [1:4], [2:10:3] [::2]

## 문자 나누기(split)

test = 'a b c d'.split
 -> ['a','b','c','d']
 
## 문자 합치기(join)

' '.join(파일이름)

##List 만들기

 - abc = []
 - abc = ['def', 'ghi'...]


## 리스트 항목 추가


abc.append('e')
맨마지막에  e 추가가 됌

## 리스트 병합

파일1.extend(파일2)

파일1 뒤에 파일2 내용이 붙어서 나옴

## 시퀀스 타입


- 삭제 방법
 - 직접삭제  del.파일[0]
 - 선택삭제  파일.remove('리스트항목')
 - 리스타항목 삭제  파일.pop(몇번째 선택가능)
- 값으로 리스트 항목찾기(index,in)
 - 파일.index('리스트항목') : 어디있는지 알림
 - '리스트항목' in 파일 : 존재여부만 확인
- 리스트 카우트
 - 파일.count('red')


## 튜플


리스트와 다르게 지정하면 바뀌지 않는 값들 적은 메모리 사용

 - 형식 
  - abc = ()
  - abc = 'red' , <-반드시 뒤에 콤마를 찍어야 튜플로인식
  - abc = 'apple', 'banana'


## 딕셔너리

key - value 항목을 가지는 구조

 - 생성
  - 파일 = { }
  - 파일 = dict{}
  - 파일 = {'abc': '가나다','def':'마바사'...}
 - 항목 추가
  - 키 값을 넣고 = 값을 넣어준다
  - 파일['새로운 키']='값'
 - 결합(update)
  - 파일.update(값이있는 파일)
 - 삭제(del)
  - del 삭제할 파일[값]
- 모든 값들마다 얻기위한 명령어
 - dict파일.keys() : 키
 - dict파일.values() : 값
 - dict파일.items() : 키 , 값 모두 얻기
 
##셋(set)
 - dict와 같으며 중복된 값이 존재할수없다
 - set('값' 또는 dict.파일)

##if elif else(조건문)

- 조건문
if 조건1: <br>
elif 조건2: <br>
else: 조건 1,2 둘다 아닐경우

- 조건 표현식<br>
 참일경우 표현 if 조건문 else 거짓일경우 표현
 
 print('Good') if (true) else print('bad')
 
- 중첩 조건 표현식<br>
 print('good') if (true.1) if (true.2)...else print('bad')
    
 

##for (반복문)

-for 항목 in 순환 객체
-break 중단 할때
-continue 건너띄고 계속 진행할때
-else 

- range() : 0부터 숫자만큼 범위 값이 주어짐
- len(항목) : 몇개가있는지 구함
- zip(a,b) : 	두개의 리스트들 중 짧은 리스트에 맞춰서 갯수가 정해짐
- 
 
 