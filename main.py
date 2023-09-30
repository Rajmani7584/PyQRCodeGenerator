from flask import Flask, render_template, request, jsonify
import png
import pyqrcode

app = Flask(__name__)

dataTypes = ['text', 'wifi', 'phone', 'url', 'whatsapp', 'upi']

@app.route('/')
def main0():
    return render_template("layout.html", dataTypes=dataTypes, index=0)

@app.route('/wifi')
def main2():
    return render_template("layout.html", dataTypes=dataTypes, index=1)

@app.route('/phone')
def main3():
    return render_template("layout.html", dataTypes=dataTypes, index=2)

@app.route('/url')
def main4():
    return render_template("layout.html", dataTypes=dataTypes, index=3)

@app.route('/whatsapp')
def main5():
    return render_template("layout.html", dataTypes=dataTypes, index=4)
@app.route('/upi')
def main6():
    return render_template("layout.html", dataTypes=dataTypes, index=5)

@app.route('/qrApi', methods=['POST'])
def genQr():
    data = request.get_json()
    key1 = data.get('data')
    print(key1)
    code = pyqrcode.create(key1)
    return jsonify({'data': f"data:image/png;base64,{code.png_as_base64_str(scale=8)}"})

app.run(None, 5000)