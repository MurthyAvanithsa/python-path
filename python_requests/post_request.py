import requests

BASE_URL = "http://localhost:9090/"
SIGNUP="signup/"
TWEETS="tweets/"
#headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}


signup_form_data ={"yourname": "Murthy", "youremail": "murthyavsn@tecnics.com"}
response = requests.post(url=BASE_URL, data=signup_form_data)
print response.content

# data ={"apikey": "KUYHAAAA345AZ", "secret": "17865489346ABE#1087"}
# response = requests.post(url=BASE_URL+TWEETS, data=data)
# print response.content
