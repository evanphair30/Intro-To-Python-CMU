from flask import Flask, render_template, make_response, jsonify, request, redirect, json
import sqlite3

app = Flask(__name__)

with open('football.json') as json_file:
    data = json.load(json_file)

print (data)

@app.route("/")
def home():
    return render_template('home.html',title="Home Page")

# Pass the required route to the decorator.
#@app.route('/result',methods = ['POST', 'GET'])
#def result():
#   if request.method == 'POST':
#      result = request.form
#      return render_template("result.html",result = result)

@app.route('/results',methods = ['POST', 'GET'])
def data():
    data = request.get_json
    test = request.form
    print(test)
    return jsonify(request.form)

#@app.route('/result',methods = ['POST', 'GET'])
#def data():
#    data = request.get_json
#    print(data)
#    return jsonify(request.form)

@app.route("/edit",methods = ['PUT', 'GET'])
def edit():
    if request.method == 'PUT':
        return "Homepage of GeeksForGeeks"
    elif request.method == 'GET':
        data = request.get_json
        test = request.form
        print(test)
        return jsonify(request.form)

@app.route("/remove",methods = ['DELETE'])
def remove():
    return render_template('remove.html',title="Remove")
        

@app.route("/<home_id>", methods=['GET', 'PUT', 'DELETE'])
def individual():
    if request.method == 'GET':
        return "Homepage of GeeksForGeeks"
    elif request.method == 'PUT':
        return "Homepage of GeeksForGeeks"
    elif request.method == 'DELETE':
        return "Homepage of GeeksForGeeks"
  
if __name__ == "__main__":
    app.run(debug=True)
