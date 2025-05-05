from flask import Flask, render_template,request,redirect
from db import Database
import api
import gpt

app = Flask(__name__,static_folder="static")
dbo = Database()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/register')
def register():
    return render_template('sign-up.html')

@app.route('/login')
def login():
    return render_template('sign-in.html')

@app.route('/Features')
def features():
    return render_template('Features.html')
    
@app.route('/Perform_registration', methods=['POST'])
def perform_registration():
    Name=request.form.get('user_ka_name')
    Mail_id=request.form.get('user_ka_email_id')
    Password=request.form.get('user_ka_password')
    response = dbo.insert(Name,Mail_id,Password)  
    
    if response == 0:
        return render_template('sign-up.html',message = "Email already exist")
    else:
        return render_template('sign-in.html', message = "Registration is successful kindly login")
    
@app.route('/Perform_login',methods=['POST'])
def perform_login():
    email = request.form.get('user_ka_email')
    password = request.form.get('user_ka_password')
    responses = dbo.verify(email,password)
    if responses:
        return redirect('/profile')
    else: 
        return render_template('sign-in.html', message = 'Invalid password or id')
    
@app.route('/profile')
def profile():
    return render_template('Features.html')  

@app.route('/NER')
def NER():
   return render_template('NER.html')

@app.route('/conversation')
def Perform_conversation():
    return render_template('CONVERSATION1.html')

@app.route('/Back to features')  
def back():
    return render_template('Features.html')

@app.route('/Perform_NER', methods=['POST'])
def Perform_ner():
    text = request.form.get('NER_Text')
    entity = request.form.get('Entity_Jo_Search_karni_he')
    response2 = api.ner(text,entity)
    return render_template('ner_output.html', response = response2)

@app.route('/perform_conversation_with_gpt', methods=['POST'])
def perform_conversation():
    userinput = request.form.get('Prompt')
    message = [{'role': 'user', 'content': userinput}]
    response3 = gpt.gpt_35_api(message)
    return render_template('CONVERSATION1.html', response = response3)
    
    
    
if __name__ == "__main__": 
    app.run(debug=True)