from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/inputnama', methods=['GET'])
def inputnama():
    return render_template('index2.html')

@app.route('/tampilnama', methods=['GET'])
def tampilnama():
    name = request.args.get('nama_mhs', 'Tidak ada nama')
    return render_template('index3.html', name2=name)

if __name__ == '__main__':
    app.run(debug=True)
