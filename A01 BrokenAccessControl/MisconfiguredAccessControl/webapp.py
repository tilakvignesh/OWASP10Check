from flask import Flask, request, redirect, url_for

app = Flask(__name__)

users = {
    "admin": "admin_password",
    "username": "password"
}

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    
    if username in users and users[username] == password:
        return redirect(url_for('dashboard', username=username))
    else:
        return "Login Failed", 401

@app.route('/dashboard/<username>')
def dashboard(username):
    if username == 'admin':
        return f"Welcome Admin, you can access everything!"
    elif username == 'username':
        return f"Welcome User, you can only access user content."
    else:
        return "Unauthorized", 403

@app.route('/admin')
def admin():
    if request.args.get('role') == 'admin':
        return "Welcome to the Admin Page! U must be an admin! There's no way you're not right?\n"
    else:
        return "Forbidden", 403

@app.route('/user')
def user():
    if request.args.get('role') in ['user', 'admin']:
        return "User Page"
    else:
        return "Forbidden", 403

if __name__ == "__main__":
    app.run(debug=True)
