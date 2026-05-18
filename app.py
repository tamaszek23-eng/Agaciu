from flask import Flask, request

app = Flask(__name__)

LOGIN = "agaciu"
PASSWORD = "wielemuch"

@app.route('/')
def home():
    return '''
    <h2>Logowanie</h2>

    <form method="POST" action="/login">
        <input name="login" placeholder="login"><br><br>
        <input name="password" type="password" placeholder="hasło"><br><br>
        <button type="submit">Zaloguj</button>
    </form>
    '''

@app.route('/login', methods=['POST'])
def login():
    login = request.form.get('login')
    password = request.form.get('password')

    if login == LOGIN and password == PASSWORD:
        return '''
	<div style="text-align:center;">
        <h1 style="font-size:80px;">❤️</h1>
        <h2 style="font-size:60px;">Dziękuję że jesteś, Kocham Cię 🙂</h2>
        <p style="font-size:30px;">To była ukryta wiadomość tylko dla Ciebie.</p>
	</div>
        '''

    return '<h2>Zły login lub hasło 😄</h2>'

if __name__ == '__main__':
    app.run(debug=True)
