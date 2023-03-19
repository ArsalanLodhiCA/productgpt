import os
import re

import openai
from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)
openai.api_key = os.getenv("OPENAI_API_KEY")


@app.route("/", methods=("GET", "POST"))
def index():
    if request.method == "POST":
        product = request.form["product"]
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=product, #prompt=generate_prompt(product),
            temperature=0.6,
            max_tokens=150,
            top_p=1,
            frequency_penalty=1,
            presence_penalty=1
        )
        response_text = response.choices[0].text
        lines = re.split("\d+\. ", response_text)
        
        # Split the result string into a list of lines
        lines = lines.splitlines()

        # Use a list comprehension to strip leading whitespace from each line
        stripped_lines = [line.lstrip() for line in lines]

        # Join the stripped lines back together into a single string
        lines = '\n'.join(stripped_lines)

        # lines.remove('')
        # return redirect(url_for("index", result=lines))
        return render_template("index.html", result=lines)
        # return redirect(url_for("index", result=response.choices[0].text))

    result = request.args.get("result")
    return render_template("index.html", result=result)

def generate_prompt(product):
    return """Suggest differentiated topics for a machine learning curriculum to attract students.

Product: Machine Learning Engineering
Ideas: Deep Learning, Reinforcement Learning, Natural Langugage Processing, Computer Vision, Time Series Analysis, Unsupervised Learning, Bayesian Machine Learning, Explainable AI, Transfer Learning, Edge Computing
Product: {}
Ideas:""".format(
        product.capitalize()
    )
