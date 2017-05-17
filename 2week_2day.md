# GIT 저장소
수정되는  것들에 따라 저장소가 달라짐

|        Untracked |   Unmodified - Modified   |    Staged    | 
|------------------|---------------------------|--------------|
| 작성되거나 수정되었을 때 | working area로  "add" 시키면 | "commit"로 등록 |


# GIT 로컬에서 github연동 시키는 명령어

```git reomte add (repositoy 생성한 주소)```


# GIT diff로 추적

diff로 unstaged에 있는 아직은 commit	하지 않은 것 중에서 수정된부분을 보여준다


# GIT 이름 변경 과 삭제

 - rm 로 파일 삭제후 git status 를 하면 삭제한 파일이 삭제가되어 staged에 남아있는다
이때 git rm 삭제파일 까지 진행을 해주면 완벽히 삭제가 이루어진다.

 - 이름 변경할 때는 git mv 파일이름 변경 이때 효과는 git rm 하고 git add 해주는것과 같은 효과이다.

# GIT Log 보는 방법
 - 사용 방법 
 - git log --oneline --graph --all 하게되면 트리 형식으로 보여주게된다
 - 
  





