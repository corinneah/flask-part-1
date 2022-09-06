# run in terminal 
#python3 -m venv ~/.venvs/flask
#source ~/.venvs/flask/bin/activate
#pip3 install Flask
#pip freeze > requirements.txt

# import packages 
from flask import Flask

# creating the Flask application 
app = Flask(__name__)

# creating different routes 
@app.route('/') 
def home():
    return 'Hello World'

@app.route('/aboutus')
def aboutus():
    return 'My name is Corinne Harris and this is my Flask Application for HHA 504'

@app.route('/contactus')
def contactus():
    return 'If you have any comments, questions, or concerns please feel free to reach out to us.'

#
if __name__ == '__main__':
     app.run(debug=True, host='0.0.0.0', port=80)