# import requests

# key = '39482ee966f81c52351ae45548ec214f'
# targetDt = '20190713' #yyyymmdd
# api_url = f'http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchWeeklyBoxOfficeList.json?key={key}&targetDt={targetDt}'
# print(api_url)

# response = requests.get(api_url).json()
# print(response)

import datetime
hundred = datetime.timedelta(days = 7*50)
dayy = datetime.datetime(2019, 7, 13) - hundred
print(type(dayy))
print(dayy)
print(str(dayy)[0:4])
