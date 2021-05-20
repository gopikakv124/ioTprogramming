from flask import Flask

#Create a flask application
app = Flask(__name__)

#Define a function when <ip>:<port>/ is accessed on browser
@app.route('/')
def hello():
  return "hello world"	
# @app.route('/hello')
# def welcome():
#   #Return what you want to show on browser page
#   return "Welcome to Amrita Intelligent Infrastructure Data Management and Control Panel App. \n Use one of the options below."

if __name__ == '__main__':
  app.run(host="0.0.0.0",port=5000,debug=1)
