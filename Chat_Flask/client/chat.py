from utils import set_timeout, fetch

last_seen_id = 0

send_message = document.getElementById("send_message")
sender = document.getElementById("sender")
message_text = document.getElementById("message_text")
chat_window = document.getElementById("chat_window")


def append_message(message):
    item = document.createElement('Li')
    item.className = 'list-group-item'
    item.innerHTML = f'[<b>{message["sender"]}</b>]: <span>{message["text"]}</span><span class="badge text-bg-light text-secondary">{message["time"]}</span>'
    chat_window.prepend(item)

async def send_message_click(e):
    await fetch(f'/send_message?sender={sender.value}&text={message_text.value}', method = 'GET')
    message_text.value = ''



async def load_fresh_messages():
    global last_seen_id
    result = await fetch(f"/get_message?after={last_seen_id}", method="GET")
    #chat_window.innerHTML = ""
    data = await result.json()
    all_messages = data["message"]
    for msg in all_messages:
        last_seen_id = msg['msg_id']
        append_message(msg)

    set_timeout(1, load_fresh_messages)

send_message.onclick = send_message_click
load_fresh_messages()
