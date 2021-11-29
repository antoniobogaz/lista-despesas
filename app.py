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
    valores = request.form['valor']# <input name="texto"/> recebe os dados do template create.html
    texto = texto.upper()
    pagamentos = pagamentos.upper() # transforma a string em maiúsculo
    if texto == "" or pagamentos == "" or valores == "": # se algum campo do formulário estiver em branco...
        return render_template('erroCreate.html') # ...retorna a página de erro "erroCreate.html"
    else:
        tarefa = { "conta": texto, "pagamento": pagamentos, "valor": valores } # senão, ele joga os valores para um dicionário
        lista_despesas.append(tarefa) # e adiciona para a "lista_despesas"
        return redirect('/') #redireciona para a pagina principal
    
#deletar------------------------------------------------------------------------
@app.route('/deletar', methods=['POST'])
def deletar():
    deleta = request.form['deleta'] #recebe a informação vinda do template "index.html"
    deleta= deleta.upper() # transforma a string em maiúsculo
    if deleta == "": # se o usuário não digitar nada...
        return redirect('/') #...ele da redirect para a página principal
    for despesa in lista_despesas:
        if despesa not in lista_despesas: # se a despesa não estiver contida na lista principal...
            return redirect('/') # ele também dará redirect para a página principal
        if despesa['conta'].upper() == deleta.upper(): # se a conta na lista_despesa for igual ao que o usuário informou no campo de excluir...
            lista_despesas.remove(despesa) #... ele remove
    return redirect('/') # e redireciona à pagina principal

#pesquisar---------------------------------------------------------------------
@app.route('/pesquisar', methods=['POST'])                                 
def pesquisar():
    lista_resultado = []
    resultado = request.form['pesquisa'] # recebe a informação venda do template "index.html"
    resultado = resultado.upper() # tranforma a # string em maiúsculo
    if resultado == "": # se o usuário não digitar nada e pesquisar
        return redirect('/') # ele dará redirect para a página principal
    for indice in lista_despesas:
        if resultado in indice['conta'].upper(): # se o resultado estiver na lista_despesas
            lista_resultado.append(indice) # adiciona à lista vazia criada
            return render_template('Search.html', resultado=lista_resultado) # e retorna a informação para ser exibida no template "Search.html"
        if resultado in indice['pagamento'].upper():
            lista_resultado.append(indice)
            return render_template('Search.html', resultado=lista_resultado)
        if resultado in indice['valor'].upper():
            lista_resultado.append(indice)
            return render_template('Search.html', resultado=lista_resultado)        
    return redirect('/') #retorna para a página principal
#-----------------------------------------------------------------------------
app.run(debug=True)