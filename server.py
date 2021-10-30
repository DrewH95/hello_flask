from flask import Flask
app = Flask (__name__)


@app.route ("/")          # The "@" decorator associates this route with the function immediately following
def hello_world():
    return "Hello World!" # Return the string 'Hello World!' as a response



@app.route("/dojo")
def dojo():
    return "Dojo!" 



@app.route("/say/<string:say>")
def say(say): 
    print(say) 
    return f"Hi, {say}!"



@app.route("/repeat/<int:number>/<string:word>")
def repeat_word(number, word):
    print(number, word)
    output = " "

    for i in range(0, number):
        output += f"<h1>{word}</h1>"
    
    return output



if __name__== "__main__":
    app.run (debug=True)
    # app.run(debug=True) should be the very last statement! 