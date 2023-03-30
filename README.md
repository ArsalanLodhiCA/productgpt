<p align="center">
  <img src="./static/idea.png" alt="ProductGPT" width="200" height="200">
</p>


# Product GPT
Generates ideas for product managers and entrepreneurs.

## Setup
If you don’t have Python installed, [install it from here.](https://www.python.org/downloads/) Then download the code by cloning this repository.

```
git clone https://github.com/ArsalanLodhiCA/productgpt.git
```

## Add your API Key
Navigate into the project directory and make a copy of the example environment variables file.

```
cp .env.example .env
```

## Run the app
Run the following commands in the project directory to install the dependencies and run the app. When running the commands, you may need to type python3/pip3 instead of python/pip depending on your setup.

```
pip install -r requirements.txt
flask run --host 0.0.0.0
```
Open http://localhost:5000 (or your public IP) in your browser and you should see the Product GPT!

## Closing
One limitation to keep in mind is that, for most OpenAI models, a single API request can only process up to 2,048 tokens (roughly 1,500 words) between your prompt and completion.
