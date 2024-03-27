from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/home")
def index():
    page = request.args.get("page")
    return render_template("index.html", page = page)
 
@app.route("/tabulator")
def TabulatorDemo():
    #page = request.args.get("page")
    return render_template("TabulatorDemo.html")
    
if __name__ == '__main__':
    app.run(debug=True)