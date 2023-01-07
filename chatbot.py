#imports
from flask import Flask, render_template, request
from main import message_probability,check_all_messages
import re
app = Flask(__name__)


#define app routes
@app.route("/")
def index():
    return render_template("app.html")

@app.route("/get")
#function for the bot response
def get_bot_response():
    userText = request.args.get('msg')
    split_message = re.split(r'\s+|[,;?!.-]\s*', userText.lower())
    response = check_all_messages(split_message)
    return response

if __name__ == "__main__":
    app.run()
