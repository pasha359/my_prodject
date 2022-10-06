from datetime import datetime
from flask import Flask, request, render_template

app = Flask(__name__, static_folder="./client", template_folder="./client")

all_message = []
msg_id =1
def add_message(sender, text):
    global msg_id
    new_message = {
        'sender':sender,
        'text': text,
        'time': datetime.now().strftime("%H:%M"),
        'msg_id':msg_id
    }
    msg_id += 1
    all_message.append(new_message)
    return all_message

add_message('pasha','hi')
add_message('juliya', 'hiyushki')

@app.route('/get_message')  #get_message?after=5
def get_message():
    after = int(request.args['after'])
    return {'message':all_message[after:]}

@app.route('/send_message') #/send_message?sender=Pasha&text=Hello
def send_message():
    sender = request.args['sender']
    text = request.args['text']
    add_message(sender,text)
    return {'result':True}

@app.route("/")
def chat_page():
    return render_template("chat.html")

app.run()



