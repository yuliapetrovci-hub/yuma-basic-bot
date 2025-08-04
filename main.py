import flask
import telegram

TOKEN = "8009723450:AAGQzCEH36BMYFGeYtrhGFz5F3vav2Sa8n0"
bot = telegram.Bot(token=TOKEN)

app = flask.Flask(__name__)

@app.route('/', methods=['POST'])
def webhook():
    update = telegram.Update.de_json(flask.request.get_json(force=True), bot)
    chat_id = update.message.chat.id
    text = update.message.text
    bot.send_message(chat_id=chat_id, text="Привіт! Це тест від Юми ☀️")
    return 'ok'

@app.route('/', methods=['GET'])
def index():
    return 'Бот працює!'

if __name__ == '__main__':
    app.run()
