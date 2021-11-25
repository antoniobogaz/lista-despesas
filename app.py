from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

tarefas = [
    {"texto": "Lavar Louça", "concluida": False},
    {"texto": "Passear com o cachorro", "concluida": True},
    {"texto": "Estudar mais para a prova", "concluida": False},
]
# pagina principal
@app.route('/')
def index():
    return render_template('index.html', lista=tarefas)

# pagina de adicionar nova tarefa
@app.route('/create')
def create():
    return render_template('create.html')

@app.route('/exemplo')
def create():
    return render_template('exemplo.html')


@app.route('/save', methods=['POST'])  # <form action="/save" method="POST">
def save():
    texto = request.form['texto']      # <input name="texto"/>
    tarefa = { "texto": texto, "concluida": False }
    tarefas.append(tarefa)
    return redirect('/')
    

app.run(debug=True)