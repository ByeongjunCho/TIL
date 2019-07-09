











git => (분산) 버전 관리 시스템

코드의 History를 관리하는 도구. 

분산형 버전 관리 시스템(Distributed Version Control System) => 관리가 쉬움



add => commit할 목록에 추가

commit => 커밋(create a snapshot) 만들기

push => 현재까지 만든 commit를 서버에 올린다.



``` bash
$ touch a.txt  # 경로에 a.txt파일을 생성한다.
$ git init  # 초기화
$ student@DESKTOP MINGW64 ~/Desktop/gittest (master) # master를 통해 파일 관리
$ ls -al
total 8
drwxr-xr-x 1 student 197121 0  7월  9 09:13 ./
drwxr-xr-x 1 student 197121 0  7월  9 09:12 ../
drwxr-xr-x 1 student 197121 0  7월  9 09:13 .git/  # git init명령어로 .git폴더 생성
-rw-r--r-- 1 student 197121 0  7월  9 09:12 a.txt
```

```bash
student@DESKTOP MINGW64 ~/Desktop/gittest (master)
$ git status  # 현재 git의 상태
On branch master # 현재 master경로

No commits yet  # commit은 없음

Untracked files:
  (use "git add <file>..." to include in what will be committed) 

        a.txt

nothing added to commit but untracked files present (use "git add" to track)
```

현재 상황 : untracked

```bash
$ git add a.txt   # commit전 staging area상태로 변화
student@DESKTOP MINGW64 ~/Desktop/gittest (master)
$ git add a.txt

student@DESKTOP MINGW64 ~/Desktop/gittest (master)
$ git status
On branch master

No commits yet

Changes to be committed:
  (use "git rm --cached <file>..." to unstage)

        new file:   a.txt
```

 git add => commit목록으로 a.txt가 변화

```bash
student@DESKTOP MINGW64 ~/Desktop/gittest (master)
$ git commit -m 'a.txt'   # a.txt파일을 git commit에 추가
[master (root-commit) e1a23f0] a.txt
 1 file changed, 0 insertions(+), 0 deletions(-)
 create mode 100644 a.txt

$ git status
On branch master
nothing to commit, working tree clean

student@DESKTOP MINGW64 ~/Desktop/gittest (master)

$ git log
commit e1a23f0d3c0d499504100031df5b4fde6a8f51d0 (HEAD -> master)
Author: ByeongjunCho <jjgk91@naver.com>
Date:   Tue Jul 9 09:20:29 2019 +0900

    a.txt

$ git diff HEAD~1 HEAD  # 변화 확인

$ git add .  # 모든 파일 commit대기

```

```bash
# 미리 github홈페이지에서 저장소를 만든 경우
git remote add origin https://github.com/ByeongjunCho/gittest.git # url주소
git push -u origin master # commit를 저장소에 저장
```

> vi 명령어 모음
>
> * :wq => 저장하고 종료
> * i => 입력 모드 전환
> * 참조 : [https://cyberseo.tistory.com/entry/Vi-%EC%97%90%EB%94%94%ED%84%B0-%EC%82%AC%EC%9A%A9%EB%B2%95](https://cyberseo.tistory.com/entry/Vi-에디터-사용법)

