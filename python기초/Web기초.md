# URL을 이용한 데이터 요청

```python
import requests

targetDt = '20190713' #yyyymmdd
weekGb = '0'
api_url = f'http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchWeeklyBoxOfficeList.json?key={key}&targetDt={targetDt}&weekGb={weekGb}'

response = requests.get(api_url).json()
# json형식의 경우 python dictionary 형식처럼 사용할 수 있다.
```

