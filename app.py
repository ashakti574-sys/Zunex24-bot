from flask import Flask, request
import requests

app = Flask(__name__)

INSTANCE_ID = "instance196001"
TOKEN = "di2i7fudl98iavuh"
ULTRAMSG_URL = f"https://api.ultramsg.com/{INSTANCE_ID}/messages/chat"

@app.route('/')
def home():
    return "Zunex24 Bot is LIVE!"

@app.route('/webhook', methods=['POST'])
def webhook():
    try:
        data = request.json
        if not data:
            return "ok", 200
        msg_data = data.get('data', {})
        incoming = msg_data.get('body', '').lower()
        sender = msg_data.get('from', '')
        if not sender or '@g.us' in sender:
            return "ok", 200
        reply = ""
        if any(w in incoming for w in ["hi", "hello", "hey", "namaste", "hlo"]):
            reply = "Namaste! Zunex24 me swagat hai!\n\n1. Price ke liye 'price' likho\n2. Collection ke liye 'collection' likho\n3. Order ke liye 'order' likho"
        elif "price" in incoming:
            reply = "Zunex24 Price List:\nShoes Rs 499 se\nT-shirt Rs 299 se\nJeans Rs 599 se\nBulk me 20% OFF!"
        elif "collection" in incoming:
            reply = "Nayi Collection aa gayi hai! Instagram @zunex24 par dekho. Kya photos bheju?"
        elif "order" in incoming:
            reply = "Order ke liye: Product, Size, Address bhejo. Team 5 min me confirm karegi!"
        else:
            reply = "Dhanyawad! Team jald contact karegi. Price ke liye 'price' likho. - Zunex24"
        if reply:
            payload = {"token": TOKEN, "to": sender, "body": reply}
            requests.post(ULTRAMSG_URL, data=payload)
    except Exception as e:
        print(e)
    return "ok", 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
