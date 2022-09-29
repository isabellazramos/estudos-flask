from flask import Flask, redirect, url_for

app = Flask(__name__)


@app.route("/admin/")
def admin():
    return "<h1>Admin</h1>"


@app.route("/guest/<name>")
def guest(name):
    return "<p>olá guest <b>%s</b></p>" % name


@app.route("/user/<name>")
def user(name):
    if name == "admin":
        return redirect(url_for('admin'))

    else:
        return redirect(url_for('guest', name=name))

@app.route("/google")
def google():
    return redirect("http://www.google.com")

if __name__ == '__main__':
    app.run(debug=True)
