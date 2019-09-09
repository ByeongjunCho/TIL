# Git

`Git`은 `분산형 버전관리시스템(DVCS)` 이다.

* Window에서 `Git`을 사용하기 위해서는 `Git bash`를 반드시 설치해야 함.

* 참고자료
  * [Git Scm](https://git-scm.com/book/ko/v2)
  * [누구나 쉽게 이해할 수 있는 Git 입문](https://backlog.com/git-tutorial/kr/intro/intro1_1.html)

## Git 기본 명령어(로컬)

* 로컬에서 처음 Git을 활용하는 경우 아래의 설정을 해줘야 한다.

  ```bash
  $ git config --global user.name 'ByeongjunCho'
  $ git config --global user.email 'jjgk91@naver.com'
  ```

  커밋하는 사람(`autoher`)이 누구인지 설정. Github email이랑 다르면, Github에서 다른 사람이 커밋한 것으로 인식된다.

  *컴퓨터에서 한번만 설정해주면 된다.*

1. Git 저장소 설정

   ```bash
   $ git init
   Initialized empty Git repository in C:/Users/student/Desktop/새 폴더/.git/
   
   student@DESKTOP MINGW64 ~/Desktop/새 폴더 (master)
   
   $ git remote -v  # 현재 폴더가 어떤 git url과 연결되어 있는지 확인할 수 있다.
   origin  https://github.com/ByeongjunCho/TIL.git (fetch)
   origin  https://github.com/ByeongjunCho/TIL.git (push)
   ```

   * `git init`명렁어를 입력하면, 해당 디렉토리에 `.git/`폴더가 생성된다.
   * 모든 git과 관련된 내용은 해당 폴더에 담겨있다.
   * 정자소로 설정되었다면, `git bash`에서 `(master)`가 나타난다.
   * `git remote -v` 명령어를 통해 현재 폴더가 어떤 git url과 연결되어 있는지 확인할 수 있다.

2. Staging area(커밋 대상 목록)에 담기

   ```bash
   $ git add .
   $ git add <파일명>
   $ git add startcamp/
   ```

   * `git add` 명령어를 통해 특정 파일 혹은 폴더를 `commit` 할 목록(`Staging Area`, `INDEX`)에 담아 놓는다.

   * 반드시 `git status` 명령어를 통해 내가 원하는 파일이 반영되었는지 확인한다.

     ```bash
     $ git status
     ...
     Changes to be committed:
       (use "git rm --cached <file>..." to unstage) # add전 상태로 돌리는 명령어
     
             new file:   a.txt
     ```

3. 이력 남기기(`commit`)

   ```bash
   $ git commit -m '커밋메시지'
   ```

   * `commit` 은 현재 소스코드의 상태를 **스냅샷** 찍는 것과 동일하다.
   * `Staging Area` 에 담겨 있는 내용을 이력으로 남긴다.
   * 커밋메시지는 반드시 해당 이력의 내용을 정확하게 표현해야 한다.(보통 오픈소스 프로젝트, 회사 내에서 관련된 컨벤션이 존재한다.)

4. 커밋이력 확인하기

   ```bash
   $ git log
   commit 6a616e5bb5de06a793c167cbc7bf1b34cf72f6a1 (HEAD -> master)
   Author: ByeongjunCho <jjgk91@naver.com>
   Date:   Tue Jul 9 10:49:12 2019 +0900
   
       a.txt 생성
   
   $ git log -2  # 최근 2개만 생성
   ```

   * `git log -n` 옵션을 주면, 최근 n개의 커밋을 보여준다.
   * 커밋 이력을 남긴 이후에 커밋 메시지 변경, 삭제 등을 할 수 있는데 이 경우는 매우 조심해야 한다!

5. **git 상태 확인**

   **항상 모든 명령어를 입력하기 전에 아래의 명령어를 입력하는 습관을 들이자!**

   ```bash
   $ git status
   ```

6. commit메시지 변경

   ```bash
   $ git commit --amend
   ```

   * stage에 있는 파일들의 commit 메시지를 변경한다.

7. git 변경된 파일 복구

   ```bash
   $ git checkout -- <file_name>
   ```

8. 이전으로 돌아가기

   ```bash
   $ git reset --hard <hashcode> # 이력이 남지 않음(hard/soft)
   $ git revert  # 이력이 남음
   ```



## Git 원격 저장소 활용하기

원격 저장소(`remote repository`)는 `github`, `gitlab`, `bitbucket` 등 다양한 서비스를 사용할 수 있다.

1. 원격 저장소('remote repository') 설정

   ```bash
   $ git remote add origin __https://github.com__  # 해당 저장소의 url
   ```

   * 로컬 저장소에 최초에 한번만 등록하면 된다.
   * 원격 저장소(remote)를 `origin` 이라는 이름으로 정해진 url을 `등록(add)`하는 것이다.

2. 원격 저장소 `push`

   ```bash
   $git push origin master
   ```

   * `origin` 으로 설정된 원격 저장소에 `push` 한다.

3. 원격 저장소에서 `pull`

   ```bash
   $ git pull origin master
   ```

   * 원격 저장소에 새로운 변경 사항이 있는 경우 `pull`을 통해 받아온다.

4. `clone`

   ```bash
   $ git clone __url__
   ```

   * `clone` 은 원격 저장소에서 최초에 받아올 때 활용한다.



# gitignore

> git init을 하면 해당 파일을 작성하는 습관을 들이자!

`.gitignore` 에 작성된 파일 혹은 폴더 등은 git으로 관리되지 않는다. 예시는 다음과 같다.

```
__pycache__ # __pychche__ 폴더 안에 있는 내용 모두
*.zip		# 확장자가 zip인 파일 모두
profile.jpg # profile.jpg 파일
```

처음에는 직접 만들기보다 [gitignore](https://gitignore.io)에서 내 개발환경에 맞춰 만들어주는 파일을 적용하자.

예를 들면, pycharm을 쓰고 있을 때, `.idea/` 를 올리지 않는다거나, python에서는 `__pycache__/`를 올릴 필요는 없다.



# Git을 이용한 협업

1. Fork 작업
2. Fork한 저장소를 clone
3. 직접 코드 수정
   * 수정된 데이터는 그때그때 add, commit 를 하여 commit message가 꼬이지 않게 만들어야 좋다.
4. fork한 저장소로 push
5. 수정 후 상대방에게 merge요청



# 기타사항

git => (분산) 버전 관리 시스템

코드의 History를 관리하는 도구. 

분산형 버전 관리 시스템(Distributed Version Control System) => 관리가 쉬움

=> '[대괄호 주소]()'

dd => commit할 목록에 추가

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
$ git remote add origin https://github.com/ByeongjunCho/gittest.git # url주소
$ git push -u origin master # commit를 저장소에 저장  -u : 처음 한번만 사용하면 그 이후 -u 이후 값은 자동으로 입력된다. 
# git push -u이후 
# $ git push만 사용하게 하면 된다.
```

# Gitlab 사용법

```bash
git remote add gitlab <gitlab 주소>
git remote -v
```

```
gitlab  https://lab.ssafy.com/ByeongjunCho/daily.git (fetch)
gitlab  https://lab.ssafy.com/ByeongjunCho/daily.git (push)
origin  https://github.com/ByeongjunCho/daily.git (fetch)
origin  https://github.com/ByeongjunCho/daily.git (push)
```

```bash
git push origin master # github로 push
git push gitlab master # gitlab로 push
```





선택자(selector)

id : #____ >P

class : class=__BLUE__

/span : 



<span class = 'blue' id = 'ssafy'>

<p> <p>

> vi 명령어 모음
>
> * :wq => 저장하고 종료
> * i => 입력 모드 전환
> * 참조 : [https://cyberseo.tistory.com/entry/Vi-%EC%97%90%EB%94%94%ED%84%B0-%EC%82%AC%EC%9A%A9%EB%B2%95](https://cyberseo.tistory.com/entry/Vi-에디터-사용법)

