import requests

def chat_feather(message):
    r = requests.post(
        "https://api.deepai.org/api/text-generator",
        data={
            'text': message,
        },
        headers={'api-key': '4a4c76a8-df35-4832-818b-b9997a886416'}
    )
    
    return r.json()
