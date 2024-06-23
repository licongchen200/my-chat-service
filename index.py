from flask import Flask, request
from src.chat import get_message, send_message, delete_message
from src.user import get_user, create_user, delete_user, sign_in

app = Flask(__name__)


@app.route('/health')
def health():
    return "ok"


@app.route('/user', methods = [ 'GET', 'POST', 'DELETE'])
def my_user():
    if request.method == "GET":
        return get_user()
    elif request.method == 'POST':
        user = request.get_json()
        return create_user(user["email"], user["firstname"], user["lastname"], user["password"], user["username"])
    elif request.method == 'DELETE':
        id = request.args.get("id", default=None, type=int)
        return delete_user(id)




@app.route('/message', methods = ['GET', 'POST', 'DELETE'])
def my_message():
    if request.method == 'GET':
        id = request.args.get('id', default=1, type=int)
        count = request.args.get('count', default=10, type=int)
        return get_message(id, count)
    if request.method == "POST":
        message = request.get_json()
        return send_message(message['sender'], message['receiver'], message['content'], '', message['is_group'])
    if request.method == "DELETE":
        id = request.args.get("id", default = None, type = int)
        return delete_message(id)

@app.route('/signin', methods = ['POST'])
def my_signin():
    if request.method == "POST":
        body = request.get_json()
        return sign_in(body['email'], body['password'])




if __name__ == "__main__":
    app.run(debug=True, port=8081, host='0.0.0.0')
