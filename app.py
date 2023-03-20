from flask import Flask, render_template,request

app = Flask(__name__)

@app.route('/', methods = ['GET','POST'])

def index():
    name = None
    email = None
    feedback = None
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get("email")
        feedback = request.form.get('feedback')
        with open('data.txt','r+') as file:
            file.write(f"Name:{name} Email:{email} feedback:{feedback}")
    return render_template('index.html',name = name,email = email,feedback = feedback)

app.run(host='0.0.0.0', port=81) 