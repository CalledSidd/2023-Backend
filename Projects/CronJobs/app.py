from flask import Flask, request

app = Flask(__name__)


@app.route('/webhook', methods=['POST'])
def webHook():
    if request.method == 'POST':
        print("Data from webhook", request.json)
        return "Webhook Received"
    
app.run(host='0.0.0.0', port=8000)