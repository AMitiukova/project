from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")

def index():
    page = request.args.get("page")
    return render_template("index.html", page = page)
    # return "<p>Hello, World!</p>"



if __name__ == '__main__':
    app.run(debug=True)