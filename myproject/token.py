import jwt
import datetime
from dotenv import load_dotenv
load_dotenv()
import os
key=str(os.getenv('Secret_Key'))
def generatejwt():
    key=str(os.getenv('Secret_Key'))
    payload = {
    "username": "admin",
    "exp": datetime.datetime.utcnow() + datetime.timedelta(days=1)
    }
    return (jwt.encode(payload, key, algorithm='HS256'))


def verifyjwt(username, token):

    decoded_token = jwt.decode(token, key, algorithms=['HS256'])
    return decoded_token['username']==username