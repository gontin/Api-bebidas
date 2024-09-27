from flask import Flask, render_template
import requests

app = Flask(__name__)




@app.route('/bolo')
def index():
    url = "https://www.thecocktaildb.com/api/json/v1/1/search.php?s="
    response = requests.get(url)
    dados = response.json()
    bebidas = dados['drinks']
    return render_template('index.html', bebidas=bebidas)

if __name__ == '__main__':
    app.run(debug=True)