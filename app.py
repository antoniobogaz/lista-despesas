from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

lista_despesas = [
    {"conta": "AGUA", "pagamento": 'PENDENTE', "valor": '250'},
    {"conta": "ENERGIA", "pagamento": 'PENDENTE', "valor": '400'},
    {"conta": "FINANCIAMENTO DO CARRO", "pagamento": 'PAGO', "valor": '2000'},
    {"conta": "IPVA", "pagamento": 'PAGO', "valor": '550'},
    {"conta": "LICENCIAMENTO MOTO", "pagamento": 'PAGO', "valor": '125'},
    {"conta": "IPTU", "pagamento": 'PENDENTE', "valor": '650'},
    {"conta": "ALIMENTAÇÃO", "pagamento": 'PAGO', "valor": '1100'},
    {"conta": "CARTÃO DE CRÉDITO", "pagamento": 'PENDENTE', "valor": '642'},
    {"conta": "EMPRÉSTIMO SANTANDER", "pagamento": 'PENDENTE', "valor": '980'},
    {"conta": "ROUPAS", "pagamento": 'PAGO', "valor": '150'},
]
# pagina principal-------------------------------------------------------------
@app.route('/')
def index():
    return render_template('index.html', lista=lista_despesas)

# Adicionar nova despesa-------------------------------------------------------
@app.route('/create')
def create():
    return render_template('create.html')



# Save-------------------------------------------------------------------------
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
    
#deletar------------------------------------------------------------------------
@app.route('/deletar', methods=['POST'])
def deletar():
    deleta = request.form['deleta']
    deleta= deleta.upper()
    if deleta == "":
        return redirect('/')
    for despesa in lista_despesas:
        if despesa not in lista_despesas:
            return redirect('/')
        if despesa['conta'].lower() == deleta.lower():
            lista_despesas.remove(despesa)
    return redirect('/')

#pesquisar---------------------------------------------------------------------
@app.route('/pesquisar', methods=['POST'])                                 
def pesquisar():
    lista_resultado = []
    resultado = request.form['pesquisa']
    resultado = resultado.upper()
    if resultado == "":
        return redirect('/')
    for indice in lista_despesas:
        if resultado in indice['conta'].upper():
            lista_resultado.append(indice)
            return render_template('Search.html', resultado=lista_resultado)
    for indice in lista_despesas:
        if resultado in indice['pagamento'].upper():
            lista_resultado.append(indice)
            return render_template('Search.html', resultado=lista_resultado)
    for indice in lista_despesas:
        if resultado in indice['valor'].upper():
            lista_resultado.append(indice)
            return render_template('Search.html', resultado=lista_resultado)        
    return redirect('/')
#-----------------------------------------------------------------------------
app.run(debug=True)