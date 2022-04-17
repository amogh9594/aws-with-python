from fnmatch import translate
from flask import Flask, render_template, request 
from translate import *
from sentiment import *
app = Flask(__name__)

pos = sentiment[0]
neg = sentiment[1]
neu = sentiment[2]


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/", nethods=['POST', 'GET'])
def main():
    if request.method == 'POST':
        input=request.form.get("input text")
        selected_lang= request.form.get("selected Language", None)
        if selected_lang is not None:
            lang = selected_lang
            translate=do_translate(input)
            sentiment=do_sentiment_analysis(input)
        return render_template("index.html", input=input, lang=lang, translate=translate, sentiment=sentiment, pos=pos, neg=neg, neu=neu)


if __name__ == "__main__" :
    app.run(debug=True)
