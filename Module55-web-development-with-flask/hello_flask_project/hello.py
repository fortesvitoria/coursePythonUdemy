from flask import Flask

app = Flask(__name__)

@app.route("/") #decorator - ("/") - goes to the homepage
def hello_world():
    return '<h1 style = "color:green">Hello, World!</h1>' \
    '<p>Next line</p>'

#creating decorator
def bold_decor(func):
    def wrapper():
        result = func() # pega o retorno da função original
        return f'<b>{result}</b>'  # adiciona as tags <b>
    return wrapper


@app.route("/bye") 
@bold_decor
def bye_world():
    return "<p>Bye, World!</p>"

# @app.route("/<name>")  #<name> returns a variable that will be in the url and in the func below
# def greet(name):
#     return f"Hello {name}"

@app.route("/<name>/<int:number>")  #<path:name> ou <int:name> returns a variable that will be in the url and in the func below
def greet(name,number):
    return f"Hello {name}, you are {number} yeard old"


if __name__ == "__main__":
    app.run(debug=True) #same as flask run command on terminal . debug true to reload, so we dont have to stop the program everytime we change something

