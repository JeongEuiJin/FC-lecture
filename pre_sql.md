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

##wildcards

##in

##between

##aliases

##joins

##inner join

##left join

##right join

##full join

##self join

##union

##group by

##having

##exists

##any all

##select info

##insert into select

##comments


##create db

##drop db

##create table

##drop table

##alter table

##constraints

##not null

##unique

##primary key

##foreign key

##check

##default

##index

##auto increment

##views

##injection
 - sql 구문을 활용하여 데이타를 수정하는 것
 - sql parameters를 사용 추천
 - 
##hosting

##ms access functions

##mysql functions

##sql server functions

##oracle functions

##dates

##null functions

##operators

##data type

##db data types

##quick ref