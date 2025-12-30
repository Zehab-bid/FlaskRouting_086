from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def index():
   return render_template("index.html")

@app.route("/inputnama")
def index2():
   return render_template("index2.html")

@app.route("/tampilnama")
def index3():
   name= request.args.get("nama_msh", "nilai default")
   return render_template("index3.html",name2=name)

if __name__ == '__main__':
   app.run(debug = True)