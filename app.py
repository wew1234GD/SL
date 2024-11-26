from flask import Flask, render_template, request, redirect, url_for
import random
import string

app = Flask(__name__)

link_dict = {}

def generate_key():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=8))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/shorten', methods=['POST'])
def shorten():
    long_url = request.form['long_url']
    if long_url:
        short_key = generate_key()
        link_dict[short_key] = long_url
        short_url = f'http://{request.host}/{short_key}'
        return f'<a href="{short_url}">{short_url}</a>'
    return 'Введите ссылку'

@app.route('/<short_key>')
def redirect_to_url(short_key):
    long_url = link_dict.get(short_key)
    if long_url:
        return redirect(long_url)
    return 'Ссылка не найдена', 404

if __name__ == '__main__':
    app.run(debug=True)
