from flask import Flask, render_template, request, redirect
import string
import random

app = Flask(__name__)
url_mapping = {}


def generate_short_url():
    letters = string.ascii_letters + string.digits
    while True:
        short_url = ''.join(random.choice(letters) for _ in range(6))
        if short_url not in url_mapping.keys():
            return short_url


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/shorten', methods=['POST'])
def shorten():
    long_url = request.form['long_url']
    short_url = generate_short_url()
    url_mapping[short_url] = long_url
    return render_template('shortened.html', short_url=short_url)


@app.route('/<short_url>')
def redirect_to_long_url(short_url):
    if short_url in url_mapping:
        long_url = url_mapping[short_url]
        return redirect(long_url)
    else:
        return "Short URL not found."


if __name__ == '__main__':
    app.run(debug=True)
