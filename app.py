from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

lista_despesas = [
    {"conta": "AGUA", "pagamento": 'PENDENTE', "valor": '15400'},
]
# pagina principal
@app.route('/')
def index():
    return render_template('index.html', lista=lista_despesas)

# Adicionar nova despesa
@app.route('/create')
def create():
    return render_template('create.html')



# Save
@app.route('/save', methods=['POST'])  # <form action="/save" method="POST">
def save():
    texto = request.form['conta']  
    pagamentos = request.form['pagamento']
    valores = request.form['valor']# <input name="texto"/>
    texto = texto.upper()
    pagamentos = pagamentos.upper()
    if texto == "" or pagamentos == "" or valores == "":
        return render_template('erroCreate.html')
    else:    
        tarefa = { "conta": texto, "pagamento": pagamentos, "valor": valores }
        lista_despesas.append(tarefa)
        return redirect('/')
    
#deletar
@app.route('/deletar', methods=['POST'])
def deletar():
    deleta = request.form['deleta']
    if deleta == "":
        return render_template('erro.html')
    for despesa in lista_despesas:
        if despesa['conta'].lower() == deleta.lower():
            lista_despesas.remove(despesa)
    return redirect('/')

#pesquisar
@app.route('/buscar', methods=['POST'])
def pesquisar():
    lista_resultado = []
    resultado = request.form['pesquisa']
    resultado = resultado.lower()
    if resultado == "":
        return render_template('erro.html')
    for indice in lista_despesas:
        if resultado in indice['conta'].lower():
            lista_resultado.append(indice)
    for indice in lista_despesas:
        if resultado in indice['pagamento'].lower():
            lista_resultado.append(indice)
    for indice in lista_despesas:
        if resultado in indice['valor'].lower():
            lista_resultado.append(indice)
    return redirect('/')


app.run(debug=True)