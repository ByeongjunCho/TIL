# Day5

## Telegram API 활용하기

### 텔레그램 메시지 보내기

* 텔레그램 API의 기본 URL은 다음과 같다. 

  ```text
  https://api.telegram.org/bot{mathod_name}
  ```

* 메시지 보내기

  ```python
  https://api.telegram.org/bot{mathod_name}/sendMessage
  ```

  * 필수 파라미터
    * `text` : 보낼 메시지 내용
    * `chat_id` : 사용자 id

  ```python
  import requests
  from decouple import config
  
  
  token = config('TELEGRAM_TOKEN')
  base_url = f"https://api.telegram.org/bot{token}"
  
  @app.route(f'/{token}', methods=['POST'])  #
  def telegram():
      response = request.get_json()
      chat_id = response.get('message').get('chat').get('id')
      
  	url = f'{base_url}/sendMessage?chat_id={chat_id}&text={text}'
  	requests.get(url)
  ```

  * **주의사항!!!** `token` 값은 별도의 환경변수로 관리해야 함.

    * `python-decouplt` 설치

    ```bash
    $ pip install python-decouple
    ```

    * `.env` 파일 생성

      ```
      TELEGRAM_TOKEN='ㅁㄴㅇㄹㄴㅁㅇㄹㄴㅁㅇㄻㅇㄴㄹ'
      ```

    * `.gitignore` 에 추가

      ```
      .env
      ```

    * 활용

      ```python
      from decouple import config
      token = config('TELEGRAM_TOKEN')
      ```

  

  ## Telegram webhook 설정

  `webhook` 은 텔레그램 서버에서 내가 설정한 서버의 url로 메시지를 전달해주는 설정을 뜻한다.

  여기서 주의할 점은, 반드시 url이 `https`가 설정되어야 하는데, 이를 위해서 개발 단계에서는 `ngrok`를 설치하여 활용하자!

  * `ngrok` 활용법

    * `ngrok.exe` 파일을 다운로드 받는다.

    * `cmd` 를 열어 해당 파일의 경로로 이동한다.

    * 아래의 명령어를 입력한다.

      ```bash
      $ ngrok http 5000
      ```

  * webhook url 설정

    아래의 텔레그램 API url에 요청을 보낸다.

    ```txt
    https://api.telegram.org/bot{mathod_name}/setWebhook?url={url}
    ```

    주의할 점은 `url` 을 전부 작성해야 한다. 요청은 크롬 주소창에 만들어진 URL을 입력하는 것으로 대체한다.

    예) `https://123.io/telegramtoken실제값을여기에추가`

  

  ## Heroku 배포

  `heroku` 는 무료로 서버에 배포하는 것을 도와주며 `https` 를 지원하여, 쉽고 빠르게 할 수 있다.

  1. pip 패키지 정보 추가

     ```bash
     $ pip freeze > requirements.txt
     ```

  2. `runtime.txt` 설정 추가

     ```
     python-3.7.3
     ```

  3. `Procfile`추가

     ```
     web: python app.py
     ```

  4. `app.py` 변경

     ```python
     if __name__ == '__main__':
         import os
         port = int(os.environ.get("PORT", 5000))
         app.run(host='0.0.0.0', port=port)
     ```

  5. `commit`

     ```bash
     $ git init
     $git add .
     git commit -m 'qwerty'
     ```

  6. `heroku cli` 다운로드

     구글에 heloku cli를 검색하여 다운로드한다.

  7. heroku app 설정 - 최초에 한번

     ```bash
     $ heroku login
     $ heroku create __프로젝트 이름을 여기에 작성__
     ```

  8. `push`

     ```bash
     $ git heroku origin master
     ```

## Naver Papago(번역기) 사용하기

1. 네이버 API 설정
   
   * `Naver Developer` 홈페이지에 가입하고 Papago 사용신청을 한다.
   
2. python에 다음과 같이 초기값을 설정한다.

   ```python
   import requests
   from decouple import config
   from pprint import pprint
   # 1. 네이버 API 설정
   naver_client_id = config('NAVER_CLIENT_ID')
   naver_client_secret = config('NAVER_CLIENT_SECRET')
   ```

3. 요청을 위해 `naver_url` 을 설정한다.

   ```python
   # 2. URL 설정
   naver_url = 'https://openapi.naver.com/v1/papago/n2mt' # papago 홈페이지
   ```

4. **Naver** 에서 요구하는 형식으로 아이디와 비밀번호, data를 설정하여 요청을 보낸다.

   ```python
   # 3. 요청보내기! POST
   headers = {'X-Naver-Client-Id': naver_client_id,
           'X-Naver-Client-Secret': naver_client_secret
           }
   data = {
       'source': 'ko',
       'target': 'en',
       'text': '결코 다시 전쟁'
   }
   
   response = requests.post(naver_url, headers=headers, data=data).json()
   ```

   * `json` 형식으로 결과를 보내준다.

5. 받은 결과에서 내가 필요한 값을 추출하여 print한다.

   ```python
   text = response.get('message').get('result').get('translatedText')
   print(text)
   ```



## Naver Clova 얼굴인식 사용

1. `data`로 보낼 이미지를 구성한다.

   ```python
   import requests
   from decouple import config
   from pprint import pprint
   
   # 0. 이미지 파일
   img_url = 'https://api.telegram.org/file/bot815471355:AAEXs3TbfrpoVRbYTUFHlTFzzddYjSAz_44/photos/file_2.jpg'
   
   response = requests.get(img_url, stream=True)
   image = response.raw.read()
   ```

   * `row.read()` 메서드를 이용해 형식을 변환해야 한다.

2. 네이버 API를 설정하고 요청을 보낸다.

   ```python
   # 1. 네이버 API 설정
   naver_client_id = config('NAVER_CLIENT_ID')
   naver_client_secret = config('NAVER_CLIENT_SECRET')
   
   # 2. URL 설정
   naver_url = 'https://openapi.naver.com/v1/vision/celebrity'
   # 3. 요청보내기! POST
   
   headers = {'X-Naver-Client-Id': naver_client_id,
           'X-Naver-Client-Secret': naver_client_secret
           }
   response = requests.post(naver_url, headers=headers, files={'image': image}).json()
   ```

   * Naver에서 받은 데이터는 `json`값이 되며, 여기서 필요한 값을 추출해야 한다.

3. `dictionary` key값을 이용해 원하는 값을 얻는다.

   ```python
   best = response.get('faces')[0].get('celebrity')
   
   if best.get('confidence') > 0.2:
       text = f"{best.get('confidence')*100}%만큼 {best.get('value')}를 닮으셨네요"
   else:
       text = "닮은 사람이 없어요"
   print(text)
   ```





# 이미지 가져오기

**텔레그렘에서 보낸 이미지를 Naver 얼굴인식기로 보내기 위해서는 여러 과정이 필요하다.**

1. 텔레그램에서 이미지 파일이 입력되면, 이미지 파일의 `file_id` 를 가져온다.

   ```python
   from pprint import pprint
   from flask import Flask, request
   import requests
   from decouple import config
   import random
   app = Flask(__name__)
   
   token = config('TELEGRAM_TOKEN')
   base_url = f"https://api.telegram.org/bot{token}"
   
   naver_client_id = config('NAVER_CLIENT_ID')
   naver_client_secret = config('NAVER_CLIENT_SECRET')
   
   ## -----본코딩---
   @app.route(f'/{token}', methods=['POST'])  #
   def telegram():
       response = request.get_json()
       chat_id = response.get('message').get('chat').get('id')
       # 사진 파일의 id를 가져온다
       file_id = response.get('message').get('photo')[-1].get('file_id')
   ```

2. 사진 파일의 `file_id`를 받아서 텔레그램 서버에 파일의 경로를 요청한다.

   ```python
   # 텔레그램 서버에 파일의 경로를 받아온다.
       file_response = requests.get(f'{base_url}/getFile?file_id={file_id}').json()
   ```

3. 파일 경로를 통해 `URL`을 만든다.

   ```python
   
   ```

   



## 텔레그램 챗봇에서 내가 쓴 글을 나의 서버로 보내는 방법

1. **텔레그램** 환경을 설치한다.

   * 텔레그램을 설치하고 `botfather` 에서 나의 챗봇을 만든다
   * 만들고 나서 나오는 토근 주소를 복사하여 저장한다.

2. **텔레그램** 챗봇이 받는 데이터를 내 서버에 전달하기 위해 **webHook** 환경을 구성한다.

   * 내 서버를 열고, 공용 서버를 만들기 위해 `ngrok`을 사용한다.

     ```bash
     ngrok https 5001
     ```

   * 내가 open한 서버 주소와 텔레그램 코드를 이용하여야 **webHook**을 할 수 있다.

     > https://api.telegram.org/{__내 텔레그램 코드 주소__}?url={ngrok 주소}/{내 텔레그램 코드 주소}

3. `flask` 를 이용해서 내 서버를 오픈한다.

   ```python
   from pprint import pprint
   from flask import Flask, request
   import requests
   from decouple import config
   
   app = Flask(__name__)
   
   token = config('TELEGRAM_TOKEN')
   base_url = f"https://api.telegram.org/bot{token}"
   @app.route(f'/{token}', methods=['POST'])  # 서버 연결을 위해 텔레그램 토큰을 추가
   def telegram():
       #.....
   ```

   * 내 서버와 텔레그램 쳇봇간의 연결을 위해 `텔레그램 토큰` 을 이용해야 한다.

4. `request` 를 이용해 데이터를 가지고온다.

   ```python
   #.....
   def telegram():
       response = request.get_json()
   ```

5. `message` 에 입력값이 존재하면, 해당 답을 보낸다.

```python
def telegram():
    response = request.get_json()
    # 만약에 메시지가 있으면
    if response.get('message'):
        # 사용자가 보낸 메시지를 text 변수에 저장, 사용자 정보는 chat_id에 저장
        text = response.get('message').get('text')
        chat_id = response.get('message').get('chat').get('id')

        if text=='호우':
            text = '장마임'
        if text=='패드립':
            text = '패드립 머신 가동'
        # url 만들어서 메시지 보내기
        api_url = f'{base_url}/sendMessage?chat_id={chat_id}&text={text}'
        requests.get(api_url)
    return 'OK', 200  # 200 : 응답 상태 코드
```





```bash
$ pip freeze > requrments.txt  
$ pip install -r requirements.txt
```

