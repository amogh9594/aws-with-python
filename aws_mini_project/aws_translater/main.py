from fnmatch import translate
from flask import Flask, render_template, request 
from translate import *
app = Flask(__name__)



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
        return render_template("index.html", input=input, lang=lang, translate=translate)


if __name__ == "__main__" :
    app.run(debug=True)