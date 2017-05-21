##컴프리헨션(Comprehension)

가독성과 사용성을 높이기 위해 한줄로표시?

예로 적어둠
```
for x in range(7):
    for y in range(4):
         x , y
    ```
아래와 같이 만들수있다.
    
```
[(x,y) for x in range(7) for y in range(4)]
```


