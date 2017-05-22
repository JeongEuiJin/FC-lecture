##SQL
관계형 데이타베이스
Mysql,sql server , access...등등
테이블로 정의가 되어있다.


##Syntax
 - 구분자 : 정의
 - 칼럼 데이타 값을 열로 정리?
 - 레코드 : 데이타값
 - 대소문자 구분하지 않는다
 - 한문장이 끝나면 ' ; ' 사용한다.

 - sql commands
  - select : 데이타 값을 가지고올때
  - update : 데이타값을 업데이트할때
  - delete : 데이타값을 삭제할때
  - insert into : 데이타를 기록할때
  - create database : 데이타베이스 만들때
  - alter database : 데이타베이스 값을 변경
  - crate table :테이블 새로 만들때
  - alter table : 테이블 수정할때 구조를 변경
  - drop table : 테이블 값 삭제할 때
  - crate index : 검색할 떄 필요한 인텍스 만들어줌
  - drop index : 인텍스 삭제

##select

 - 데이타베이스안의 데이타를 불러올때
 - select (  ) from (table)

##select -distinct

 - 유일한 값을 가지고오겠다
 - select distinct ( ) form (table)

##where

 - 조건을 주어 추출하기위한 명령어
 - select ( ) from (Table) where( )
 - 텍스트와 숫자
  - 텍스트는 ' '필요
  - 숫자는 그냥 숫자만 적어주면된다.
 - 연산자
  - = : 같다.
  - <> : 아니다.
  - between : 사이값
  - like :일부분만 일치
  - in : 두개이상값
 
##and or not

 - and : 두개 조건이 맞아야 출력
 - or : 두개 조건중 하나만맞아도 출력
 - not : 조건이 아닌 건들 출력

##order by

 - 정렬 키워드
 - select ( ) from (table) order by ( colum name1 , colum name 2)
 - asc / desc : 오름차순 /내림차순 - 옵션

##insert info

 - 새로운 레코드 삽입할때
 - insert info (table_name) values (값들)
 - 컬럼의 갯수(내용)에 맞게 작성이 되어야한다.
 - 컬럼을 순서대로 입력을 해야된다.
 - 컬럼네임을 지정해서 값을 입력할수있다.

##null values
 - 테이블에 옵션이 되어있다면 입력이 되어있지않으면 null로 저장
 - null 은 0 과 비교가 되지않는다
 - is not null 널값이 아닌것

##update
 - 기존데이타를 수정하기위해서
 - update (table) set ( ) where ( )
 - 어떤값을 바꿀건지 선택을 위해 반드시 where서야된다.
 - 바꿀 컬럼 = '바꿀 값',

##delete

 - 레코드 값을 지우기 위해
 - delete from (table) where ( )
 - 어떤 레코드를 선택을 할건지 반드시 지정 where

##select top
 - 테이블 값이 거대하거나 많을때 사용
 - sql , ms access 만 사용가능함
 - mysql 에서는 limit 숫자;
 - oracle 에서는 wher rownum <= 숫자;
 - percent를 지정할수있다

##min and max
 - min : 컬럼에서 제일 작은 값을 선택
 - max : 컬럼에서 제일 큰 값을 선택
 - select (min max)(value) from (table) where ();
##count, avg , sum

##like
 - where 절에서 사용
 - where () like 조건넣어주면 검색

##wildcards
 - where절 이하 like와 함께 사용
 - % _ [] [^ ] [!  ]
 - _ : 임의 문자하나
 - [] : 집합 범위
 - [^ ] , [! ] : 매치 되지 않는

##in
 - where 절에서 사용
 - where ( ) in (value1, value2..)
 - or?랑 비슷해보임

##between
 - where 절에서 사용
 - 범위 중에서 값을 선택
 - where ( ) between ( ) and ( )
 - 두개 사이 값중의 레코드 선택
 - not between 사용가능 사이로 시작하지 않는 값들 선택
 

##aliases
 - as 테이블 칼럼네임을 바꿔서 사용
 - select ( ) as () from (table)
 - select ( ) from(table)
 - 조합을 해서 사용할수도있다.
 - 명칭 지정할수있다

##joins
 - 두개 이상의 테이블에서 공통의 컬럼을 통하여 데이타를 가져올때 사용한다.
 - on = where

##inner join
 - join의 일반적인 형태

##left join
 - left 레이블 과 공통분모를 다가져온다

##right join
 - right 레이블 과 공통분모를 다 가져온다
 - left와 반대개념이다

##full join
 - left , right join을 다 합친것
 - * 과 무슨차이가있지 ;;??
 - 다 가져와서 조인시킨다는의미로보임

##self join

##union
 - 각각의 컬럼의 수가 같아야된다 
 - 칼람의 데이타타입이 같아야된다
 - select 구문으로 된것들을 union으로 묶는다
 - 중복된값을 제외하고 가져오고 모든값을 가져오기위해서는 all을 붙이면된다.

##group by

##having

##exists

##any all

##select into
 - 하나의 테이블로 부터 다른 테이블을 만들때 사용
 - select () into (new table) from (table)
 - into () in 백업복사할떄 사용

##insert into select
 - 존재하는 테이블에서 데이타를 가져와서 기존 테이블에 추가한다
 - insert into () select * from (table)
 - 
##comments


##create db
 - create database ();

##drop db
 - 이미 만들어진 drop database를 사용하면 제거가된다

##create table
 - create table (
 - 컬럼 네임 ,data_typ
 - )
 - create table
 - ( personID int,
 - lastname vachar(255),...)
 - insert into를 통하여 값을 입력
 
##drop table
 - 테이블을 지울때 사용
 - drop table
 - truncate table 테이블을 지우고 다시 똑같은 구조로 만들때 사용

##alter table
 - 이미 만들어진 테이블 내에서 수정할 떄 사용
 - alter table(table)
 - add column_name datatype
 - drop column (name)
 - 

##constraints
 - 제약사항 create table 만들때 지정할수있음
  - not null : 입력을 반드시 해야댐
  - unique : 중복되는 값이 있으면안될때
  - primary key : 레코드 한컬럼만 지정
  - foreign key : 가져오는 값
  

##not null
 - create table 할 떄 사용
 - 레코드 만들 때 not null을 사용하여 만들수있다
 - 사용 시 반드시 값이 들어가야된다
##unique
 - 유일한 값
 - 하나이상의 칼럼에 지정가능
 - atlter talbe 기존에 있던 테이블에 넣을때
 - add unique(ID)
 - 제거할때  - drop index (ID)

##primary key
 - null 값을 가질수없다
 - 테이블당 하나의 키이다
 - 테이블을 생성시 컬럼에 primary key 설정
 - 기존테이블에 추가 할 떄 add primary key(id)
 - 삭제할 때 drop primary key(id)

##foreign key
 - 외래키 다른 테이블의 primary key와 연결된다


##check
 - table만들때 컬럼 체크를 사용할수있다
 - check(ID >0)조건을 걸수있다

##default
 - 컬럼에 들어갈것을 기본으로 정해준다
 - 테이블 만들 때 컬럼에 default값을 지정

##index
 - 색인 찾기위한 용도
 - 업데이트를 할 때 느려질수있다
 - create index() on (table) (index)
 - 검색이 자주일어나는 곳에 지정

##auto increment
 - 컬럼에 지정하는것으로 유일한값으로 지정하여 숫자를 넣어준다

##views
 - 결과 가상테이블
 - 모든 select 사용가능하다
 - create view (table) as select ....
 - 업데이트 제거
  - create or replace view () as ()
  - drow view ()
 

##injection
 - sql 구문을 활용하여 데이타를 수정하는 것
 - sql parameters를 사용 추천
 - 
##hosting

##ms access functions

##mysql functions

##sql server functions

##oracle functions

##dates function
 - now() : 현재 날짜와 시간을 반환
 - curdate() : 현재 날짜 년 월 일
 - curtime() : 현재 시간 시 분 초
 - date() : date /time 날짜 부분만 추출한다
 - extract(unit date) : 한부분씩만 추출하고싶을 때
 - date_add() : 주어진 날짜에서 추가
 - date_sub() : 빼주는것

##null functions
 - isnull() : null값을 특정값으로 대체
 - nvl() :
 - ifnull() :
 - coalesce() :

##operators
 - & : and
 - | : or
 - ^ : COR
 - = : 같다
 - <> : 같지않다.
 - 

##data type

##db data types

##quick ref