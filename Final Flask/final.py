from flask import Flask, render_template, make_response, jsonify, request, redirect, json

app = Flask(__name__)

with open('football.json') as json_file:
    data = json.load(json_file)

print (data)

@app.route("/")
def home():
    return render_template('home.html',title="Home Page")



@app.route('/roster', methods=['GET', 'POST'])
def roster():
    if request.method == 'GET':
        return make_response(jsonify(data), 200)
    elif request.method == 'POST':
        content = request.json
        roster_id = content['id']
        data[roster_id] = content
        data_obj = data.get(roster_id, {})
        print(data_obj)
        return make_response(jsonify(data_obj), 201)

@app.route('/roster/<roster_id>', methods=['GET', 'PUT', 'DELETE'])
def each_roster(roster_id):
    if request.method == 'GET':
        data_obj = data.get(roster_id, {})
        if data_obj:
            return make_response(jsonify(data_obj), 200)
        else:
            return make_response(jsonify(data_obj), 404)
    elif request.method == 'PUT':
        content = request.json
        data[roster_id] = content
        data_obj = data.get(roster_id, {})
        return make_response(jsonify(data_obj), 200)
#    elif request.method == 'DELETE':
#        if roster_id in data:
#            del data(roster_id)
#        return make_response(jsonify({}),204)


if __name__ == "__main__":
    app.run(debug=True)
