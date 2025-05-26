from flask import Flask, render_template, request, url_for, redirect, flash, session

app = Flask(__name__)
# lista_tarefas = []

@app.route('/')
def pagina_principal():
    return render_template('index.html')

if __name__ == '__main__':
    with app.app_context():
        app.run(debug=True)