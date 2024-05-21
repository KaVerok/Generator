from flask import Flask
import random

app = Flask(__name__)
    

@app.route("/")
def nachalo():
    # return '<h1>Hello, World!</h1>'
    return '<a href="/password_choice">Сгенерировать код</a>'

@app.route("/password_choice")
def pass_PS():
    return '<a href="/password_8">Пароль из 8 значений</a>'


@app.route("/password_4")
def pass_4():
    elements = "123456789QWERTYUIOPLKJHGFDSAZXCVBNMqwertyuioplkjhgfdsazxcvbnm+-/*!&$#?=@<>"
    password=''
    for i in range(4):
        password += random.choice(elements)
    return password

@app.route("/password_8")
def pass_8():
    elements = "123456789QWERTYUIOPLKJHGFDSAZXCVBNMqwertyuioplkjhgfdsazxcvbnm+-/*!&$#?=@<>"
    password=''
    for i in range(8):
        password += random.choice(elements)
    return password


app.run(debug=True)