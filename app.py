from flask import Flask, request, send_from_directory

app = Flask(__name__)

@app.route('/AGACIU.mp3')
def muzyka():
	return send_from_directory('.','AGACIU.mp3')

LOGIN = "agaciu"
PASSWORD = "wieleMuch"

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
	<style>
	@keyframes pulse {
    		0% { transform: scale(1); }
    		50% { transform: scale(1.3); }
    		100% { transform: scale(1); }
}

.heart {
    font-size: 250px;
	color: red;
    animation: pulse 1s infinite;
}
</style>

<div style="text-align:center;">

<div class="heart">&#9829;</div>

<audio controls autoplay loop>
	<source src="/AGACIU.mp3" type="audio/mpeg">
</audio>

<h2 style="font-size:90px;">
Dziękuję że jesteś, Kocham Cię 🙂
</h2>

<p style="font-size:30px;">
To była ukryta wiadomość tylko dla Ciebie.
</p>

<p style="font-size:60px;">
Bo tylko dzięki Tobie Me serce bije dziś<br>
Z popiołów wstałem Nauczyłaś mnie żyć<br>
I dziś już nie umiem bez Ciebie śnić<br>
Bo tylko przy Tobie cokolwiek ma sens<br>
Gdy świat się zawali ja nie poddam się<br>
Gdy zabraknie Ci sił ja podniosę Cię
</p>

</div>
'''

    return '<h2>Zły login lub hasło 😄</h2>'

if __name__ == '__main__':
    app.run(debug=True)
