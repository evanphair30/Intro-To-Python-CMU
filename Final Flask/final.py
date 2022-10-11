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

@app.route("/edit",methods = ['POST', 'GET'])
def edit():
    return "Homepage of GeeksForGeeks"

@app.route("/remove",methods = ['DELETE'])
def remove():
    return "Homepage of GeeksForGeeks"

@app.route("/home/<home_id>", methods=['GET', 'PUT', 'DELETE'])
def individual():
    return "Homepage of GeeksForGeeks"
  
if __name__ == "__main__":
    app.run(debug=True)