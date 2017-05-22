##선택 정렬

'''def selection_sort(ori_list):
    print('원본 리스트:', ori_list)
    # 주어진 리스트의 길이
    ori_len = len(ori_list)
    
    # 리스트길이-1번만큼 순회, 각 인덱스는 i에 지정
    for i in range(ori_len - 1):
        print('{}번째 loop입니다'.format(i + 1))
        cur_min_index = i
        print(' 현재 최소값은{}, 인덱스는{}'.format(
            ori_list[cur_min_index],
            cur_min_index + 1
        ))
        
        # loop내부에서 매 loop마다 리스트길이 - i(상위 인덱스)만큼 순회
        # 순회 시, i+1부터 리스트 전체길이까지 순회하여 비교하려는 첫번째 인덱스 이후부터 끝까지 순회
        for j in range(i + 1, ori_len):
            # cur_min_index가 가지는 값과 j인덱스가 가지는 값을 비교
            if ori_list[cur_min_index] > ori_list[j]:
                cur_min_index = j
                print('  {}번째 index의 {}값이 기존값보다 작음'.format(
                    cur_min_index + 1,
                    ori_list[cur_min_index]
                ))
        # 내부 loop가 끝난 후, cur_min_index의 값과 i인덱스의 값을 서로 바꿔준다
        ori_list[i], ori_list[cur_min_index] = ori_list[cur_min_index], ori_list[i]
        print('{}번째 loop결과 :{}'.format(i + 1, ori_list))'''
        
 - 리스트 길이를 구해서 n-1번째 까지 비교해서 작은 값을 제일 앞의 리스트값과 교환

##module
 - import로 다른 모듈을 불러온다
 - import로 함수를 불러와서 사용할 때 부르는 파일에서 실행이 먼저 실행이 된다.
  - 이러한 먼저실행되는 것을 막기위해 " __main__" 묶어서 사용한다
  
 - import를 사용하는데 두가지 방법이있다.
  - import (module name) 단점 중복되는 항목이 쓰일경우 마지막값이 나오게된다.
  - form (module name) import (함수명)(* : 모든 함수를 다가지고온다)
 - 모듈 불러올때 import 뒤에 alias를 사용하여 명칭을 지정할수있다.

##package
 - 모듈을 모아둔 폴더를 패키지라고한다
 - __ init __.py 를 넣어준다

##class
 -         
        
  