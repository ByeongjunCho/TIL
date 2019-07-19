import requests

key = '39482ee966f81c52351ae45548ec214f'
targetDt = '20190713' #yyyymmdd
weekGb = '0'
print(api_url)

response = requests.get(api_url).json()
# print(response)