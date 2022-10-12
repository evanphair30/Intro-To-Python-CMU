from flask import Flask, render_template, make_response, jsonify, request, redirect
import sqlite3
  
app = Flask(__name__)

@app.route("/")
def home():
    return render_template('home.html',title="Home Page")

# Pass the required route to the decorator.
@app.route('/result',methods = ['POST', 'GET'])
def result():
   if request.method == 'POST':
      result = request.form
      return render_template("result.html",result = result)

@app.route("/edit",methods = ['PUT', 'GET'])
def edit():
    if request.method == 'PUT':
        return "Homepage of GeeksForGeeks"
    elif request.method == 'GET':
        return "Hello"

@app.route("/remove",methods = ['DELETE'])
def remove():
    if request.method == 'DELETE':
        return "Homepage of GeeksForGeeks"

@app.route("/home/<home_id>", methods=['GET', 'PUT', 'DELETE'])
def individual():
    if request.method == 'GET':
        return "Homepage of GeeksForGeeks"
    elif request.method == 'PUT':
        return "Homepage of GeeksForGeeks"
    elif request.method == 'DELETE':
        return "Homepage of GeeksForGeeks"
  
if __name__ == "__main__":
    app.run(debug=True)
