from machinetranslation.translator import french_to_english, english_to_french
from flask import Flask, render_template, request
#import json


app = Flask("Web Translator")

@app.route("/englishToFrench")
def englishToFrench():
    textToTranslate = request.args.get('textToTranslate')
    translated_text = english_to_french(textToTranslate)
    response = ("Translated text to French: " + str(translated_text))
    return response
    #return ("Translated text to French:",translated_text)

@app.route("/frenchToEnglish")
def frenchToEnglish():
    textToTranslate = request.args.get('textToTranslate')
    translated_text = french_to_english(textToTranslate)
    return ("Translated text to English: " + str(translated_text))

@app.route("/")
def renderIndexPage():
    # Write the code to render template
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)