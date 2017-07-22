from microsoftbotframework import ReplyToActivity
import requests
import json

def echo_response(message):
  if message["type"] == "message":
    print(message)

    if message["type"] == "message":
        if "bitcoin" in message["text"]:

            r = requests.get("https://api.korbit.co.kr/v1/ticker")
            bitcoin_price = r.json()["last"]
            msg = "bitcoin price is %s" % bitcoin_price
            print(msg)
            ReplyToActivity(fill=message,
                            text=msg).send()