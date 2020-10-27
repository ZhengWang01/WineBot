import requests
url = 'https://vp-chatbot.herokuapp.com/webhooks/rest/webhook' ##change rasablog with your app name
myobj = {
"message": "hi",
"sender": 1,
}
x = requests.post(url, json = myobj)
print(x.text)
