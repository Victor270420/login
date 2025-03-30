from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Lista para armazenar os usuários
usuarios = []

@app.route('/')
def index():
    return render_template('index.html', usuarios=usuarios)

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    
    # Adiciona o usuário à lista
    usuarios.append({'username': username, 'password': password})
    
    return jsonify({'username': username, 'password': password, 'usuarios': usuarios})

if __name__ == '__main__':
    app.run(debug=True)
