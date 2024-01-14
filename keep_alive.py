from flask import Flask
from threading import Thread

app = Flask('')

@app.route('/')
def main():
	return '[英文]Bot Is Online \n[繁體中文] Bot 已上線'

def run():
    app.run(host="0.0.0.0", port=8080)

def keep_alive():
    server = Thread(target=run)
    server.start()