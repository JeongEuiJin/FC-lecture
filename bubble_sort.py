import random

#10개의 임의로 숫자 생성
random_list = [x for x in range(1,11)]
random.shuffle(random_list)

def bubble_sort(bubble_list):
    bubble_len = len(bubble_list) -1
    for i in range(bubble_len):
        print(i)
        for j in range(bubble_len-1):
            if bubble_list[j] > bubble_list[j+1]:
                bubble_list[j],bubble_list[j+1] = bubble_sort(j+1),bubble_list[j]
    print(bubble_list)


bubble_sort(random_list)