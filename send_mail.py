import requests

domain: str = 'sandboxe4caaed5b28d4847baef2e43b7d1e36c.mailgun.org'
api_key: str = '5b886c620b4622bdbe1f994bb7842f65-413e373c-3938144f'

def send_simple_message():
    return requests.post(
        f"https://api.mailgun.net/v3/{domain}/messages",
        auth=("api", api_key),
        data={"from": f"server@{domain}",
              "to": ["ben@drolet.cloud"],
              "subject": "Hello",
              "text": "Testing some Mailgun awesomness!"})

print(send_simple_message())
